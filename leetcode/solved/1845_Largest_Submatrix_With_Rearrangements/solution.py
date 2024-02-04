from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

Example 1:

Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example 2:

Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m * n <= 105
	matrix[i][j] is either 0 or 1.
"""
import pytest
import sys


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """Feb 04, 2024 10:40"""
        ret = 0
        M, N = len(matrix), len(matrix[0])
        acc = [(0, i) for i in range(N)]
        for row in matrix:
            zeros = []
            _acc = []
            for s, i in acc:
                if row[i] == 0:
                    zeros.append((0, i))
                else:
                    _acc.append((s+1, i))
                    ret = max(ret, _acc[-1][0] * len(_acc))
            acc = _acc + zeros
        return ret


@pytest.mark.parametrize('args', [
    (([[0,0,1],[1,1,1],[1,0,1]], 4)),
    (([[1,0,1,0,1]], 3)),
    (([[1,1,0],[1,0,1]], 2)),
])
def test(args):
    assert args[-1] == Solution().largestSubmatrix(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
