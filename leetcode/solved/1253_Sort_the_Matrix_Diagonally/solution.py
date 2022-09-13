#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Example 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 100
	1 <= mat[i][j] <= 100
"""
from typing import List
import pytest
import sys


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return [[]]

        n, m = len(mat), len(mat[0])

        def get_diag(i, j):
            ret = []
            while i < n and j < m:
                ret.append(mat[i][j])
                i += 1
                j += 1
            return ret

        def fill_diag(i, j, mat, values):
            k = 0
            while i < n and j < m:
                mat[i][j] = values[k]
                i += 1
                j += 1
                k += 1

        ret = [[None]*m for _ in range(n)]
        for d in range(n+m-1):
            i, j = max(0, (n-1)-d), max(0, d-(n-1))
            arr = sorted(get_diag(i, j))
            fill_diag(i, j, ret, arr)

        return ret



@pytest.mark.parametrize('mat, expected', [
    ([[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]]),
    ([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]], [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]),
])
def test(mat, expected):
    assert expected == Solution().diagonalSort(mat)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
