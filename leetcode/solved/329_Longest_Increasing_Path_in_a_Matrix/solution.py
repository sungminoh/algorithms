#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 200
	0 <= matrix[i][j] <= 231 - 1
"""
from itertools import chain
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """10/01/2020 19:52"""
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
                chain(
                    [0],
                    (dfs(_i, _j) for _i, _j in neighbors(i, j)
                     if matrix[_i][_j] > matrix[i][j])))
            return memo[i][j]

        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret = max(ret, dfs(i, j))
        return ret

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """04/29/2021 10:00
        DFS from each cell leveraging cache
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        """
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        def neighbors(i, j):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m:
                    yield x, y

        @lru_cache(None)
        def dfs(i, j):
            mx = 0
            for x, y in neighbors(i, j):
                if matrix[x][y] > matrix[i][j]:
                    mx = max(mx, dfs(x, y))
            return 1 + mx

        return max([dfs(i, j) for i in range(n) for j in range(m)])

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """06/05/2022 19:00"""
        def increasing_neighbors(i, j):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<len(matrix) and 0<=y<len(matrix[x]) and matrix[x][y]>matrix[i][j]:
                    yield x, y

        @lru_cache(None)
        def dfs(i, j):
            ret = 0
            for x, y in increasing_neighbors(i, j):
                ret = max(ret, dfs(x, y))
            return ret+1

        return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[i])))


@pytest.mark.parametrize('matrix, expected', [
    ([[9,9,4],[6,6,8],[2,1,1]], 4),
    ([[3,4,5],[3,2,6],[2,2,1]], 4),
    ([[1]], 1),
])
def test(matrix, expected):
    assert expected == Solution().longestIncreasingPath(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
