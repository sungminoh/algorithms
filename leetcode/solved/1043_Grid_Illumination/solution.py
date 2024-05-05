#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.

Example 1:

Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.

The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.

Example 2:

Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
Output: [1,1]

Example 3:

Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
Output: [1,1,0]

Constraints:

	1 <= n <= 109
	0 <= lamps.length <= 20000
	0 <= queries.length <= 20000
	lamps[i].length == 2
	0 <= rowi, coli < n
	queries[j].length == 2
	0 <= rowj, colj < n
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        """Apr 29, 2024 22:31"""
        lamps = set([tuple(x) for x in lamps])
        horizontal = defaultdict(set)
        vertical = defaultdict(set)
        left_diagonal = defaultdict(set)
        right_diagonal = defaultdict(set)
        for r, c in lamps:
            rc = (r, c)
            horizontal[r].add(rc)
            vertical[c].add(rc)
            left_diagonal[r+c].add(rc)
            right_diagonal[r-c].add(rc)

        ret = []
        for r, c in queries:
            ret.append(
                1 if (horizontal[r]
                      or vertical[c]
                      or left_diagonal[r+c]
                      or right_diagonal[r-c]) else 0)
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    x, y = r+dx, c+dy
                    xy = (x, y)
                    if 0<=x<n and 0<=y<n and (x, y) in lamps:
                        horizontal[x].discard(xy)
                        vertical[y].discard(xy)
                        left_diagonal[x+y].discard(xy)
                        right_diagonal[x-y].discard(xy)

        return ret


@pytest.mark.parametrize('args', [
    ((5, [[0,0],[4,4]], [[1,1],[1,0]], [1,0])),
    ((5, [[0,0],[4,4]], [[1,1],[1,1]], [1,1])),
    ((5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]], [1,1,0])),
])
def test(args):
    assert args[-1] == Solution().gridIllumination(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
