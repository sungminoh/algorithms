#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

	1 <= n <= 9
"""
import sys
import copy
from typing import List
import pytest


class Solution:
    def solveNQueens(self, n):
        """12/26/2017 03:49"""
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

    def solveNQueens(self, n: int) -> List[List[str]]:
        """06/14/2021 07:12
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        col = set()
        fdig = set()
        bdig = set()
        ret = []

        def dfs(i, backtrack):
            if i == n:
                ret.append(backtrack[:])
            for j in range(n):
                if j not in col and i+j not in bdig and i-j not in fdig:
                    col.add(j)
                    bdig.add(i+j)
                    fdig.add(i-j)
                    backtrack.append('.'*j + 'Q' + '.'*(n-j-1))
                    dfs(i+1, backtrack)
                    col.remove(j)
                    bdig.remove(i+j)
                    fdig.remove(i-j)
                    backtrack.pop()

        dfs(0, [])
        return ret

    def solveNQueens(self, n: int) -> List[List[str]]:
        """06/16/2022 15:32"""
        class Board:
            def __init__(self, n):
                self.n = n
                self.board = [['.']*n for _ in range(n)]
                self.occupied_row = set()
                self.occupied_col = set()
                self.occupied_rdiag = set()
                self.occupied_ldiag = set()

            def is_available(self, i, j):
                return i not in self.occupied_row \
                    and j not in self.occupied_col \
                    and i-j not in self.occupied_rdiag \
                    and i+j not in self.occupied_ldiag

            def put(self, i, j):
                self.occupied_row.add(i)
                self.occupied_col.add(j)
                self.occupied_rdiag.add(i-j)
                self.occupied_ldiag.add(i+j)
                self.board[i][j] = 'Q'

            def remove(self, i, j):
                self.occupied_row.remove(i)
                self.occupied_col.remove(j)
                self.occupied_rdiag.remove(i-j)
                self.occupied_ldiag.remove(i+j)
                self.board[i][j] = '.'

        def dfs(i, board):
            if i == n:
                return [[''.join(row) for row in board.board]]
            ret = []
            for j in range(n):
                if board.is_available(i, j):
                    board.put(i, j)
                    ret.extend(dfs(i+1, board))
                    board.remove(i, j)
            return ret

        return dfs(0, Board(n))


@pytest.mark.parametrize('n, expected', [
    (4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
])
def test(n, expected):
    actual = Solution().solveNQueens(n)
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
