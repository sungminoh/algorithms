#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n square matrix of integers grid. Return the matrix such that:

	The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
	The diagonals in the top-right triangle are sorted in non-decreasing order.

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:

The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

	[1, 8, 6] becomes [8, 6, 1].
	[9, 5] and [4] remain unchanged.

The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

	[7, 2] becomes [2, 7].
	[3] remains unchanged.

Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:

The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

Constraints:

	grid.length == grid[i].length == n
	1 <= n <= 10
	-105 <= grid[i][j] <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N, M = len(grid), len(grid[0])

        def sort_diag(i, j):
            nums = []
            while i < N and j < M:
                nums.append(grid[i][j])
                i += 1
                j += 1

            if i < j:
                nums.sort()
            else:
                nums.sort(reverse=True)

            while i>0 and j>0:
                grid[i-1][j-1] = nums.pop()
                i -= 1
                j -= 1

        sort_diag(0, 0)
        for i in range(1, N):
            sort_diag(i, 0)
        for j in range(1, M):
            sort_diag(0, j)
        return grid


@pytest.mark.parametrize('args', [
    (([[1,7,3],[9,8,2],[4,5,6]], [[8,2,3],[9,6,7],[4,5,1]])),
    (([[0,1],[1,2]], [[2,1],[1,0]])),
    (([[1]], [[1]])),

])
def test(args):
    actual = Solution().sortMatrix(*args[:-1])
    assert args[-1] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
