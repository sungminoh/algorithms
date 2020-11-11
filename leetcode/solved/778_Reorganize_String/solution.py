#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

	S will consist of lowercase letters and have length in range [1, 500].
"""
import sys
from heapq import heappop
from heapq import heappush
from collections import defaultdict
import pytest


class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt = defaultdict(int)
        for x in S:
            cnt[x] += 1
            if cnt[x] > (len(S)+1)//2:
                return ''
        h = []
        for x, c in cnt.items():
            heappush(h, (-c, x))
        ret = []
        while h:
            nc, x = heappop(h)
            c = -nc - 1
            ret.append(x)
            if not h:
                if c:
                    return ''
                break
            nc2, x2 = heappop(h)
            c2 = -nc2 - 1
            ret.append(x2)
            if c > 0:
                heappush(h, (-c, x))
            if c2 > 0:
                heappush(h, (-c2, x2))
        return ''.join(ret)


@pytest.mark.parametrize('S, expected', [
    ("aab", "aba"),
    ("aaab", "")
])
def test(S, expected):
    assert expected == Solution().reorganizeString(S)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
