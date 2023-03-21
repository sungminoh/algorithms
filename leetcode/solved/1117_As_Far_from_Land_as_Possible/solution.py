#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 100
	grid[i][j] is 0 or 1
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """Mar 19, 2023 13:28"""
        m, n = len(grid), len(grid[0])
        dists = defaultdict(lambda: float('inf'))
        # left, top
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dists[i, j] = 0
                else:
                    dists[i, j] = min(
                        dists[i, j],
                        dists[i-1, j] + 1,
                        dists[i, j-1] + 1,
                        dists[i-1,j-1] + 2)
        # right, botton
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    dists[i, j] = 0
                else:
                    dists[i, j] = min(
                        dists[i, j],
                        dists[i+1, j] + 1,
                        dists[i, j+1] + 1,
                        dists[i+1,j+1] + 2)
        ret = max(dists[i, j] for i in range(m) for j in range(n))
        return ret if ret != float('inf') and ret != 0 else -1


@pytest.mark.parametrize('args', [
    (([[1,0,1],[0,0,0],[1,0,1]], 2)),
    (([[1,0,0],[0,0,0],[0,0,0]], 4)),
    (([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], -1)),
    (([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], -1))
])
def test(args):
    assert args[-1] == Solution().maxDistance(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
