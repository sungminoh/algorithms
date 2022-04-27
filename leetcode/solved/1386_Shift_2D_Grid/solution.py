#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

	Element at grid[i][j] moves to grid[i][j + 1].
	Element at grid[i][n - 1] moves to grid[i + 1][0].
	Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:

	m == grid.length
	n == grid[i].length
	1 <= m <= 50
	1 <= n <= 50
	-1000 <= grid[i][j] <= 1000
	0 <= k <= 100
"""
import sys
from typing import List
import pytest


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        In-place
        """
        if not grid or not grid[0] or k == 0:
            return grid

        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(b, a % b)

        def next_index(i, j, k):
            j += k
            x, j = divmod(j, n)
            i += x
            _, i = divmod(i, m)
            return i, j

        def iter_indexes(i, j, k):
            _i, _j = next_index(i, j, k)
            while (_i, _j) != (i, j):
                yield _i, _j
                _i, _j = next_index(_i, _j, k)
            yield _i, _j

        m, n = len(grid), len(grid[0])
        i, j = 0, 0
        for _ in range(gcd(m*n, k)):
            tmp = grid[i][j]
            for _i, _j in iter_indexes(i, j, k):
                tmp, grid[_i][_j] = grid[_i][_j], tmp
            i, j = next_index(i, j, 1)
        return grid


@pytest.mark.parametrize('grid, k, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], 1, [[9,1,2],[3,4,5],[6,7,8]]),
    ([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4, [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]),
    ([[1,2,3],[4,5,6],[7,8,9]], 9, [[1,2,3],[4,5,6],[7,8,9]]),
])
def test(grid, k, expected):
    assert expected == Solution().shiftGrid(grid, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
