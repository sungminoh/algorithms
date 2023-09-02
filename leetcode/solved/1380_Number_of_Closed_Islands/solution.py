#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:

	1 <= grid.length, grid[0].length <= 100
	0 <= grid[i][j] <=1
"""
from typing import List
import pytest
import sys


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """Aug 26, 2023 14:54"""
        m, n = len(grid), len(grid[0])

        def neighbor(i, j):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                yield i+dx, j+dy

        def dfs(i, j):
            assert grid[i][j] == 0
            grid[i][j] = 2
            ret = True
            for x, y in neighbor(i, j):
                if x<0 or x>=m or y<0 or y>=n:
                    ret &= False
                elif grid[x][y] == 0:
                    ret &= dfs(x, y)
            return ret

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]], 2)),
    (([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]], 1)),
    (([[1,1,1,1,1,1,1],
       [1,0,0,0,0,0,1],
       [1,0,1,1,1,0,1],
       [1,0,1,0,1,0,1],
       [1,0,1,1,1,0,1],
       [1,0,0,0,0,0,1],
       [1,1,1,1,1,1,1]], 2)),
    (([[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]], 4)),
])
def test(args):
    assert args[-1] == Solution().closedIsland(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
