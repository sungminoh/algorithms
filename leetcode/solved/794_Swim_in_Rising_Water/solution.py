#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example 1:

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Constraints:

	n == grid.length
	n == grid[i].length
	1 <= n <= 50
	0 <= grid[i][j] < n2
	Each value grid[i][j] is unique.
"""
from pathlib import Path
import json
from heapq import heappop
from heapq import heappush
from collections import deque
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        DFS, brute-force searching every path to find min elebation
        """
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        memo = {}
        memo[0,0] = 0
        visited = set()
        def dfs(i, j):
            """From (i, j) to (n-1, m-1)"""
            if i == n-1 and j == m-1:
                return grid[i][j]
            ret = float('inf')
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if not (0 <= x < n) or not (0 <= y < m) or (x, y) in visited:
                    continue
                visited.add((x, y))
                ret = min(ret, dfs(x, y))
                visited.remove((x, y))
            ret = max(ret, grid[i][j])
            memo.setdefault((i, j), ret)
            memo[i,j] = min(memo[i,j], ret)
            return ret

        return dfs(0, 0)

    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        BFS with a heap
        """
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        visited = set([(0,0)])
        heap = [(grid[0][0], 0, 0)]
        while heap:
            d, i, j = heappop(heap)
            if i == n-1 and j == m-1:
                return d
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if not (0 <= x < n) or not (0 <= y < m) or (x, y) in visited:
                    continue
                visited.add((x, y))
                heappush(heap, (max(d, grid[x][y]), x, y))
        assert False, 'Not reachable'
        return None


@pytest.mark.parametrize('grid, expected', [
    ([[0,2],[1,3]], 3),
    ([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]], 16),
    ([[35,19,17,25,4,10],
      [8,18,29,21,28,31],
      [15,5,33,2,13,3],
      [26,20,27,23,11,1],
      [6,14,24,7,12,16],
      [30,34,32,22,0,9]], 35),
    (json.load(open(Path(__file__).parent/'testcase.json')), 375),
])
def test(grid, expected):
    assert expected == Solution().swimInWater(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
