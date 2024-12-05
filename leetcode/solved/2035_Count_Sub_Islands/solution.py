#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

Constraints:

	m == grid1.length == grid2.length
	n == grid1[i].length == grid2[i].length
	1 <= m, n <= 500
	grid1[i][j] and grid2[i][j] are either 0 or 1.
"""
from typing import List
import pytest
import sys


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """Dec 05, 2024 12:54"""
        M, N = len(grid1), len(grid1[0])

        def neighbor(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0<=x<M and 0<=y<N:
                    yield x, y

        visited = set()
        def dfs(i, j):
            ret = grid1[i][j] == 1
            for x, y in neighbor(i, j):
                if grid2[x][y] == 1 and (x, y) not in visited:
                    visited.add((x, y))
                    ret &= dfs(x, y)
            return ret

        ret = 0
        for i in range(M):
            for j in range(N):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    if dfs(i, j):
                        ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]], 3)),
    (([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]], 2)),
])
def test(args):
    assert args[-1] == Solution().countSubIslands(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
