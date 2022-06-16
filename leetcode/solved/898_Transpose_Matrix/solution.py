#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 1000
	1 <= m * n <= 105
	-109 <= matrix[i][j] <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        if not matrix[0]:
            return [[] for _ in range(len(matrix))]
        m, n = len(matrix), len(matrix[0])
        ret = [[None]*m for _ in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ret[j][i] = matrix[i][j]
        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
    ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]),
])
def test(matrix, expected):
    assert expected == Solution().transpose(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
