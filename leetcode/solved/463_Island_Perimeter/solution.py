#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

	row == grid.length
	col == grid[i].length
	1 <= row, col <= 100
	grid[i][j] is 0 or 1.
	There is exactly one island in grid.
"""
import sys
from typing import List
import pytest


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ret = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, -1]):
                        x = i+dx
                        y = j+dy
                        if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:
                            ret += 1
        return ret


@pytest.mark.parametrize('grid, expected', [
    ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16),
    ([[1]], 4),
    ([[1,0]], 4),
])
def test(grid, expected):
    assert expected == Solution().islandPerimeter(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
