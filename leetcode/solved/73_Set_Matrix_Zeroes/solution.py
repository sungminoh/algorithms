#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?<Paste>
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if matrix[i][j] == 0:
                    for k, _ in enumerate(matrix[i]):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k, _ in enumerate(matrix):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


def main():
    mat = []
    row = input()
    while row:
        mat.append([int(x) for x in row.split()])
        row = input()
    for l in Solution().setZeroes(mat):
        print(l)


if __name__ == '__main__':
    main()
