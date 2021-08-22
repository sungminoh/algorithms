#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 104
	1 <= m * n <= 104
	mat[i][j] is either 0 or 1.
	There is at least one 0 in mat.
"""
import sys
from typing import List
import pytest


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """06/04/2020 23:15"""
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

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        def get_dp(dx, dy):
            dp = [[float('inf')] * n for _ in range(m)]
            for i in (range(m) if dx < 0 else range(m-1, -1, -1)):
                for j in (range(n) if dy < 0 else range(n-1, -1, -1)):
                    v = mat[i][j]
                    if v == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[(i+dx)%m][j], dp[i][(j+dy)%n]) + 1
            return dp

        if not mat:
            return []
        if not mat[0]:
            return [[]]
        m, n = len(mat), len(mat[0])
        dps = [get_dp(-1, -1), get_dp(1, -1), get_dp(-1, 1), get_dp(1, 1)]
        return [[min(dp[i][j] for dp in dps) for j in range(n)] for i in range(m)]


@pytest.mark.parametrize('mat, expected', [
    ([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
    ([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
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
    ([[0,0,1,0,1,1,1,0,1,1],
      [1,1,1,1,0,1,1,1,1,1],
      [1,1,1,1,1,0,0,0,1,1],
      [1,0,1,0,1,1,1,0,1,1],
      [0,0,1,1,1,0,1,1,1,1],
      [1,0,1,1,1,1,1,1,1,1],
      [1,1,1,1,0,1,0,1,0,1],
      [0,1,0,0,0,1,0,0,1,1],
      [1,1,1,0,1,1,0,1,0,1],
      [1,0,1,1,1,0,1,1,1,0]],
     [[0,0,1,0,1,2,1,0,1,2],
      [1,1,2,1,0,1,1,1,2,3],
      [2,1,2,1,1,0,0,0,1,2],
      [1,0,1,0,1,1,1,0,1,2],
      [0,0,1,1,1,0,1,1,2,3],
      [1,0,1,2,1,1,1,2,1,2],
      [1,1,1,1,0,1,0,1,0,1],
      [0,1,0,0,0,1,0,0,1,2],
      [1,1,1,0,1,1,0,1,0,1],
      [1,0,1,1,1,0,1,2,1,0]]),
])
def test(mat, expected):
    print()
    print('-------------------')
    print('mat')
    for row in mat:
        print(row)
    print('actual')
    actual = Solution().updateMatrix(mat)
    for row in actual:
        print(row)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
