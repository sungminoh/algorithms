#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
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

    def __maximalSquare(self, matrix: List[List[str]]) -> int:
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




if __name__ == '__main__':
    cases = [
        ['10100',
         '10110',
         '11111',
         '10010'],
        [],
        ['0'],
        [["0","0","0","0","0"],["1","0","0","0","0"],["0","0","0","0","0"],["0","0","0","0","0"]],
        [["0","0"],["0","0"]]
    ]
    expecteds = [
        4,
        0,
        0,
        1,
        0
    ]
    for mat, expected in zip(cases, expecteds):
        actual = Solution().maximalSquare(mat)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
