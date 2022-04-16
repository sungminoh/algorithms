#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 100
	-104 <= matrix[i][j], target <= 104
"""
import sys
import operator
from typing import List
import pytest


class Solution:
    def searchMatrix(self, matrix, target):
        """04/22/2018 06:45"""
        if not matrix or not matrix[0]:
            return False
        l, r = 0, len(matrix)-1
        while l <= r:
            p = (l+r)//2
            if target < matrix[p][0]:
                r = p-1
            elif target > matrix[p][0]:
                l = p+1;
            else:
                return True
        row = matrix[r]
        l, r = 0, len(row)-1
        while l <= r:
            p = (l+r)//2
            if target < row[p]:
                r = p-1
            elif target > row[p]:
                l = p+1;
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisearch(arr, x, func=operator.lt):
            l, r = 0, len(arr)-1
            while l <= r:
                m = l + (r-l)//2
                if func(arr[m], x):
                    l = m+1
                else:
                    r = m-1
            return l

        i = bisearch(matrix, target, lambda row, x: row[0] < x)
        if i < len(matrix) and matrix[i][0] == target:
            return True
        if i == 0:
            return False
        j = bisearch(matrix[i-1], target)
        if j < 0 or j >= len(matrix[i-1]):
            return False
        return matrix[i-1][j] == target


@pytest.mark.parametrize('matrix, target, expected', [
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
    ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False),
    ([[1]], 1, True),
    ([[1,3]], 3, True),
])
def test(matrix, target, expected):
    assert expected == Solution().searchMatrix(matrix, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

