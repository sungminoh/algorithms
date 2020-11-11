#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
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


if __name__ == '__main__':
    cases = [
        (([[1,   4,  7, 11, 15],
           [2,   5,  8, 12, 19],
           [3,   6,  9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]], 5), True),
        (([[1,   4,  7, 11, 15],
           [2,   5,  8, 12, 19],
           [3,   6,  9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]], 20), False),
        (([[1,2,3,4,5]], 1), True),
        (([[ 1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]], 5),  True)
    ]
    for case, expected in cases:
        actual = Solution().searchMatrix(*case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
