#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 10
	-100 <= matrix[i][j] <= 100
"""
import sys
from typing import List
import pytest


class Solution:
    def spiralOrder(self, matrix):
        """12/30/2017 19:59"""
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


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(m, n):
            b, t, l, r = 0, m-1, 0, n-1
            i, j = 0, 0
            di, dj = 0, 1
            while t >= b and r >= l:
                yield i, j
                if dj == 1 and j == r:
                    di, dj = 1, 0
                    b += 1
                elif di == 1 and i == t:
                    di, dj = 0, -1
                    r -= 1
                elif dj == -1 and j == l:
                    di, dj = -1, 0
                    t -= 1
                elif di == -1 and i == b:
                    di, dj = 0, 1
                    l += 1
                i += di
                j += dj

        return [matrix[i][j] for i, j in spiral(len(matrix), len(matrix[0]))]


@pytest.mark.parametrize('matrix, expected', [
([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
])
def test(matrix, expected):
    assert expected == Solution().spiralOrder(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
