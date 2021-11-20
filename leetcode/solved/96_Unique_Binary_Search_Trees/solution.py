#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1

Constraints:

	1 <= n <= 19
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def numTrees(self, n):
        """05/06/2018 06:03"""
        memo = {}
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
        s = sum(max(self.numTrees(i-1), 1) * max(self.numTrees(n-i), 1) for i in range(1, n+1))
        memo[n] = s
        return s

    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        """
        Top-down Recursion
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if n <= 1:
            return 1
        ret = 0
        for k in range(n):
            ret += self.numTrees(k)*self.numTrees(n-k-1)
        return ret

    def numTrees(self, n: int) -> int:
        """
        Bottom-up dp
        Recursion
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        memo = [0]*(n+1)
        memo[0] = memo[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                memo[i] += memo[j] * memo[i-j-1]
        return memo[-1]


@pytest.mark.parametrize('n, expected', [
    (3, 5),
    (1, 1),
])
def test(n, expected):
    assert expected == Solution().numTrees(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
