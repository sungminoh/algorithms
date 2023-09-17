from typing import List

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
import pytest
import sys


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
        """Oct 04, 2021 11:51"""
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

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Sep 10, 2023 14:41"""
        M, N = len(matrix), len(matrix[0])

        def iter_spiral(M, N):
            for j in range(N):
                yield 0, j
            for i in range(1, M):
                yield i, N-1
            if M > 1:
                for j in range(N-2, -1, -1):
                    yield M-1, j
            if N > 1:
                for j in range(M-2, 0, -1):
                    yield j, 0
            if M-2>0 and N-2>0:
                for i, j in iter_spiral(M-2, N-2):
                    yield i+1, j+1

        return [matrix[i][j] for i, j in iter_spiral(M, N)]


@pytest.mark.parametrize('args', [
    (([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5])),
    (([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])),
    (([[1,2]], [1,2])),
])
def test(args):
    assert args[-1] == Solution().spiralOrder(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
