#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

	Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
	Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
	Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

	Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

Example 1:

Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].

Example 2:

Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9

Constraints:

	2 <= n <= 100
	0 <= grid[i][j] <= 1
	It is guaranteed that the snake starts at empty cells.
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """May 05, 2024 11:58"""
        M, N = len(grid), len(grid[0])

        HORIZONTAL = 1
        VERTICAL = -2

        def check(i, j, pos):
            if 0<=i<M and 0<=j<N and grid[i][j]==0:
                if pos == HORIZONTAL:
                    return 0<=j+1<N and grid[i][j+1]==0
                if pos == VERTICAL:
                    return 0<=i+1<N and grid[i+1][j]==0
            return False

        def check_rotate(i, j):
            return 0<=i<M-1 and 0<=j<N-1 \
                and grid[i][j]==0 \
                and grid[i+1][j]==0 \
                and grid[i][j+1]==0 \
                and grid[i+1][j+1]==0 \

        dp = {(0, 0, HORIZONTAL): 0}
        for i in range(M):
            for j in range(N):
                for p in {HORIZONTAL, VERTICAL}:
                    if check(i, j, p):
                        for dx, dy in ((-1, 0), (0, -1)):
                            x, y = i+dx, j+dy
                            if check(x, y, p):
                                dp[i, j, p] = min(
                                    dp.get((i, j, p), float('inf')),
                                    dp.get((x, y, p), float('inf')) + 1,
                                )
                for p in {HORIZONTAL, VERTICAL}:
                    if check(i, j, p):
                        if check_rotate(i, j):
                            dp[i, j, p] = min(
                                dp.get((i, j, p), float('inf')),
                                dp.get((i, j, ~p), float('inf')) + 1,
                            )
        ret = dp.get((M-1, N-2, HORIZONTAL), float('inf'))
        return ret if ret < float('inf') else -1


@pytest.mark.parametrize('args', [
    (([[0,0,0,0,0,1],
       [1,1,0,0,1,0],
       [0,0,0,0,1,1],
       [0,0,1,0,1,0],
       [0,1,1,0,0,0],
       [0,1,1,0,0,0]], 11)),
    (([[0,0,1,1,1,1],
       [0,0,0,0,1,1],
       [1,1,0,0,0,1],
       [1,1,1,0,0,1],
       [1,1,1,0,0,1],
       [1,1,1,0,0,0]], 9)),
    (([[0,0,0,0,0,0,0,0,0,1],
       [0,1,0,0,0,0,0,1,0,1],
       [1,0,0,1,0,0,1,0,1,0],
       [0,0,0,1,0,1,0,1,0,0],
       [0,0,0,0,1,0,0,0,0,1],
       [0,0,1,0,0,0,0,0,0,0],
       [1,0,0,1,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [1,1,0,0,0,0,0,0,0,0]], -1)),
])
def test(args):
    assert args[-1] == Solution().minimumMoves(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
