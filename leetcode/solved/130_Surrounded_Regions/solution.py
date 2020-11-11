#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board
are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the
border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected
horizontally or vertically.
"""
class Solution1:
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
    board = None
    n, m = 0, 0

    def dfs(self, i, j):
        if not (0 <= i < self.n and 0 <= j < self.m) or self.board[i][j] != 'O':
            return
        self.board[i][j] = '.'
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board = board
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            self.dfs(i, 0)
            self.dfs(i, self.m-1)
        for j in range(self.m):
            self.dfs(0, j)
            self.dfs(self.n-1, j)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == '.':
                    self.board[i][j] = 'O'


def main():
    row = input().split()
    board = []
    while row:
        board.append(row)
        row = input().split()
    Solution().solve(board)
    for row in board:
        print(row)


if __name__ == '__main__':
    main()
