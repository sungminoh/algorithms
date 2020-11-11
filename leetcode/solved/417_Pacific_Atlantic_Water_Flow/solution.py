
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

	The order of returned grid coordinates does not matter.
	Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from typing import List
import pytest
from functools import lru_cache


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def neighbors(i, j):
            if i > 0:
                yield i - 1, j
            if i < m - 1:
                yield i + 1, j
            if j > 0:
                yield i, j - 1
            if j < n - 1:
                yield i, j + 1

        def dfs(i, j, mat):
            mat[i][j] = True
            for _i, _j in neighbors(i, j):
                if not mat[_i][_j] and matrix[_i][_j] >= matrix[i][j]:
                    dfs(_i, _j, mat)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)

        ret = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ret.append([i, j])
        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    ([[10,10,10],[10,1,10],[10,10,10]], [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]),
    ([[11,3,2,4,14,6,13,18,1,4,12,2,4,1,16],[5,11,18,0,15,14,6,17,2,17,19,15,12,3,14],[10,2,5,13,11,11,13,19,11,17,14,18,14,3,11],[14,2,10,7,5,11,6,11,15,11,6,11,12,3,11],[13,1,16,15,8,2,16,10,9,9,10,14,7,15,13],[17,12,4,17,16,5,0,4,10,15,15,15,14,5,18],[9,13,18,4,14,6,7,8,5,5,6,16,13,7,2],[19,9,16,19,16,6,1,11,7,2,12,10,9,18,19],[19,5,19,10,7,18,6,10,7,12,14,8,4,11,16],[13,3,18,9,16,12,1,0,1,14,2,6,1,16,6],[14,1,12,16,7,15,9,19,14,4,16,6,11,15,7],[6,15,19,13,3,2,13,7,19,11,13,16,0,16,16],[1,5,9,7,12,9,2,18,6,12,1,8,1,10,19],[10,11,10,11,3,5,12,0,0,8,15,7,5,13,19],[8,1,17,18,3,6,8,15,0,9,8,8,12,5,18],[8,3,6,12,18,15,10,10,12,19,16,7,17,17,1],[12,13,6,4,12,18,18,9,4,9,13,11,5,3,14],[8,4,12,11,2,2,10,3,11,17,14,2,17,4,7],[8,0,14,0,13,17,11,0,16,13,15,17,4,8,3],[18,15,8,11,18,3,10,18,3,3,15,9,11,15,15]], [[0,14],[1,14],[2,14],[3,14],[4,13],[4,14],[5,14],[19,0]]),
])
def test(matrix, expected):
    print()
    for row in matrix:
        print(row)
    assert set(tuple(x) for x in expected) == set(tuple(x) for x in Solution().pacificAtlantic(matrix))
