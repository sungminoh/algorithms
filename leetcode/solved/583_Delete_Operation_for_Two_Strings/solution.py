#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:

	1 <= word1.length, word2.length <= 500
	word1 and word2 consist of only lowercase English letters.
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """06/13/2020 10:44"""
        @lru_cache(None)
        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
            m = 0
            if word1[i] == word2[j]:
                m = max([m, lcs(i-1, j-1) + 1])
            else:
                m = max([lcs(i-1, j), lcs(i, j-1)])
            return m
        lcs_length = lcs(len(word1)-1, len(word2)-1)
        return len(word1) + len(word2) - (2 * lcs_length)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        Top-down DP (recursion)
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        @lru_cache(None)
        def rec(i, j):
            if word1[i:] == word2[j:]:
                return 0
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            ret = float('inf')
            if word1[i] == word2[j]:
                ret = min(ret, rec(i+1, j+1))
            else:
                ret = min(ret, 1+rec(i+1, j), 1+rec(i, j+1))
            return ret
        return rec(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        """05/19/2021 10:17
        Bottom-up DP
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        n, m = len(word1)+1, len(word2)+1
        dp = []
        dp.append(list(range(m)))
        dp.append([float('inf')]*m)
        for i in range(1, n):
            # init
            for k in range(m): dp[i%2][k] = float('inf')
            for j in range(m):
                if j == 0:
                    dp[i%2][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i%2][j] = min(dp[i%2][j], dp[(i-1)%2][j-1])
                else:
                    dp[i%2][j] = min(dp[i%2][j], 1 + dp[(i-1)%2][j], 1 + dp[i%2][j-1])
        return dp[(n-1)%2][-1]


    def minDistance(self, word1: str, word2: str) -> int:
        """06/19/2022 16:02"""
        @lru_cache(None)
        def dfs(i, j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if word1[i] != word2[j]:
                return min(dfs(i+1, j), dfs(i, j+1)) + 1
            return dfs(i+1, j+1)

        return dfs(0, 0)


@pytest.mark.parametrize('word1, word2, expected', [
    ("sea", "eat", 2),
    ("leetcode", "etco", 4),
])
def test(word1, word2, expected):
    assert expected == Solution().minDistance(word1, word2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
