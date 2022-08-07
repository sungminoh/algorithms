#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

	Integers in each row are sorted in ascending from left to right.
	Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= n, m <= 300
	-109 <= matrix[i][j] <= 109
	All the integers in each row are sorted in ascending order.
	All the integers in each column are sorted in ascending order.
	-109 <= target <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def searchMatrix(self, matrix, target):
        """08/25/2019 20:14"""
        def search(x1, x2, y1, y2):
            if x1 > x2 or y1 > y2:
                return False
            if x1 == x2 and y1 == y2:
                return matrix[x1][y1] == target
            xm = x1 + (x2 - x1 - 1) // 2
            ym = y1 + (y2 - y1 - 1) // 2
            return search(x1, xm, y1, ym) \
                or search(x1, xm, ym + 1, y2) \
                or search(xm + 1, x2, y1, ym) \
                or search(xm + 1, x2, ym + 1, y2)
        if not matrix or not matrix[0]:
            return False
        return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

    def searchMatrix(self, matrix, target):
        """08/25/2019 20:22"""
        def search(x1, x2, y1, y2):
            if x1 > x2 or y1 > y2:
                return False
            if x1 == x2 and y1 == y2:
                return matrix[x1][y1] == target
            xm = x1 + (x2 - x1) // 2
            ym = y1 + (y2 - y1) // 2
            if target == matrix[xm][ym]:
                return True
            elif target < matrix[xm][ym]:
                return search(x1, xm, y1, ym) \
                    or search(x1, xm, ym + 1, y2) \
                    or search(xm + 1, x2, y1, ym)
            else:
                return search(x1, xm, ym + 1, y2) \
                    or search(xm + 1, x2, y1, ym) \
                    or search(xm + 1, x2, ym + 1, y2)
        if not matrix or not matrix[0]:
            return False
        return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisearch(s, e, x, func):
            while s <= e:
                m = s + (e-s)//2
                if func(m, x):
                    s = m+1
                else:
                    e = m-1
            return s-1

        # find il where matrix[i][-1] < target for all i <= il
        il = bisearch(0, len(matrix)-1, target, lambda i, x: matrix[i][-1] < x)
        # find iu where matrix[i][0] <= target for all i <= iu
        iu = bisearch(0, len(matrix)-1, target, lambda i, x: matrix[i][0] <= x)
        for i in range(il+1, iu+1):
            j = bisearch(0, len(matrix[i])-1, target, lambda j, x: matrix[i][j] <= x)
            if j >= 0 and matrix[i][j] == target:
                return True
        return False


@pytest.mark.parametrize('matrix, target, expected', [
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5, True),
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20, False),
    ([[-5]], -5, True),
])
def test(matrix, target, expected):
    assert expected == Solution().searchMatrix(matrix, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
