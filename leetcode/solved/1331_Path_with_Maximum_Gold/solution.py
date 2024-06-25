#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

	Every time you are located in a cell you will collect all the gold in that cell.
	From your position, you can walk one step to the left, right, up, or down.
	You can't visit the same cell more than once.
	Never visit a cell with 0 gold.
	You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 15
	0 <= grid[i][j] <= 100
	There are at most 25 cells containing gold.
"""
from typing import List
import pytest
import sys


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """Jun 03, 2024 22:31"""
        M, N = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            m = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N and grid[x][y] > 0 and (x, y) not in visited:
                    visited.add((x, y))
                    m = max(m, dfs(x, y))
                    visited.discard((x, y))
            return grid[i][j] + m

        ret = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] > 0:
                    visited.add((i, j))
                    ret = max(ret, dfs(i, j))
                    visited.discard((i, j))
        return ret


@pytest.mark.parametrize('args', [
    (([[0,6,0],[5,8,7],[0,9,0]], 24)),
    (([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]], 28)),
])
def test(args):
    assert args[-1] == Solution().getMaximumGold(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
