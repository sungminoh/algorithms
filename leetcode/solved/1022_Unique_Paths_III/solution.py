#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n integer array grid where grid[i][j] could be:

	1 representing the starting square. There is exactly one starting square.
	2 representing the ending square. There is exactly one ending square.
	0 representing empty squares we can walk over.
	-1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 20
	1 <= m * n <= 20
	-1 <= grid[i][j] <= 2
	There is exactly one starting cell and one ending cell.
"""
import sys
from typing import List
import pytest


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """DFS"""
        m, n = len(grid), len(grid[0])

        start = None
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                elif grid[i][j] == 1:
                    start = (i, j)

        def dfs(i, j, c=0):
            if grid[i][j] == 2 and c == cnt+1:
                return 1
            saved = grid[i][j]
            grid[i][j] = -1
            ret = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    ret += dfs(x, y, c+1)
            grid[i][j] = saved
            return ret

        return dfs(*start)


@pytest.mark.parametrize('grid, expected', [
    ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2),
    ([[1,0,0,0],[0,0,0,0],[0,0,0,2]], 4),
    ([[0,1],[2,0]], 0),
])
def test(grid, expected):
    assert expected == Solution().uniquePathsIII(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
