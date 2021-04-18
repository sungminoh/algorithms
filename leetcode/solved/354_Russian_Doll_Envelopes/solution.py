#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
from pathlib import Path
import json
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        DFS
        """
        envelopes.sort()

        @lru_cache(None)
        def dfs(i):
            if i == 0:
                return 1
            ret = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    ret = max(ret, 1+dfs(j))
            return ret

        return max(dfs(i) for i in range(len(envelopes))) if envelopes else 0

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        envelopes = set(tuple(x) for x in envelopes)
        ws, hs = map(list, list(zip(*envelopes)))
        ws.sort()
        hs.sort()

        # init dp
        wd = {w: i for i, w in enumerate(ws)}
        hd = {h: i for i, h in enumerate(hs)}
        dp = [[(0, (0, 0))]*(len(hs)+1) for _ in range(len(ws)+1)]
        for w, h in envelopes:
            dp[wd[w]][hd[h]] = (1, (w, h))

        # dp
        for i, w in enumerate(ws):
            for j, h in enumerate(hs):
                pw_count, (pww, pwh) = dp[i-1][j]
                ph_count, (phw, phh) = dp[i][j-1]
                if (w, h) in envelopes:
                    from_previous_w = pw_count + (1 if w>pww and h>pwh else 0)
                    from_previous_h = ph_count + (1 if w>phw and h>phh else 0)
                    if from_previous_w > from_previous_h:
                        if w>pww and h>pwh:
                            dp[i][j] = from_previous_w, (w, h)
                        else:
                            dp[i][j] = from_previous_w, (pww, pwh)
                    else:
                        if w>phw and h>phh:
                            dp[i][j] = from_previous_h, (w, h)
                        else:
                            dp[i][j] = from_previous_h, (phw, phh)
                else:
                    if pw_count > ph_count:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]

        return dp[-2][-2][0]

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        def binsearch(arr, v):
            s, e = 0, len(arr)-1
            while s <= e:
                m = (s+e)//2
                if arr[m] >= v:
                    e = m-1
                else:
                    s = m+1
            return e+1

        # dedup
        envelopes = list(set(tuple(x) for x in envelopes))
        # sort by w increasing, h decresing
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # n*logn longest increasing sub sequence on heights
        # hs[i] means the minimum value of the last element of the longest
        # increasing sequence whose length is i.
        hs = []
        for _, h in envelopes:
            i = binsearch(hs, h)
            if i < len(hs):
                hs[i] = h
            else:
                hs.append(h)
        return len(hs)


@pytest.mark.parametrize('envelopes, expected', [
    ([[5,4],[6,4],[6,7],[2,3]], 3),
    ([[1,1],[1,1],[1,1]], 1),
    ([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]], 5),
    ([[10,8],[1,12],[6,15],[2,18]], 2),
    (json.load(open(Path(__file__).parent/'testcase.json')), 129),
    (json.load(open(Path(__file__).parent/'testcase2.json')), 117),
])
def test(envelopes, expected):
    assert expected == Solution().maxEnvelopes(envelopes)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
