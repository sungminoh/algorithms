#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 300
	grid[i][j] is '0' or '1'.
"""
import sys
from typing import List
import pytest


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        def travel(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])\
                    or visited[i][j] or grid[i][j] != '1':
                return False
            visited[i][j] = True
            travel(i - 1, j)
            travel(i + 1, j)
            travel(i, j - 1)
            travel(i, j + 1)
            return True

        ret = 0
        visited = [[None] * len(grid[0]) for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if travel(i, j):
                    ret += 1
        return ret

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        VISITED_MARKER = '2'
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] != '1':
                return 0
            ret = 1
            grid[i][j] = VISITED_MARKER  # mark visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m:
                    ret += dfs(x, y)
            return ret
        return sum(1 if dfs(i, j)>0 else 0 for i in range(n) for j in range(m))


@pytest.mark.parametrize('grid, expected', [
    ([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ], 1),
    ([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ], 3),
])
def test(grid, expected):
    assert expected == Solution().numIslands(grid)

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
