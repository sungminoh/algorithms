#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:

	1 <= s.length, t.length <= 1000
	s and t consist of English letters.
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    def numDistinct(self, s, t):
        """08/15/2018 06:17"""
        @lru_cache(maxsize=None)
        def foo(i, j):
            if j >= len(t):
                return 1
            cnt = 0
            for k in range(i, len(s)-len(t)+j+1):
                if s[k] == t[j]:
                    cnt += foo(k+1, j+1)
            return cnt

        if len(t) > len(s):
            return 0
        if s == t:
            return 1
        chars = set(t)
        s = [c for c in s if c in chars]
        return foo(0, 0)

    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j == len(t):
                return 1
            while i < len(s) and s[i] != t[j]:
                i += 1
            if i == len(s):
                return 0
            return dp(i+1, j+1) + dp(i+1, j)

        return dp(0, 0)

    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j == len(t):
                return 1
            ret = 0
            for k in range(i, len(s)-(len(t)-j)+1):
                if s[k] == t[j]:
                    ret += dp(k+1, j+1)
            return ret

        return dp(0, 0)


@pytest.mark.parametrize('s, t, expected', [
    ("rabbbit", "rabbit", 3),
    ("babgbag", "bag", 5),
    ("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcaccac", "ceadbaa", 8556153),
])
def test(s, t, expected):
    assert expected == Solution().numDistinct(s, t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

