#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

Constraints:

	1 <= n <= 9
"""
import sys
import pytest


class Solution:
    def totalNQueens(self, n):
        """08/10/2018 19:00"""
        def solveNQueens(n):
            def dfs(q, d, s):
                i = len(q)
                if i == n:
                    ret.append(q[:])
                    return None;
                for j in range(n):
                    if j in q or i-j in d or i+j in s:
                        continue
                    d.add(i-j)
                    s.add(i+j)
                    q.append(j)
                    dfs(q, d, s)
                    d.remove(i-j)
                    s.remove(i+j)
                    q.pop()
            ret = []
            dfs([], set(), set())
            return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in ret]

        return len(solveNQueens(n))

    def totalNQueens(self, n: int) -> int:
        # column, forward diag, backward diag
        occupancy = (set(), set(), set())

        def is_available(i, j):
            return j not in occupancy[0] \
                and i-j not in occupancy[1] \
                and i+j not in occupancy[2]

        def occupy(i, j):
            occupancy[0].add(j)
            occupancy[1].add(i-j)
            occupancy[2].add(i+j)

        def remove(i, j):
            occupancy[0].remove(j)
            occupancy[1].remove(i-j)
            occupancy[2].remove(i+j)

        def dfs(i):
            if i == n:
                return 1
            ret = 0
            for j in range(n):
                if is_available(i, j):
                    occupy(i, j)
                    ret += dfs(i+1)
                    remove(i, j)
            return ret

        return dfs(0)


@pytest.mark.parametrize('n, expected', [
    (4, 2),
    (1, 1),
])
def test(n, expected):
    assert expected == Solution().totalNQueens(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
