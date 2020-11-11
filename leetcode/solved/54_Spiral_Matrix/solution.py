#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
54. Spiral Matrix (https://leetcode.com/problems/spiral-matrix/description/)
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        ret = []
        m = len(matrix)
        n = len(matrix[0])
        size = m*n
        i = j = 0
        while len(ret) < size:
            ret.extend(matrix[i][j:n])
            i += 1
            if i == m:
                break
            ret.extend([matrix[k][n-1] for k in range(i, m)])
            n -= 1
            if j == n:
                break
            ret.extend(matrix[m-1][j:n][::-1])
            m -= 1
            ret.extend([matrix[k][j] for k in range(i, m)][::-1])
            j += 1
        return ret


def main():
    matrix = []
    s = input().split()
    while s:
        matrix.append(s)
        s = input().split()
    for l in matrix:
        print(l)
    print(Solution().spiralOrder(matrix))


if __name__ == '__main__':
    main()
