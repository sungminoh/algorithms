#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

Constraints:

	n == grid.length == grid[i].length
	1 <= n <= 30
	grid[i][j] is either '/', '\', or ' '.
"""
from typing import List
import pytest
import sys


def expand_grid(grid):
    n = len(grid)
    g = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '\\':
                g[3*i][3*j] = 1
                g[3*i+1][3*j+1] = 1
                g[3*i+2][3*j+2] = 1
            elif grid[i][j] == '/':
                g[3*i+2][3*j] = 1
                g[3*i+1][3*j+1] = 1
                g[3*i][3*j+2] = 1
    return g


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid = expand_grid(grid)
        n = len(grid)

        def dfs(i, j):
            grid[i][j] = 1
            if i > 0 and grid[i-1][j] == 0:
                dfs(i-1, j)
            if i < n-1 and grid[i+1][j] == 0:
                dfs(i+1, j)
            if j > 0 and grid[i][j-1] == 0:
                dfs(i, j-1)
            if j < n-1 and grid[i][j+1] == 0:
                dfs(i, j+1)

        cnt = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    cnt += 1
                    # print('-------------------')
                    # for l in grid:
                        # print(l)
        return cnt

    def regionsBySlashes(self, grid: List[str]) -> int:
        """Nov 03, 2024 20:50"""
        M, N = len(grid), len(grid[0])
        def expand_grid(grid):
            ret = [[0]*(3*N) for _ in range(3*M)]
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == "/":
                        ret[3*i][3*j+2] = 1
                        ret[3*i+1][3*j+1] = 1
                        ret[3*i+2][3*j] = 1
                    elif grid[i][j] == "\\":
                        ret[3*i][3*j] = 1
                        ret[3*i+1][3*j+1] = 1
                        ret[3*i+2][3*j+2] = 1
            return ret

        mat = expand_grid(grid)

        def dfs(i, j):
            mat[i][j] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<3*M and 0<=y<3*N and mat[x][y]==0:
                    dfs(x, y)

        ret = 0
        for i in range(3*M):
            for j in range(3*N):
                if mat[i][j] == 0:
                    ret += 1
                    dfs(i, j)
        return ret


@pytest.mark.parametrize('args', [
    (([" /","/ "], 2)),
    (([" /","  "], 1)),
    ((["/\\","\\/"], 5)),
    ((["\\/","/\\"], 4)),
    ((["\\/\\ "," /\\/"," \\/ ","/ / "], 3)),
])
def test(args):
    assert args[-1] == Solution().regionsBySlashes(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
