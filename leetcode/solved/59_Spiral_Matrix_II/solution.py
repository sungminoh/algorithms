#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

	1 <= n <= 20
"""
import sys
from typing import List
import pytest


class Solution:
    def generateMatrix(self, n):
        """04/22/2018 05:52"""
        def i2v(i, j, n):
            dist_to_side = [j, n-1-i, n-1-j, i]
            layer = min(dist_to_side)
            for s, d in enumerate(dist_to_side):
                if d == layer:
                    side = s
                    break
            outer = 4 * layer * (n - layer)
            pre = side * (n - 1 - (2 * layer))
            remain = [i, j, n-1-i, n-1-j][side] - layer + 1
            return outer + pre + remain

        return [[i2v(i, j, n) for i in range(n)] for j in range(n)]

    def generateMatrix(self, n: int) -> List[List[int]]:
        def iter_indexes(m, n):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            t, b, l, r = 0, m-1, 0, n-1
            i, j = 0, 0
            d = 0
            for _ in range(m*n):
                yield i, j
                if d == 0 and j == r:
                    d = 1
                    t += 1
                elif d == 1 and i == b:
                    d = 2
                    r -= 1
                elif d == 2 and j == l:
                    d = 3
                    b -= 1
                elif d == 3 and i == t:
                    d = 0
                    l += 1
                i, j = i + directions[d][0], j + directions[d][1]

        ret = [[0] * n for _ in range(n)]
        for x, (i, j) in enumerate(iter_indexes(n, n), 1):
            ret[i][j] = x
        return ret


@pytest.mark.parametrize('n, expected', [
    (3, [[1,2,3],[8,9,4],[7,6,5]]),
    (1, [[1]]),
])
def test(n, expected):
    assert expected == Solution().generateMatrix(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
