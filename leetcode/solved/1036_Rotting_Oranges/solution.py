#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n grid where each cell can have one of three values:

	0 representing an empty cell,
	1 representing a fresh orange, or
	2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 10
	grid[i][j] is 0, 1, or 2.
"""
from collections import deque
import sys
from typing import List
import pytest


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        elapsed = [[float('inf')]*n for _ in range(m)]

        def bfs(i, j, s):
            visited = set()
            queue = deque([(s, i, j)])
            while queue:
                s, i, j = queue.popleft()
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                        visited.add((x, y))
                        elapsed[x][y] = min(elapsed[x][y], s+1)
                        queue.append((s+1, x, y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs(i, j, 0)

        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if elapsed[i][j] == float('inf'):
                        return -1
                    else:
                        ret = max(ret, elapsed[i][j])

        return ret

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        if not grid or not grid[0]:
            return 0

        fresh = 0
        queue = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        ret = 0
        while queue:
            new_queue = []
            for i, j in queue:
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        new_queue.append((x, y))
            if new_queue:
                ret += 1
            queue = new_queue

        return ret if fresh == 0 else -1


@pytest.mark.parametrize('grid, expected', [
    ([[2,1,1],[1,1,0],[0,1,1]], 4),
    ([[2,1,1],[0,1,1],[1,0,1]], -1),
    ([[0,2]], 0),
    ([[2,1,1],[1,1,1],[0,1,2]], 2)
])
def test(grid, expected):
    print()
    assert expected == Solution().orangesRotting(grid)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
