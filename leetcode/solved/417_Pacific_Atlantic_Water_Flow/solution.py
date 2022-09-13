#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:

	m == heights.length
	n == heights[r].length
	1 <= m, n <= 200
	0 <= heights[r][c] <= 105
"""
from functools import lru_cache
from typing import List
import pytest
import sys


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


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])

        def dfs(mat, i, j):
            mat[i][j] = True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<n and 0<=y<m and heights[x][y]>=heights[i][j] and not mat[x][y]:
                    dfs(mat, x, y)

        pacific_access = [[False]*m for _ in range(n)]
        atlantic_access = [[False]*m for _ in range(n)]
        for i in range(n):
            dfs(pacific_access, i, 0)
            dfs(atlantic_access, i, m-1)
        for j in range(m):
            dfs(pacific_access, 0, j)
            dfs(atlantic_access, n-1, j)

        return [[i, j] for i in range(n) for j in range(m)
                if pacific_access[i][j] and atlantic_access[i][j]]


@pytest.mark.parametrize('heights, expected', [
    ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
    ([[1]], [[0,0]]),
    ([[1,2,3],[8,9,4],[7,6,5]], [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]),
    ([[10,10,10],[10,1,10],[10,10,10]], [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]),
    ([[11,3,2,4,14,6,13,18,1,4,12,2,4,1,16],[5,11,18,0,15,14,6,17,2,17,19,15,12,3,14],[10,2,5,13,11,11,13,19,11,17,14,18,14,3,11],[14,2,10,7,5,11,6,11,15,11,6,11,12,3,11],[13,1,16,15,8,2,16,10,9,9,10,14,7,15,13],[17,12,4,17,16,5,0,4,10,15,15,15,14,5,18],[9,13,18,4,14,6,7,8,5,5,6,16,13,7,2],[19,9,16,19,16,6,1,11,7,2,12,10,9,18,19],[19,5,19,10,7,18,6,10,7,12,14,8,4,11,16],[13,3,18,9,16,12,1,0,1,14,2,6,1,16,6],[14,1,12,16,7,15,9,19,14,4,16,6,11,15,7],[6,15,19,13,3,2,13,7,19,11,13,16,0,16,16],[1,5,9,7,12,9,2,18,6,12,1,8,1,10,19],[10,11,10,11,3,5,12,0,0,8,15,7,5,13,19],[8,1,17,18,3,6,8,15,0,9,8,8,12,5,18],[8,3,6,12,18,15,10,10,12,19,16,7,17,17,1],[12,13,6,4,12,18,18,9,4,9,13,11,5,3,14],[8,4,12,11,2,2,10,3,11,17,14,2,17,4,7],[8,0,14,0,13,17,11,0,16,13,15,17,4,8,3],[18,15,8,11,18,3,10,18,3,3,15,9,11,15,15]], [[0,14],[1,14],[2,14],[3,14],[4,13],[4,14],[5,14],[19,0]]),
])
def test(heights, expected):
    assert sorted(expected) == sorted(Solution().pacificAtlantic(heights))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
