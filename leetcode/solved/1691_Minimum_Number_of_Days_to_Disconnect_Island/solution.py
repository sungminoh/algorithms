#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

Example 1:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.

Example 2:

Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 30
	grid[i][j] is either 0 or 1.
"""
from typing import List
import pytest
import sys


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def iter_neighbor(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        def dfs(i, j, visited):
            ret = 1
            for x, y in iter_neighbor(i, j):
                if grid[x][y] == 1:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        ret += dfs(x, y, visited)
            return ret

        def count():
            ret = 0
            visited = set()
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        ret += 1
                        dfs(i, j, visited)
            return ret

        if count() != 1:
            return 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1
        return 2

    def minDays(self, grid: List[List[int]]) -> int:
        """Nov 06, 2024 15:18"""
        M, N = len(grid), len(grid[0])

        def iter_neighbor(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        lowest_reachable_time = {}
        discovery_time = {}
        def dfs(i, j, init=True):
            ret = 2
            child_cnt = 0
            for x, y in iter_neighbor(i, j):
                if grid[x][y] == 1:
                    if (x, y) not in discovery_time:
                        child_cnt += 1
                        discovery_time[(x, y)] = len(discovery_time)
                        ret = min(ret, dfs(x, y, init=False))
                        if not init and lowest_reachable_time[(x, y)] >= discovery_time[(i, j)]:
                            ret = min(ret, 1)
                        lowest_reachable_time[(i, j)] = min(lowest_reachable_time.get((i, j), M*N), lowest_reachable_time[(x, y)])
                    else:
                        lowest_reachable_time[(i, j)] = min(lowest_reachable_time.get((i, j), M*N), discovery_time[(x, y)])
            if init:
                if child_cnt == 0 or child_cnt > 1:
                    ret = min(ret, 1)
            return ret

        cnt = 0
        ret = 2
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and (i, j) not in discovery_time:
                    cnt += 1
                    discovery_time[(i, j)] = len(discovery_time)
                    ret = min(ret, dfs(i, j))
        return ret if cnt == 1 else 0


@pytest.mark.parametrize('args', [
    (([[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2)),
    (([[1,1]], 2)),
    (([[1,0,1,0]], 0)),
    (([[1,1,0,1,1],
       [1,1,1,1,1],
       [1,1,0,1,1],
       [1,1,0,1,1]], 1)),
    (([[0,0,0],[0,1,0],[0,0,0]], 1)),
    (([[0,1,1,0],
       [0,1,1,0],
       [0,0,0,0]], 2)),
])
def test(args):
    assert args[-1] == Solution().minDays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
