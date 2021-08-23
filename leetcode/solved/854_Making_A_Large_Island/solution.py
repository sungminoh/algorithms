#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n binary islandrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 500
	grid[i][j] is either 0 or 1.
"""
import sys
from typing import Tuple
from typing import List
import pytest


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        # island id. Id starts from 1
        island = [[0]*n for _ in range(m)]

        def gen_neighbors(i, j):
            for dx, dy in ([0, 1], [0, -1], [-1, 0], [1, 0]):
                _i, _j = i+dx, j+dy
                if 0 <= _i < m and 0 <= _j < n:
                    yield _i, _j

        # size of each island. accessed by id
        sizes = [0]
        # sum of size of all adjacest islands
        adjacent_island_sizes = [0]

        def dfs(i, j) -> Tuple[int, int]:
            """Returns the currnet size and sum of size of all adjacest
            islands"""
            if grid[i][j] == 0:
                m = 1  # flipped tile
                merged_islands = set()
                for x, y in gen_neighbors(i, j):
                    iid = island[x][y]
                    if iid not in merged_islands:
                        merged_islands.add(iid)
                        m += sizes[iid] if iid < len(sizes) else 0
                return 0, m
            else:
                # assign a new id
                island[i][j] = len(sizes)
                size = 1
                max_adjacent_island_size = 0
                for x, y in gen_neighbors(i, j):
                    if island[x][y] == 0:  # not visited
                        sub_size, adjacent_island_size = dfs(x, y)
                        size += sub_size
                        max_adjacent_island_size = max(
                            max_adjacent_island_size, adjacent_island_size)
                return size, max_adjacent_island_size

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and island[i][j] == 0:
                    size, adjacent_island_size = dfs(i, j)
                    sizes.append(size)
                    adjacent_island_sizes.append(adjacent_island_size)

        ret = max(s+a for s, a in zip(sizes, adjacent_island_sizes))
        return max(ret, 1)


@pytest.mark.parametrize('grid, expected', [
    ([[1,0],
      [0,1]], 3),
    ([[1,1],
      [1,0]], 4),
    ([[1,1],
      [1,1]], 4),
    ([[0,1,1,0,0],
      [1,0,0,1,1],
      [1,0,0,1,1],
      [1,0,0,1,1]], 9),
    ([[0,0],
      [0,0]], 1),
    ([[0,0,0,0,0,0,0],
      [0,1,1,1,1,0,0],
      [0,1,0,0,1,0,0],
      [1,0,1,0,1,0,0],
      [0,1,0,0,1,0,0],
      [0,1,0,0,1,0,0],
      [0,1,1,1,1,0,0]], 18),
])
def test(grid, expected):
    print()
    assert expected == Solution().largestIsland(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
