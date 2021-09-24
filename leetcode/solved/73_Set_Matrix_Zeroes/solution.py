#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

	m == matrix.length
	n == matrix[0].length
	1 <= m, n <= 200
	-231 <= matrix[i][j] <= 231 - 1

Follow up:

	A straightforward solution using O(mn) space is probably a bad idea.
	A simple improvement uses O(m + n) space, but still not the best solution.
	Could you devise a constant space solution?
"""
import sys
from typing import List
import pytest


class Solution:
    def setZeroes(self, matrix):
        """04/22/2018 06:22
        If matrix allows None
        """
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if matrix[i][j] == 0:
                    for k, _ in enumerate(matrix[i]):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k, _ in enumerate(matrix):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # find the first zero (row, column)
        fi, fj = -1, -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if fi < 0:
                        fi = i
                    else:
                        fi = min(fi, i)
                    if fj < 0:
                        fj = j
                    else:
                        fj = min(fj, j)
        if fi >= 0:
            # mark
            for i in range(fi, m):
                for j in range(fj, n):
                    if matrix[i][j] == 0:
                        matrix[fi][j] = 0
                        matrix[i][fj] = 0
            # fill zero except marker row and column
            for j in range(fj+1, n):
                if matrix[fi][j] == 0:
                    for i in range(m):
                        matrix[i][j] = 0
            for i in range(fi+1, m):
                if matrix[i][fj] == 0:
                    for j in range(n):
                        matrix[i][j] = 0
            # fill zero in marker row and column
            for j in range(n):
                matrix[fi][j] = 0
            for i in range(m):
                matrix[i][fj] = 0


@pytest.mark.parametrize('matrix, expected', [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ([[1]], [[1]]),
    ([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]], [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
])
def test(matrix, expected):
    print('------------')
    for row in matrix:
        print(row)
    print()
    Solution().setZeroes(matrix)
    for row in matrix:
        print(row)
    assert expected == matrix


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
