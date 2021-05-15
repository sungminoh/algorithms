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

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:

	m == obstacleGrid.length
	n == obstacleGrid[i].length
	1 <= m, n <= 100
	obstacleGrid[i][j] is 0 or 1.
"""
import sys
from typing import List
import pytest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        12/30/2017 23:44
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        l = [1]*len(obstacleGrid[0])
        try:
            obstacle_idx = obstacleGrid[0].index(1, 0)
            l[obstacle_idx:] = [0]*(len(obstacleGrid[0]) - obstacle_idx)
        except Exception:
            pass
        for i, row in enumerate(obstacleGrid[1:]):
            if row[0] == 1:
                l[0] = 0
            for i in range(1, m):
                l[i] = (l[i-1] + l[i]) if row[i] == 0 else 0
        return l[-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        def neighbors(i, j):
            directions = [(1, 0), (0, 1)]
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0<=x<n and 0<=y<m:
                    yield x, y

        def dfs(i, j):
            if obstacleGrid[i][j] != 0:
                return 0
            if i == n-1 and j == m-1:
                return 1
            obstacleGrid[i][j] = 1
            cnt = 0
            for x, y in neighbors(i, j):
                cnt += dfs(x, y)
            obstacleGrid[i][j] = 0
            return cnt

        return dfs(0, 0)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        DP(i, j) = DP(i-1, j) + DP(i, j-1) (if obstacleGrid[i][j] == 0)
                 = 0                       (otherwise)
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (m+1) for _ in range(2)]
        # initial case
        dp[1][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i, row in enumerate(obstacleGrid):
            # clean up the current dp row in case it is used
            for j in range(m):
                dp[i%2][j] = 0
            for j, e in enumerate(row):
                if obstacleGrid[i][j] == 0:
                    dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j-1]
        return dp[(n-1)%2][-2]


@pytest.mark.parametrize('obstacleGrid, expected', [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1),
    ([[1]], 0),
    ([[0,0,0,0],
      [0,1,0,0],
      [0,0,0,0],
      [0,0,1,0],
      [0,0,0,0]], 7),
    ([[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]], 13594824),
])
def test(obstacleGrid, expected):
    assert expected == Solution().uniquePathsWithObstacles(obstacleGrid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
