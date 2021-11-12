#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]

Constraints:

	m == board.length
	n == board[i].length
	1 <= m, n <= 200
	board[i][j] is 'X' or 'O'.
"""
import sys
from typing import List
import pytest


class Solution:
    """05/17/2018 22:13"""
    board = None
    visited = None

    def append_if_valid(self, acc, i, j, visited):
        if 0 <= i < len(self.board)\
                and 0 <= j < len(self.board[0])\
                and (not visited or self.visited[i][j] == False)\
                and self.board[i][j] == 'O':
            acc.append((i, j))

    def neighbor(self, i, j, visited=True):
        ret = []
        self.append_if_valid(ret, i-1, j, visited)
        self.append_if_valid(ret, i+1, j, visited)
        self.append_if_valid(ret, i, j-1, visited)
        self.append_if_valid(ret, i, j+1, visited)
        return ret

    def flip_dfs(self, i, j):
        if self.board[i][j] == 'X':
            return
        self.board[i][j] = 'X'
        for x, y in self.neighbor(i, j, False):
            self.flip_dfs(x, y)

    def inner_dfs(self, i, j):
        self.visited[i][j] = True
        is_inner = (0 < i < len(self.board)-1) and (0 < j < len(self.board[0])-1)
        for x, y in self.neighbor(i, j, visited=True):
            is_inner &= self.inner_dfs(x, y)
        return is_inner

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        self.board = board
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.board[i][j] == 'O' and not self.visited[i][j]:
                    if self.inner_dfs(i, j):
                        self.flip_dfs(i, j)


class Solution:
    """05/17/2018 23:07"""
    board = None

    def init(self, board):
        self.inner = [[True] * len(board[0]) for _ in range(len(board)-2)]
        self.inner.insert(0, [False] * len(board[0]))
        self.inner.append([False] * len(board[0]))
        for i in range(len(board)):
            self.inner[i][0] = False
            self.inner[i][len(board[0])-1] = False
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]

    def append_if_valid(self, stack, i, j):
        if not (0 <= i < len(self.board) and 0 <= j < len(self.board[0]))\
                or self.board[i][j] == 'X' or self.visited[i][j]:
            return
        self.visited[i][j] = True
        stack.append((i, j))

    def dfs(self, i, j):
        if self.board[i][j] == 'X' or self.visited[i][j]:
            return
        self.visited[i][j] = True
        stack = [(i, j)]
        inner = True
        p = 0
        while p < len(stack):
            x, y = stack[p]
            inner &= self.inner[x][y]
            self.append_if_valid(stack, x-1, y)
            self.append_if_valid(stack, x+1, y)
            self.append_if_valid(stack, x, y+1)
            self.append_if_valid(stack, x, y-1)
            p += 1
        if inner:
            for x, y in stack:
                self.board[x][y] = 'X'

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board = board
        self.init(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j)


class Solution:
    def solve(self, board):
        """05/17/2018 23:20"""
        if not board:
            return
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m) or board[i][j] != 'O':
                return
            board[i][j] = '.'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'


    def solve(self, board: List[List[str]]) -> None:
        """TLE"""
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = None
            ret = False
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y] == 'O':
                        if dfs(x, y):
                            ret = True
                            break
                else:
                    ret = True
                    break
            board[i][j] = 'O'
            return ret

        def flip(i, j):
            board[i][j] = 'X'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    flip(x, y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if not dfs(i, j):
                        flip(i, j)

    def solve(self, board: List[List[str]]) -> None:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2) call stack
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            board[i][j] = 'O'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and board[x][y] is None:
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = None

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] is None:
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] is None:
                    board[i][j] = 'X'


@pytest.mark.parametrize('board, expected', [
    ([["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"]],
     [["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","O","X","X"]]),
])
def test(board, expected):
    Solution().solve(board)
    assert expected == board


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
