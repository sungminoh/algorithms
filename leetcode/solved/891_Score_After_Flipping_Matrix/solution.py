#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:

Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:

Input: grid = [[0]]
Output: 1

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m, n <= 20
	grid[i][j] is either 0 or 1.
"""
import copy
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """TLE May 21, 2024 13:09"""
        M, N = len(grid), len(grid[0])

        def serialize(grid):
            return tuple([tuple(row) for row in grid])

        def score(grid):
            return sum(int(''.join(map(str, row)), 2) for row in grid)

        def flip(grid, r, c):
            if r is not None:
                for j in range(N):
                    grid[r][j] = abs(1-grid[r][j])
            if c is not None:
                for i in range(M):
                    grid[i][c] = abs(1-grid[i][c])

        ret = 0
        seen = set()
        def rec(grid):
            code = serialize(grid)
            if code in seen:
                return
            seen.add(code)
            nonlocal ret
            ret = max(ret, score(grid))
            for i in range(M):
                flip(grid, i, None)
                rec(grid)
                flip(grid, i, None)
            for j in range(N):
                flip(grid, None, j)
                rec(grid)
                flip(grid, None, j)
        rec(grid)

        return ret

    def matrixScore(self, grid: List[List[int]]) -> int:
        """MLE May 21, 2024 13:35"""
        M, N = len(grid), len(grid[0])
        BASE = (1<<N) - 1
        vals = tuple([int(''.join(map(str, row)), 2)for row in grid])

        def score(vals):
            return sum(vals)

        def fliped(vals, r, c):
            if r is not None:
                ret = list(vals)
                ret[r] = BASE ^ ret[r]
                ret = tuple(ret)
            if c is not None:
                flip = 1<<(N-1-c)
                ret = tuple([
                    (val-flip) if val&flip else (val+flip)
                    for val in vals
                ])
            return ret

        ret = 0
        seen = set()
        queue = deque([vals])
        while queue:
            g = queue.popleft()
            ret = max(ret, score(g))
            for i in range(M):
                _g = fliped(g, i, None)
                if _g not in seen:
                    seen.add(_g)
                    queue.append(_g)
            for j in range(N):
                _g = fliped(g, None, j)
                if _g not in seen:
                    seen.add(_g)
                    queue.append(_g)
        return ret

    def matrixScore(self, grid: List[List[int]]) -> int:
        """Jun 25, 2024 16:35"""
        M, N = len(grid), len(grid[0])
        ret = 0
        flipped = []
        for row in grid:
            if row[0] == 0:
                flipped.append(True)
            else:
                flipped.append(False)
            ret += 1<<(N-1)
        for j in range(1, N):
            count = [0, 0]
            for i in range(M):
                v = grid[i][j]
                count[v if not flipped[i] else (1-v)] += 1
            _, cnt = max(enumerate(count), key=lambda x: x[1])
            ret += cnt * (1<<(N-j-1))
        return ret


@pytest.mark.parametrize('args', [
    (([[0,0,1,1],[1,0,1,0],[1,1,0,0]], 39)),
    (([[0]], 1)),
    (([[0,1,1,1,0,0,0,0,0],[1,0,1,1,0,1,0,0,0],[1,0,0,0,0,0,0,0,1],[1,1,1,0,1,0,1,0,0],[1,1,1,1,1,0,1,1,0],[0,0,1,0,0,0,1,0,1]], 2318)),
    (([[1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1],[1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0],[1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1],[1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1],[0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1],[1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1],[1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1],[0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0],[0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0],[0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0],[1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0],[1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0],[0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1],[1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1],[1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0],[1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0]], 16112383)),
])
def test(args):
    assert args[-1] == Solution().matrixScore(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
