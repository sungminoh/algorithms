#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 500
	grid[i][j] is either 0 or 1.
"""
from typing import List
import pytest
import sys


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """Sep 02, 2023 14:58"""
        M, N = len(grid), len(grid[0])

        def neighbor(i, j):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                yield i+dx, j+dy


        def dfs(i, j):
            if 0<=i<M and 0<=j<N:
                if grid[i][j] in (0, 2):
                    return 0
                ret = 1
                grid[i][j] = 2
                for x, y in neighbor(i, j):
                    sub = dfs(x, y)
                    if sub < 0:
                        ret = -1
                    if ret > 0:
                        ret += sub
                return ret
            else:
                return -1

        return sum(max(0, dfs(i, j)) for i in range(M) for j in range(N))



@pytest.mark.parametrize('args', [
    (([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]], 3)),
    (([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]], 0)),
    (([[0,0,1,1,1,0,1,1,1,0,1],
       [1,1,1,1,0,1,0,1,1,0,0],
       [0,1,0,1,1,0,0,0,0,1,0],
       [1,0,1,1,1,1,1,0,0,0,1],
       [0,0,1,0,1,1,0,0,1,0,0],
       [1,0,0,1,1,1,0,0,0,1,1],
       [0,1,0,1,1,0,0,0,1,0,0],
       [0,1,1,0,1,0,1,1,1,0,0],
       [1,1,0,1,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,1,0,0,1]],
      7)),
])
def test(args):
    assert args[-1] == Solution().numEnclaves(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
