#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 100
	-1000 <= mat[i][j] <= 1000
	1 <= r, c <= 300
"""
import sys
import itertools
from typing import List
import pytest


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        m, n = len(mat), len(mat[0])
        if r*c != m*n:
            return mat
        flatten = list(itertools.chain(*mat))
        return [flatten[i:i+c] for i in range(0, len(flatten), c)]


@pytest.mark.parametrize('mat, r, c, expected', [
    ([[1,2],[3,4]], 1, 4, [[1,2,3,4]]),
    ([[1,2],[3,4]], 2, 4, [[1,2],[3,4]]),
])
def test(mat, r, c, expected):
    assert expected == Solution().matrixReshape(mat, r, c)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
