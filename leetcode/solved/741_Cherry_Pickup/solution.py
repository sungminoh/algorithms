#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

	0 means the cell is empty, so you can pass through,
	1 means the cell contains a cherry that you can pick up and pass through, or
	-1 means the cell contains a thorn that blocks your way.

Return the maximum number of cherries you can collect by following the rules below:

	Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
	After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
	When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
	If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

Example 1:

Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0

Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 50
	grid[i][j] is -1, 0, or 1.
	grid[0][0] != -1
	grid[n - 1][n - 1] != -1
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """11/28/2022 22:37, TLE"""
        m, n = len(grid), len(grid[0])

        def dfs(i, j, d):
            if d == 0:  # going down
                if i == m-1:
                    cur = 0
                    row = grid[i][:]
                    for k in range(j, n):
                        if grid[i][k] == -1:
                            return -1
                        cur += grid[i][k]
                        grid[i][k] = 0
                    sub = dfs(i, n-1, 1)
                    ret = (cur + sub) if sub>=0 else -1
                    grid[i] = row
                    return ret
                else:
                    ret = -1
                    cur = 0
                    row = grid[i][:]
                    for k in range(j, n):
                        if grid[i][k] == -1:
                            break
                        cur += grid[i][k]
                        grid[i][k] = 0
                        sub = dfs(i+1, k, d)
                        ret = max(ret, (cur + sub) if sub>=0 else -1)
                    grid[i] = row
                    return ret
            else:  # going up
                if i == 0:
                    cur = 0
                    for k in range(j, -1, -1):
                        if grid[i][k] == -1:
                            return -1
                        cur += grid[i][k]
                    return cur
                else:
                    ret = -1
                    cur = 0
                    for k in range(j, -1, -1):
                        if grid[i][k] == -1:
                            break
                        cur += grid[i][k]
                        sub = dfs(i-1, k, d)
                        ret = max(ret, (cur + sub) if sub>=0 else -1)
                    return ret

        ret = dfs(0, 0, 0)
        return max(0, ret)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        """11/28/2022 22:5"""
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j, x, y):
            # invalid case
            if not (0<=i<m and 0<=j<n and 0<=x<m and 0<=y<n \
                    and grid[i][j]!=-1 and grid[x][y]!=-1):
                return -float('inf')
            # end case
            if i == m-1 and j == n-1:
                return grid[i][j]
            # interim case
            if (i, j) == (x, y):
                ret = grid[i][j]
            else:
                ret = grid[i][j] + grid[x][y]
            ret += max(  # four cases of moving
                dfs(i+1, j, x+1, y), dfs(i+1, j, x, y+1),
                dfs(i, j+1, x+1, y), dfs(i, j+1, x, y+1)
            )
            return ret

        return max(0, dfs(0, 0, 0, 0))


@pytest.mark.parametrize('grid, expected', [
    ([[0,1,-1],[1,0,-1],[1,1,1]], 5),
    ([[1,1,-1],
      [1,-1,1],
      [-1,1,1]], 0),
    ([[1,1,1,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,1],
      [1,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,0,0,0],
      [0,0,0,1,1,1,1]], 15),
])
def test(grid, expected):
    assert expected == Solution().cherryPickup(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
