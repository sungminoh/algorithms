
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:
    1. 1 <= grid.length == grid[0].length <= 30
    2. grid[i][j] is either '/', '\', or ' '.
"""
import sys
from typing import List
import pytest


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


@pytest.mark.parametrize('grid, expected', [
    ([" /",
      "/ "], 2),
    ([" /",
      "  "], 1),
    (["\\/",
      "/\\"], 4),
    (["/\\",
      "\\/"], 5),
    (["//",
      "/ "], 3),
])
def test(grid, expected):
    print()
    assert expected == Solution().regionsBySlashes(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
