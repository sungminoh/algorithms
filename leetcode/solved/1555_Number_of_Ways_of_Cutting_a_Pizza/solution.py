#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:

	1 <= rows, cols <= 50
	rows == pizza.length
	cols == pizza[i].length
	1 <= k <= 10
	pizza consists of characters 'A' and '.' only.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """Apr 23, 2023 22:27"""
        MOD = 10**9 + 7
        M, N = len(pizza), len(pizza[0])

        integral = [[0] * (N+1) for _ in range(M+1)]
        for i in range(M):
            for j in range(N):
                integral[i][j] = integral[i-1][j] \
                    + integral[i][j-1] \
                    - integral[i-1][j-1] \
                    + (1 if pizza[i][j] == 'A' else 0)

        def num_apple(x1, y1, x2, y2):
            return integral[x2][y2] \
                - integral[x2][y1-1] \
                - integral[x1-1][y2] \
                + integral[x1-1][y1-1]

        @lru_cache(None)
        def cut(x1, y1, x2, y2, k) -> int:
            if k == 1:
                return 1 if num_apple(x1, y1, x2, y2) else 0

            ret = 0
            for x in range(x1, x2):
                if num_apple(x1, y1, x, y2):
                    ret += cut(x+1, y1, x2, y2, k-1)
                    ret %= MOD
            for y in range(y1, y2):
                if num_apple(x1, y1, x2, y):
                    ret += cut(x1, y+1, x2, y2, k-1)
                    ret %= MOD
            return ret

        return cut(0, 0, M-1, N-1, k)


@pytest.mark.parametrize('args', [
    ((["A..",
       "AAA",
       "..."], 3, 3)),
    ((["A..",
       "AA.",
       "..."], 3, 1)),
    ((["A..",
       "A..",
       "..."], 1, 1)),
])
def test(args):
    print()
    assert args[-1] == Solution().ways(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
