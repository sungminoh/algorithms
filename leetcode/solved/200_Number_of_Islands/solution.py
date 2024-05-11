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
from typing import List
import pytest
import sys


class Solution:
    def numIslands(self, grid):
        """Dec 21, 2018 19:07
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
        """Sep 13, 2022 06:14"""
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

    def numIslands(self, grid: List[List[str]]) -> int:
        """May 05, 2024 12:04"""
        M, N = len(grid), len(grid[0])

        seen = set()
        def dfs(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N and grid[x][y]=='1' and (x, y) not in seen:
                    seen.add((x, y))
                    dfs(x, y)

        ret = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]=='1' and (i, j) not in seen:
                    dfs(i, j)
                    ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ], 1)),
    (([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ], 3)),
])
def test(args):
    assert args[-1] == Solution().numIslands(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
