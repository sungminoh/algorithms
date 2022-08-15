#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

	1 <= m, n <= 100
"""
import math
import sys
import pytest


class Solution:
    def uniquePaths(self, m, n):
        """12/26/2017 18:40"""
        l = [1]*m
        for _ in range(n-1):
            for i in range(1, m):
                l[i] += l[i-1]
        return l[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        """11/28/2021 23:17"""
        return math.comb(m-1 + n-1, m-1)

    def uniquePaths(self, m: int, n: int) -> int:
        """
        For board size m+1, n+1,
        total m+n moves(m going down, n going right) are required.
        = (m+n) C m
        = (m+n)! / m! n!
        = n+1 * ... * n+m / 1 * ... * m
        """
        if m > n:
            return self.uniquePaths(n, m)
        m -= 1
        n -= 1
        numerator = 1
        denominator = 1
        for i in range(1, m+1):
            numerator *= n+i
            denominator *= i
        return numerator // denominator


@pytest.mark.parametrize('m, n, expected', [
    (3, 7, 28),
    (3, 2, 3),
])
def test(m, n, expected):
    assert expected == Solution().uniquePaths(m, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
