#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

	Players take turns placing characters into empty squares (" ").
	The first player always places "X" characters, while the second player always places "O" characters.
	"X" and "O" characters are always placed into empty squares, never filled ones.
	The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
	The game also ends if all squares are non-empty.
	No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:

	board is a length-3 array of strings, where each string board[i] has length 3.
	Each board[i][j] is a character in the set {" ", "X", "O"}.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count = defaultdict(int)
        chars = []
        for l in board:
            for c in l:
                count[c] += 1
        if count['X'] < count['O'] or count['X'] > count['O']+1:
            return False
        if count['X'] == count['O']:
            for l in board:
                if l == 'XXX':
                    return False
            for i in range(3):
                if all(board[j][i] == 'X' for j in range(3)):
                    return False
            if all(board[i][i] == 'X' for i in range(3)):
                return False
            if all(board[2-i][i] == 'X' for i in range(3)):
                return False
        if count['X'] == 5 and count['O'] == 4:
            for l in board:
                if l == 'OOO':
                    return False
            for i in range(3):
                if all(board[j][i] == 'O' for j in range(3)):
                    return False
            if all(board[i][i] == 'O' for i in range(3)):
                return False
            if all(board[2-i][i] == 'O' for i in range(3)):
                return False
        return True


@pytest.mark.parametrize('board, expected', [
    (["O  ", "   ", "   "], False),
    (["XOX", " X ", "   "], False),
    (["XXX", "   ", "OOO"], False),
    (["XOX", "O O", "XOX"], True),
])
def test(board, expected):
    assert expected == Solution().validTicTacToe(board)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
