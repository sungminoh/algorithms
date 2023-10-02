#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:

	n == grid.length == grid[i].length
	2 <= n <= 100
	grid[i][j] is either 0 or 1.
	There are exactly two islands in grid.
"""
from heapq import heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """Sep 22, 2023 18:21"""
        M, N = len(grid), len(grid[0])

        def neighbor(i, j):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        def dfs(i, j, val=1):
            grid[i][j] = val
            for x, y in neighbor(i, j):
                if grid[x][y] == 1:
                    dfs(x, y, val)

        island_id = 2
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    dfs(i, j, island_id)
                    island_id += 1

        heap = []

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    heap.append((0, (i, j)))

        dists = {}
        while heap:
            dist, (i, j) = heappop(heap)
            for x, y in neighbor(i, j):
                if grid[x][y] == 3:
                    return dist
                if dist+1 < dists.get((x, y), float('inf')):
                    dists[x, y] = dist+1
                    heappush(heap, (dist+1, (x, y)))
        return -1


@pytest.mark.parametrize('args', [
    (([[0,1],[1,0]], 1)),
    (([[0,1,0],[0,0,0],[0,0,1]], 2)),
    (([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], 1)),
])
def test(args):
    assert args[-1] == Solution().shortestBridge(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
