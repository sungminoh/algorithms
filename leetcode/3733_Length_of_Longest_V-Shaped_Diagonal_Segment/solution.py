#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

	The segment starts with 1.
	The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
	The segment:

		Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
		Continues the sequence in the same diagonal direction.
		Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.

Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:

The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:

The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:

The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

Constraints:

	n == grid.length
	m == grid[i].length
	1 <= n, m <= 500
	grid[i][j] is either 0, 1 or 2.
"""
from typing import List
import pytest
import sys


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def get_next(i, j, di, dj):
            if di == 1:
                if i == M-1:
                    if dj == -1:
                        di = -1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if di == -1:
                if i == 0:
                    if dj == 1:
                        di = 1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if dj == 1:
                if j == N-1:
                    if di == 1:
                        dj = -1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            if dj == -1:
                if j == 0:
                    if di == -1:
                        dj = 1
                        i, j = i+di, j+dj
                        if 0<=i<M and 0<=j<N:
                            return i, j, di, dj
            i, j = i+di, j+dj
            if 0<=i<M and 0<=j<N:
                return i, j, di, dj
            return None, None, di, dj


        def check(i, j, di, dj):
            ret = 0
            if grid[i][j] == 1:
                ret += 1
                while True:
                    i, j, di, dj = get_next(i, j, di, dj)
                    if i is None:
                        break
                    if grid[i][j] == (2 if ret%2 == 1 else 0):
                        ret += 1
                    else:
                        break
            return ret

        ret = 0
        for i in range(M):
            for j in range(N):
                for l in [
                    check(i, j, 1, -1),
                    check(i, j, 1, 1),
                    check(i, j, -1, 1),
                    check(i, j, -1, -1),
                ]:
                    ret = max(ret, l)
        return ret


@pytest.mark.parametrize('args', [
    (([[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]], 5)),
    (([[2,2,2,2,2],
       [2,0,2,2,0],
       [2,0,1,1,0],
       [1,0,2,2,2],
       [2,0,0,2,2]], 4)),
    (([[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]], 5)),
    (([[1]], 1)),
])
def test(args):
    assert args[-1] == Solution().lenOfVDiagonal(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
