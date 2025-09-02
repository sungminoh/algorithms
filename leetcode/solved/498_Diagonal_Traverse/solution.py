#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 104
	1 <= m * n <= 104
	-105 <= mat[i][j] <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """May 22, 2020 22:31"""
        if not matrix or not matrix[0]:
            return []
        ret = []
        n, m = len(matrix) - 1, len(matrix[0]) - 1
        for i in range(n + m + 1):  # 0 ~ n-1 + m-1
            if i % 2 == 0:
                for x in range(max(0, i - n), min(m, i) + 1):
                    y = i - x
                    ret.append(matrix[y][x])
            else:
                for x in range(min(m, i), max(0, i - n) - 1, -1):
                    y = i - x
                    ret.append(matrix[y][x])
        return ret

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """Sep 01, 2025 12:49"""
        if not mat or not mat[0]:
            return []

        M, N = len(mat), len(mat[0])

        def next_index(i, j):
            up = (i+j)%2 == 0
            if up and j == N-1:
                return i+1, j
            if up and i == 0:
                return i, j+1
            if not up and i == M-1:
                return i, j+1
            if not up and j == 0:
                return i+1, j
            di, dj = (-1, 1) if up else (1, -1)
            return i+di, j+dj

        def gen():
            i, j = 0, 0
            for _ in range(M*N):
                yield mat[i][j]
                i, j = next_index(i, j)

        return list(gen())


@pytest.mark.parametrize('args', [
    (([[1,2,3],[4,5,6],[7,8,9]], [1,2,4,7,5,3,6,8,9])),
    (([[1,2],[3,4]], [1,2,3,4])),
    (([[6,9,7]], [6,9,7]))
])
def test(args):
    assert args[-1] == Solution().findDiagonalOrder(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
