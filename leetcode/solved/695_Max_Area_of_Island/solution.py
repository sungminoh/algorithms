#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 50
	grid[i][j] is either 0 or 1.
"""
import sys
from typing import List
import pytest


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """08/29/2020 16:41	"""
        if not grid or not grid[0]:
            return 0

        X = len(grid)
        Y = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            ret = 1
            grid[x][y] = 0
            for dx, dy in directions:
                _x, _y = x + dx, y + dy
                if 0 <= _x < X and 0 <= _y < Y:
                    ret += dfs(_x, _y)
            return ret

        return max(dfs(x, y) for x in range(X) for y in range(Y))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """DFS
        Time complexity: O(n*m)
        Space complexity: O(n*m)
        """
        n, m = len(grid), len(grid[0])

        def neighbor(i, j):
            if i > 0:
                yield i-1, j
            if i < n-1:
                yield i+1, j
            if j > 0:
                yield i, j-1
            if j < m-1:
                yield i, j+1

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            cnt = 1
            for x, y in neighbor(i, j):
                cnt += dfs(x, y)
            return cnt

        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ret = max(ret, dfs(i, j))
        return ret


@pytest.mark.parametrize('grid, expected', [
([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
([[0,0,0,0,0,0,0,0]], 0),
])
def test(grid, expected):
    assert expected == Solution().maxAreaOfIsland(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
