#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

	Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
	Paste: You can paste the characters which are copied last time.

Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:

Input: n = 1
Output: 0

Constraints:

	1 <= n <= 1000
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def minSteps(self, n: int) -> int:
        """Jul 02, 2020 00:49"""
        @lru_cache(None)
        def rec(n):
            if n == 1:
                return 0
            m = float('inf')
            for i in range(1, n):
                if n % i == 0:
                    m =min(m, rec(i) + (n//i))
            return m
        return rec(n)

    def minSteps(self, n: int) -> int:
        """Nov 13, 2024 07:26"""
        @lru_cache(None)
        def dp(cur, copied):
            if cur == n:
                return 0
            ret = n
            if cur != copied:
                ret = min(ret, dp(cur, cur) + 1)
            if copied > 0 and cur + copied <= n:
                ret = min(ret, dp(cur+copied, copied) + 1)
            return ret

        return dp(1, 0)

    def minSteps(self, n: int) -> int:
        """Dec 05, 2024 12:35"""
        @lru_cache(None)
        def dp(cur, copied):
            if cur > n:
                return float('inf')
            ret = float('inf')
            if cur == n:
                ret = 0
            if copied != cur:
                ret = min(ret, dp(cur, cur) + 1)
            if copied:
                ret = min(ret, dp(cur + copied, copied) + 1)
            return ret

        return dp(1, 0)


@pytest.mark.parametrize('args', [
    ((3, 3)),
    ((1, 0)),
])
def test(args):
    assert args[-1] == Solution().minSteps(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
