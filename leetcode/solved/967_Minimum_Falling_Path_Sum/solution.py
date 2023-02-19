#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:

	n == matrix.length == matrix[i].length
	1 <= n <= 100
	-100 <= matrix[i][j] <= 100
"""
from typing import List
import pytest
import sys


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """Feb 19, 2023 15:15"""
        m, n = len(matrix), len(matrix[0])
        s = [0]*n
        for row in matrix:
            _s = [0]*n
            for i, x in enumerate(row):
                _s[i] = x + min(
                    s[i],
                    s[i-1] if i > 0 else float('inf'),
                    s[i+1] if i < n-1 else float('inf'))
            s = _s
        return min(s)


@pytest.mark.parametrize('matrix, expected', [
    ([[2,1,3],[6,5,4],[7,8,9]], 13),
    ([[-19,57],[-40,-5]], -59),
])
def test(matrix, expected):
    assert expected == Solution().minFallingPathSum(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
