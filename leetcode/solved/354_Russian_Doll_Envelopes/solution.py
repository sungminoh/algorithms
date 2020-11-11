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


def bisearch(l, v):
    s, e = 0, len(l)-1
    while s <= e:
        m = (s + e) >> 1
        if l[m] < v:
            s = m+1
        elif l[m] > v:
            e = m-1
        else:
            return m
    return e+1


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for i, (w, h) in enumerate(envelopes):
            j = bisearch(tails, h)
            if j < len(tails):
                tails[j] = h
            else:
                tails.append(h)
        return len(tails)

    def _maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()

        @lru_cache(None)
        def rec(i):
            if i == 0:
                return 1
            ret = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    ret = max(ret, 1+rec(j))
            return ret

        return max(rec(i) for i in range(len(envelopes))) if envelopes else 0


@pytest.mark.parametrize('envelopes, expected', [
    ([[5,4],[6,4],[6,7],[2,3]], 3),
    ([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]], 5),
    ([[10,8],[1,12],[6,15],[2,18]], 2),
    (json.load(open(Path(__file__).parent/'testcase.json')), 129),
])
def test(envelopes, expected):
    assert expected == Solution().maxEnvelopes(envelopes)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
