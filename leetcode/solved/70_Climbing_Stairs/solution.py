#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

	1 <= n <= 45
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def climbStairs(self, n):
        """12/31/2017 01:49"""
        memo = [1, 2]
        for i in range(2, n):
            memo[i%2] = sum(memo)
        return memo[(n-1)%2]

    def climbStairs(self, n: int) -> int:
        """Oct 13, 2021 10:57"""
        two = 1
        one = 1
        for i in range(2, n+1):
            new = one+two
            two = one
            one = new
        return one

    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        """Feb 19, 2023 15:07"""
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


@pytest.mark.parametrize('n, expected', [
    (2,2),(3,3),
])
def test(n, expected):
    assert expected == Solution().climbStairs(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
