#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.

Example 2:

Input: grid = [[8]]
Output: 0

Example 3:

Input: grid = [[4,4],[3,3]]
Output: 0

Example 4:

Input: grid = [[4,7,8],[9,5,1],[2,3,6]]
Output: 0

Constraints:

	row == grid.length
	col == grid[i].length
	1 <= row, col <= 10
	0 <= grid[i][j] <= 15
"""
import sys
from typing import List
import pytest


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(i, j):
            return all(grid[i-2][_j] + grid[i-1][_j] + grid[i][_j] == 15
                       for _j in range(j-2, j+1))\
                and all(grid[_i][j-2] + grid[_i][j-1] + grid[_i][j] == 15
                        for _i in range(i-2, i+1))\
                and grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2] == 15\
                and grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] == 15\
                and set(range(1, 10)) == set(grid[_i][_j] for _i in range(i-2, i+1) for _j in range(j-2, j+1))

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        cnt = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                if check(i, j):
                    print(i, j)
                    cnt += 1
        return cnt

    def _numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        mat = [[(0,0,0,0,0)] * len(grid[0]) for _ in grid]
        s = set(range(1,10))
        for i in range(3):
            for j in range(3):
                s.discard(grid[i][j])
        for i, row in enumerate(grid):
            r = [0] * len(grid[0])
            for j, n in enumerate(row):
                if i >= 2 and j >= 2:
                    if j > 3:
                        if 1 <= grid[i][j-3] <= 9: s.add(grid[i][j-3])
                        if 1 <= grid[i-1][j-3] <= 9: s.add(grid[i-1][j-3])
                        if 1 <= grid[i-2][j-3] <= 9: s.add(grid[i-2][j-3])
                    s.discard(grid[i][j])
                    s.discard(grid[i-1][j])
                    s.discard(grid[i-2][j])
                    print(i, j, s)
                mat[i][j] = (mat[i][j-1][0] + n - mat[i][j-3][0],
                             mat[i-1][j][1] + n - mat[i-3][j][1],
                             mat[i-1][j-1][2] + n - mat[i-3][j-3][2],
                             grid[i][j-2] + grid[i-1][j-1] + grid[i-2][j],
                             len(s))
        cnt = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                if mat[i][j][0] == mat[i][j][1] == mat[i][j][2] == mat[i][j][3] and mat[i][j][4] == 0:
                    # print(i, j)
                    cnt += 1
        for r in mat:
            print(r)

        return cnt


@pytest.mark.parametrize('grid, expected', [
    ([[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]], 1),
    ([[8]], 0),
    ([[4,4],
      [3,3]], 0),
    ([[4,7,8],
      [9,5,1],
      [2,3,6]], 0),
    ([[5,5,5],
      [5,5,5],
      [5,5,5]], 0),
    ([[10,3,5],
      [1,6,11],
      [7,9,2]], 0),
    ([[2,6,7,8],
      [10,5,0,1],
      [3,4,8,6],
      [2,9,4,4]], 0),
    ([[2,7,6,9],
      [9,5,1,6],
      [4,3,8,8],
      [1,4,10,1]], 1),
    ([[3,2,9,2,7],
      [6,1,8,4,2],
      [7,5,3,2,7],
      [2,9,4,9,6],
      [4,3,8,2,5]], 1)
])
def test(grid, expected):
    print()
    assert expected == Solution().numMagicSquaresInside(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
