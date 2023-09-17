from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5

Constraints:

	n == mat.length == mat[i].length
	1 <= n <= 100
	1 <= mat[i][j] <= 100
"""
import pytest
import sys


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """Sep 10, 2023 14:29"""
        N = len(mat)
        ret = 0 if N%2 == 0 else mat[N//2][N//2]
        for i in range(N//2):
            ret += mat[i][i] + mat[N-1-i][N-1-i] + mat[N-1-i][i] + mat[i][N-1-i]
        return ret


@pytest.mark.parametrize('args', [
    (([[1,2,3],
       [4,5,6],
       [7,8,9]], 25)),
    (([[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]], 8)),
    (([[5]], 5)),
])
def test(args):
    assert args[-1] == Solution().diagonalSum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
