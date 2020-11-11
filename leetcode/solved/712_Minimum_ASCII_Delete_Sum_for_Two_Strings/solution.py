#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Note:
0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def rec(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            ret = []
            if i < len(s1):
                ret.append(ord(s1[i]) + rec(i+1, j))
            if j < len(s2):
                ret.append(ord(s2[j]) + rec(i, j+1))
            if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                ret.append(rec(i+1, j+1))
            return min(ret)
        return rec(0, 0)


@pytest.mark.parametrize('s1, s2, expected', [
    ("sea", "eat", 231),
    ("delete", "leet", 403),
])
def test(s1, s2, expected):
    assert expected == Solution().minimumDeleteSum(s1, s2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
