#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:

Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 20
	0 <= matrix[i][j] <= 99

Follow up:

	What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
	What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
from typing import List
import pytest
import sys


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """11/08/2022 21:17"""
        m, n = len(matrix), len(matrix[0])
        return all(len(set(matrix[i+j][j] for j in range(min(m-i, n)))) == 1 for i in range(1, m))\
            and all(len(set(matrix[i][j+i] for i in range(min(n-j, m)))) == 1 for j in range(n))


@pytest.mark.parametrize('matrix, expected', [
    ([[1,2,3,4],[5,1,2,3],[9,5,1,2]], True),
    ([[1,2],[2,2]], False),
    ([[36,59,71,15,26,82,87],
      [56,36,59,71,15,26,82],
      [15,0,36,59,71,15,26]], False),
])
def test(matrix, expected):
    assert expected == Solution().isToeplitzMatrix(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
