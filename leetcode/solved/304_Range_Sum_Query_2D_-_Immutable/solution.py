#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D matrix matrix, handle multiple queries of the following type:

	Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

	NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
	int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example 1:

Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 200
	-105 <= matrix[i][j] <= 105
	0 <= row1 <= row2 < m
	0 <= col1 <= col2 < n
	At most 104 calls will be made to sumRegion.
"""
import sys
from typing import List
import pytest


class NumMatrix:
    """11/06/2019 15:22"""
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.integral_mat = [0]
        elif not matrix[0]:
            self.integral_mat = [[0] for _ in range(len(matrix) + 1)]
        else:
            self.integral_mat = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
            for i, row in enumerate(matrix):
                for j, e in enumerate(row):
                    self.integral_mat[i][j] = matrix[i][j]\
                        + self.integral_mat[i][j - 1]\
                        + self.integral_mat[i - 1][j]\
                        - self.integral_mat[i - 1][j - 1]
            # for row in self.integral_mat:
                # print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.integral_mat[row2][col2]\
            - self.integral_mat[row1 - 1][col2]\
            - self.integral_mat[row2][col1 - 1]\
            + self.integral_mat[row1 - 1][col1 - 1]


class NumMatrix:
    """
    Integral sum
    Time complexity:
        init: O(n^2),
        query: O(1)
    Space complexity:
        init: O(n^2),
        query: O(1)
    """
    def __init__(self, matrix: List[List[int]]):
        self.integral = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i, row in enumerate(matrix, 1):
            for j, e in enumerate(row, 1):
                self.integral[i][j] = self.integral[i-1][j] + self.integral[i][j-1] - self.integral[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.integral[row2+1][col2+1] - self.integral[row2+1][col1] - self.integral[row1][col2+1] + self.integral[row1][col1]


@pytest.mark.parametrize('commands, args, expecteds', [
    (["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
     [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]],
     [None, 8, 11, 12]),

])
def test(commands, args, expecteds):
    obj = NumMatrix(*args[0])
    for cmd, arg, expected in zip(commands[1:], args[1:], expecteds[1:]):
        assert expected == getattr(obj, cmd)(*arg)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
