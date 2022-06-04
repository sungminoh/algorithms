#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

	All the visited cells of the path are 0.
	All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 100
	grid[i][j] is 0 or 1
"""
import sys
from typing import List
import pytest


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """BFS"""
        if not grid or not grid[0]:
            return 0
        if grid[0][0] == 1:
            return -1

        def neighbors(x, y):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    i, j = x+dx, y+dy
                    if dx|dy != 0  and 0<=i<len(grid) and 0<=j<len(grid[0]):
                        yield i, j

        queue = [(0, 0)]
        visited = set([(0, 0)])
        dest = (len(grid)-1, len(grid[0])-1)
        dist = 1
        while queue:
            new_queue = []
            for xy in queue:
                if xy == dest:
                    return dist
                for ij in neighbors(*xy):
                    if ij not in visited and grid[ij[0]][ij[1]] == 0:
                        visited.add(ij)
                        new_queue.append(ij)
            queue = new_queue
            dist += 1
        return -1


@pytest.mark.parametrize('grid, expected', [
    ([[0,1],[1,0]], 2),
    ([[0,0,0],[1,1,0],[1,1,0]], 4),
    ([[1,0,0],[1,1,0],[1,1,0]], -1),
])
def test(grid, expected):
    assert expected == Solution().shortestPathBinaryMatrix(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
