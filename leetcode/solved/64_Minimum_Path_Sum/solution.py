#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 200
	0 <= grid[i][j] <= 100
"""
from typing import List
import pytest
import sys


class Solution:
    def minPathSum(self, grid):
        """Dec 28, 2017 19:42"""
        memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
        memo[0][0] = grid[0][0]
        for j in range(1, len(grid[0])):
            memo[0][j] = memo[0][j-1] + grid[0][j]
        for i in range(1, len(grid)):
            memo[i][0] = memo[i-1][0] + grid[i][0]

        def short_to(i, j):
            if memo[i][j] >= 0:
                return memo[i][j]
            memo[i][j] = min(short_to(i-1, j), short_to(i, j-1)) + grid[i][j]
            return memo[i][j]
        return short_to(len(grid)-1, len(grid[0])-1)

    def minPathSum(self, grid: List[List[int]]) -> int:
        """Apr 23, 2023 21:34"""
        n = len(grid[0])
        cost = [float('inf')] * (n+1)
        cost[0] = 0
        for row in grid:
            _cost = [0] * n
            _cost[-1] = float('inf')
            for j in range(n):
                _cost[j] = min(cost[j], _cost[j-1]) + row[j]
            cost = _cost
        return cost[-1]


@pytest.mark.parametrize('args', [
    (([[1,3,1],[1,5,1],[4,2,1]], 7)),
    (([[1,2,3],[4,5,6]], 12)),
    (([[1,2],[1,1]], 3)),
])
def test(args):
    assert args[-1] == Solution().minPathSum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
