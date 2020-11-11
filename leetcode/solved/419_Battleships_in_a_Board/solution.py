
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:
X..X
...X
...X

In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
import sys
from typing import List
import pytest


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                count += 1
        return count

    def _countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        def dfs(i, j):
            board[i][j] = 'Y'
            while i < len(board) - 1 and board[i + 1][j] == 'X':
                board[i + 1][j] = 'Y'
                i += 1
            while j < len(board[0]) - 1 and board[i][j + 1] == 'X':
                board[i][j + 1] = 'Y'
                j += 1

        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    dfs(i, j)
                    count += 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'Y':
                    board[i][j] = 'X'

        return count

@pytest.mark.parametrize('board, expected', [
    ([['X', '.', '.', 'X'],
      ['.', '.', '.', 'X'],
      ['.', '.', '.', 'X']], 2),
])
def test(board, expected):
    assert expected == Solution().countBattleships(board)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

