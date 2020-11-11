#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
from itertools import chain
import sys
from typing import List
import pytest



class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def neighbors(i, j):
            if i > 0:
                yield i-1, j
            if j > 0:
                yield i, j-1
            if i < len(matrix)-1:
                yield i+1, j
            if j < len(matrix[0])-1:
                yield i, j+1

        memo = [[0]*len(matrix[0]) for _ in matrix]
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            memo[i][j] = 1 + max(
                chain([0],
                      (dfs(_i, _j) for _i, _j in neighbors(i, j)
                       if matrix[_i][_j] > matrix[i][j])))
            return memo[i][j]

        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret = max(ret, dfs(i, j))
        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[9,9,4],
      [6,6,8],
      [2,1,1]], 4),
    ([[3,4,5],
      [3,2,6],
      [2,2,1]], 4),
])
def test(matrix, expected):
    assert expected == Solution().longestIncreasingPath(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
