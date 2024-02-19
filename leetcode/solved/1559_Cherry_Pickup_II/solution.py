from functools import lru_cache
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

	Robot #1 is located at the top-left corner (0, 0), and
	Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

	From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
	When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
	When both robots stay in the same cell, only one takes the cherries.
	Both robots cannot move outside of the grid at any moment.
	Both robots should reach the bottom row in grid.

Example 1:

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

Example 2:

Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

Constraints:

	rows == grid.length
	cols == grid[i].length
	2 <= rows, cols <= 70
	0 <= grid[i][j] <= 100
"""
import pytest
import sys


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Jan 29, 2022 10:30
        Top down recursion
        Time complexity: O(m*n^2)
        Space complexity: O(m*n^2)
        """
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(r, i, j):
            if r == m:
                return 0
            ret = grid[r][i] + (grid[r][j] if i != j else 0)
            sub = 0
            for di, dj in [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]:
                ni = i+di
                nj = j+dj
                if 0<=ni<n and 0<=nj<n:
                    sub = max(sub, dp(r+1, ni, nj))
            return ret+sub

        return dp(0, 0, n-1)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Jan 29, 2022 10:39
        Bottom up dp
        Time complexity: O(m*n^2)
        Space complexity: O(n^2)
        """
        m, n = len(grid), len(grid[0])
        memo = {(-1, n): 0}
        for r in range(m):
            new_memo = {}
            for i, j in memo.keys():
                for di, dj in [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]:
                    ni = i+di
                    nj = j+dj
                    if 0<=ni<n and 0<=nj<n:
                        new_memo[ni, nj] = max(
                            new_memo.get((ni, nj), 0),
                            memo[i, j] + grid[r][ni] + (grid[r][nj] if ni != nj else 0))
            memo = new_memo

        return max(memo.values())


    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Feb 19, 2024 14:40"""
        rows, cols = len(grid), len(grid[0])
        dp = {(0, cols-1): grid[0][0] + grid[0][-1]}
        for i in range(1, rows):
            row = grid[i]
            _dp = {}
            for (l, r), s in dp.items():
                for dl in (-1, 0, 1):
                    for dr in (-1, 0, 1):
                        x, y = l+dl, r+dr
                        if 0<=x<y<cols:
                            _dp[(x, y)] = max(
                                _dp.get((x, y), 0),
                                s + row[x] + row[y])
            dp = _dp
        return max(dp.values())


@pytest.mark.parametrize('args', [
    (([[3,1,1],[2,5,1],[1,5,5],[2,1,1]], 24)),
    (([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]], 28)),
    (([[4,1,5,7,1],
       [6,0,4,6,4],
       [0,9,6,3,5]], 32)),
])
def test(args):
    assert args[-1] == Solution().cherryPickup(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
