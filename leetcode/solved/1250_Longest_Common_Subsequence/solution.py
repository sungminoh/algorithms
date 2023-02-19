#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

	1 <= text1.length, text2.length <= 1000
	text1 and text2 consist of only lowercase English characters.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Oct 11, 2021 09:07"""
        @lru_cache(None)
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))

        return dp(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Oct 11, 2021 09:15"""
        pre = [0]*(len(text2)+1)
        for i in range(len(text1)):
            cur = [0]*(len(text2)+1)
            for j in range(len(text2)):
                cur[j] = (1+pre[j-1]) if text1[i] == text2[j] else max(pre[j], cur[j-1])
            pre = cur
        return pre[-2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Feb 19, 2023 15:22"""
        m, n = len(text1), len(text2)

        @lru_cache(None)
        def lcs(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + lcs(i+1, j+1)
            return max(lcs(i+1, j), lcs(i, j+1))

        return lcs(0, 0)


@pytest.mark.parametrize('text1, text2, expected', [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
])
def test(text1, text2, expected):
    assert expected == Solution().longestCommonSubsequence(text1, text2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
