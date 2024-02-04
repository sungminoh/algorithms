from collections import Counter
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

	Let the number of ones in the ith row be onesRowi.
	Let the number of ones in the jth column be onesColj.
	Let the number of zeros in the ith row be zerosRowi.
	Let the number of zeros in the jth column be zerosColj.
	diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

Return the difference matrix diff.

Example 1:

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2

Example 2:

Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 105
	1 <= m * n <= 105
	grid[i][j] is either 0 or 1.
"""
import pytest
import sys


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """Feb 03, 2024 18:34"""
        M, N = len(grid), len(grid[0])
        row = [[0]*M, [0]*M]
        col = [[0]*N, [0]*N]
        for i in range(M):
            for j in range(N):
                row[grid[i][j]][i] += 1
                col[grid[i][j]][j] += 1
        diff = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                diff[i][j] = row[1][i] + col[1][j] - row[0][i] - col[0][j]
        return diff


@pytest.mark.parametrize('args', [
    (([[0,1,1],[1,0,1],[0,0,1]], [[0,0,4],[0,0,4],[-2,-2,2]])),
    (([[1,1,1],[1,1,1]], [[5,5,5],[5,5,5]])),
])
def test(args):
    assert args[-1] == Solution().onesMinusZeros(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
