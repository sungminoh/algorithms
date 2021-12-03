#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6

Constraints:

	1 <= m, n <= 100
	It's guaranteed that the answer will be less than or equal to 2 * 109.
"""
import sys
import math
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
        return math.comb(m-1 + n-1, m-1)


@pytest.mark.parametrize('m, n, expected', [
    (3, 7, 28),
    (3, 2, 3),
    (7, 3, 28),
    (3, 3, 6),
])
def test(m, n, expected):
    assert expected == Solution().uniquePaths(m, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
