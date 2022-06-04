#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

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

	m == obstacleGrid.length
	n == obstacleGrid[i].length
	1 <= m, n <= 100
	obstacleGrid[i][j] is 0 or 1.
"""
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """12/30/2017 23:44"""
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
        05/13/2021 09:14
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

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Top down DP by recursion
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 1

        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1-obstacleGrid[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            return dp(i-1, j) + dp(i, j-1)

        return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Bototm up DP by recursion
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 1

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        rows = [[0]*n for _ in range(2)]
        rows[0][0] = 1-obstacleGrid[0][0]
        for j in range(1, n):
            rows[0][j] = min(rows[0][j-1], 1-obstacleGrid[0][j])

        for i in range(1, m):
            rows[i%2][0] = min(rows[(i-1)%2][0], 1-obstacleGrid[i][0])
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    rows[i%2][j] = 0
                else:
                    rows[i%2][j] = rows[(i-1)%2][j] + rows[i%2][j-1]

        return rows[(m-1)%2][-1]


@pytest.mark.parametrize('obstacleGrid, expected', [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1),
    ([[1,0]], 0),
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
