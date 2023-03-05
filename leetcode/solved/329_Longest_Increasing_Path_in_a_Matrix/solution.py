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
from functools import lru_cache
from typing import List
import pytest
import sys


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

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Mar 05, 2023 12:18"""
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])

        @lru_cache()
        def dfs(i, j):
            sub = 0
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i + dx, j + dy
                if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                    sub = max(sub, dfs(x, y))
            return sub + 1

        return max(dfs(i, j) for i in range(m) for j in range(n))


@pytest.mark.parametrize('args', [
    (([[9,9,4],[6,6,8],[2,1,1]], 4)),
    (([[3,4,5],[3,2,6],[2,2,1]], 4)),
    (([[1]], 1)),
    (([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]], 140)),
])
def test(args):
    assert args[-1] == Solution().longestIncreasingPath(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
