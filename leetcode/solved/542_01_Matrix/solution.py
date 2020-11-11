
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:

	The number of elements of the given matrix will not exceed 10,000.
	There are at least one 0 in the given matrix.
	The cells are adjacent in only four directions: up, down, left and right.
"""
import sys
from collections import deque
from typing import List
import pytest


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix
        # directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        n, m = len(matrix), len(matrix[0])
        ret = [[float('inf')] * m for _ in range(n)]
        if matrix[0][0] == 0:
            ret[0][0] = 0
        for j in range(1, m):
            ret[0][j] = 0 if matrix[0][j] == 0 else (ret[0][j-1] + 1)
        for i in range(1, n):
            ret[i][0] = 0 if matrix[i][0] == 0 else (ret[i-1][0] + 1)
        for i in range(1, n):
            for j in range(1, m):
                ret[i][j] = 0 if matrix[i][j] == 0 else min(ret[i-1][j] + 1, ret[i][j-1] + 1)
        for j in range(m-2, -1, -1):
            ret[n-1][j] = min(ret[n-1][j], ret[n-1][j+1] + 1)
        for i in range(n-2, -1, -1):
            ret[i][m-1] = min(ret[i][m-1], ret[i+1][m-1] + 1)
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                ret[i][j] = min(ret[i][j], ret[i+1][j] + 1, ret[i][j+1] + 1)
        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[0,0,0],
      [0,1,0],
      [0,0,0]],
     [[0,0,0],
      [0,1,0],
      [0,0,0]]),
    ([[0,0,0],
      [0,1,0],
      [1,1,1]],
     [[0,0,0],
      [0,1,0],
      [1,2,1]]),
    ([[0,1,0,1,1],
      [1,1,0,0,1],
      [0,0,0,1,0],
      [1,0,1,1,1],
      [1,0,0,0,1]],
     [[0,1,0,1,2],
      [1,1,0,0,1],
      [0,0,0,1,0],
      [1,0,1,1,1],
      [1,0,0,0,1]]),
])
def test(matrix, expected):
    print()
    ret = Solution().updateMatrix(matrix)
    for l in expected: print(l)
    print('------------')
    for l in ret: print(l)
    assert expected == ret


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
