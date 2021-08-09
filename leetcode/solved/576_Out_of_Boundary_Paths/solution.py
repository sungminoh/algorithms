#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:

	1 <= m, n <= 50
	0 <= maxMove <= 50
	0 <= startRow < m
	0 <= startColumn < n
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        """06/13/2020 01:04"""
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        @lru_cache(None)
        def _rec(i, j, k):
            if k == 0:
                return 0
            cnt = 0
            if i == 0:
                cnt += 1
            if i == m-1:
                cnt += 1
            if j == 0:
                cnt += 1
            if j == n-1:
                cnt += 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    cnt += _rec(x, y, k-1) % (1e9 + 7)
            return cnt

        return _rec(i, j, N) % (1e9 + 7)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        DP
        Time complexity: O(m*n*maxMove)
        Space complexity: O(m*n*maxMove)
        """
        mod = int(1e9+7)
        def min_move_to_out(i, j):
            return min(i+1, m-i, j+1, n-j)

        @lru_cache(None)
        def dfs(i, j, move):
            if not move:
                return 0
            cnt = 0
            if i == 0: cnt += 1
            if i == m-1: cnt += 1
            if j == 0: cnt += 1
            if j == n-1: cnt += 1
            if i-1 >= 0 and min_move_to_out(i-1, j) <= move-1:
                cnt += dfs(i-1, j, move-1) % mod
            if i+1 < m and min_move_to_out(i+1, j) <= move-1:
                cnt += dfs(i+1, j, move-1) % mod
            if j-1 >= 0 and min_move_to_out(i, j-1) <= move-1:
                cnt += dfs(i, j-1, move-1) % mod
            if j+1 < n and min_move_to_out(i, j+1) <= move-1:
                cnt += dfs(i, j+1, move-1) % mod
            return cnt % mod
        return dfs(startRow, startColumn, maxMove)


@pytest.mark.parametrize('m, n, maxMove, startRow, startColumn, expected', [
    (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12),
    (8, 50, 23, 5, 26, 914783380),
])
def test(m, n, maxMove, startRow, startColumn, expected):
    assert expected == Solution().findPaths(m, n, maxMove, startRow, startColumn)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
