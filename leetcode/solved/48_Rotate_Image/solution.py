#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:

Input: matrix = [[1]]
Output: [[1]]

Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Constraints:

	matrix.length == n
	matrix[i].length == n
	1 <= n <= 20
	-1000 <= matrix[i][j] <= 1000
"""
import sys
from typing import List
import pytest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Time complexity: O(n^2)
        Space complexity: O(1) inplace
        """
        def gen_next(x, y):
            yield y, n-1-x
            yield n-1-x, n-1-y
            yield n-1-y, x


        n = len(matrix)
        if n <= 1:
            return

        for d in range(0, n//2):
            for i in range(d, n-d-1):
                tmp = matrix[d][i]
                for a, b in gen_next(d, i):
                    matrix[a][b], tmp = tmp, matrix[a][b]
                matrix[d][i] = tmp



@pytest.mark.parametrize('matrix, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
    ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
    ([[1]], [[1]]),
    ([[1,2],[3,4]], [[3,1],[4,2]]),
])
def test(matrix, expected):
    print()
    for row in matrix:
        print(row)
    Solution().rotate(matrix)
    print()
    for row in matrix:
        print(row)
    print('--------------')
    assert expected == matrix


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
