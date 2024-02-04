import itertools
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:

	m == mat.length
	n == mat[i].length
	1 <= m, n <= 100
	mat[i][j] is either 0 or 1.
"""
import pytest
import sys


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """Feb 03, 2024 18:25"""
        M, N = len(mat), len(mat[0])
        ones = list((i, j) for i in range(M) for j in range(N) if mat[i][j] == 1)
        seen_x = seen_y = 0
        x2y = {}
        y2x = {}
        for x, y in ones:
            if (1<<x) & seen_x or (1<<y) & seen_y:
                y2x.pop(x2y.pop(x, None), None)
                x2y.pop(y2x.pop(y, None), None)
            else:
                x2y[x] = y
                y2x[y] = x
            seen_x |= (1<<x)
            seen_y |= (1<<y)
        return len(x2y)


@pytest.mark.parametrize('args', [
    (([[1,0,0],[0,0,1],[1,0,0]], 1)),
    (([[1,0,0],[0,1,0],[0,0,1]], 3)),
    (([[0,0,0,1],
       [1,0,0,0],
       [0,1,1,0],
       [0,0,0,0]], 2)),
])
def test(args):
    assert args[-1] == Solution().numSpecial(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
