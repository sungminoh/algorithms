#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:

	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 300
	matrix[i][j] is '0' or '1'.
"""
import sys
from collections import deque
from typing import List
import pytest


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """05/12/2019 16:31"""
        if not matrix:
            return 0

        matrix = [[int(x) for x in row] for row in matrix]
        horizental = []
        for row in matrix:
            hor = []
            n = 0
            for e in row:
                n = (n + 1) if e else 0
                hor.append(n)
            horizental.append(hor)

        vertical = []
        for c in range(len(matrix[0])):
            ver = []
            n = 0
            for row in matrix:
                n = (n + 1) if row[c] else 0
                ver.append(n)
            vertical.append(ver)

        prevs = matrix[0]
        m = max(prevs)
        for i in range(1, len(matrix)):
            curr = [matrix[i][0]]
            for j in range(1, len(matrix[i])):
                curr.append(min(horizental[i][j], vertical[j][i], prevs[j - 1] + 1))
            prevs = curr
            m = max(m, *curr)
        return m ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """05/12/2019 16:41"""
        if not matrix:
            return 0
        prevs = [int(x) for x in matrix[0]]
        m = max(prevs)
        for i in range(1, len(matrix)):
            curr = [int(matrix[i][0])]
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == '1':
                    curr.append(min(curr[-1], prevs[j], prevs[j - 1]) + 1)
                else:
                    curr.append(0)
            m = max(m, *curr)
            prevs = curr
        return m ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def max_square(arr):
            ret = 0
            stack = [-1]
            for i, n in enumerate(arr):
                while stack[-1] >= 0 and arr[stack[-1]] >= n:
                    h = arr[stack.pop()]
                    w = i-1 - stack[-1]
                    ret = max(ret, min(w, h)**2)
                stack.append(i)

            while stack[-1] >= 0:
                j = stack.pop()
                w = len(arr)-1-stack[-1]
                h = arr[j]
                ret = max(ret, min(w, h)**2)

            return ret

        acc = [0]*len(matrix[0])
        ret = 0
        for row in matrix:
            for i, v in enumerate(row):
                if v == '0':
                    acc[i] = 0
                else:
                    acc[i] += 1
            ret = max(ret, max_square(acc))

        return ret


@pytest.mark.parametrize('matrix, expected', [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
    ([["0","1"],["1","0"]], 1),
    ([["0"]], 0),
    ([["1","1"],["1","1"]], 4),
    ([["0","1"],["0","1"]], 1),
    ([["0","0","1","0"],
      ["1","1","1","1"],
      ["1","1","1","1"],
      ["1","1","1","0"],
      ["1","1","0","0"],
      ["1","1","1","1"],
      ["1","1","1","0"]], 9)
])
def test(matrix, expected):
    assert expected == Solution().maximalSquare(matrix)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
