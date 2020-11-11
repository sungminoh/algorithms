#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
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


def bisearch(arr, t):
    l, r = 0, len(arr)-1
    while l <= r:
        p = (l+r)//2
        if t < arr[p]:
            r = p-1
        elif t > arr[p]:
            l = p+1;
        else:
            return p
    return False


def main():
    mat = []
    row = input().split()
    while len(row) > 1:
        mat.append([int(x) for x in row])
        row = input().split()
    print(Solution().searchMatrix(mat, int(row[0])))


if __name__ == '__main__':
    main()
