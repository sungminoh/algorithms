#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

	Players take turns placing characters into empty squares ' '.
	The first player A always places 'X' characters, while the second player B always places 'O' characters.
	'X' and 'O' characters are always placed into empty squares, never on filled ones.
	The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
	The game also ends if all squares are non-empty.
	No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.

Constraints:

	1 <= moves.length <= 9
	moves[i].length == 2
	0 <= rowi, coli <= 2
	There are no repeated elements on moves.
	moves follow the rules of tic tac toe.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        columns = defaultdict(lambda: defaultdict(int))
        rows = defaultdict(lambda: defaultdict(int))
        diagonals = defaultdict(lambda: defaultdict(int))
        for i, (x, y) in enumerate(moves):
            rows[x][i%2] += 1
            columns[y][i%2] += 1
            if x == y:
                diagonals[x-y][i%2] += 1
            if x+y == 2:
                diagonals[x+y][i%2] += 1
            if rows[x][i%2] == 3 or columns[y][i%2] == 3 or diagonals[0][i%2] == 3 or diagonals[2][i%2] == 3:
                return 'A' if i%2 == 0 else 'B'
            if i == 8:
                return 'Draw'
        return 'Pending'


@pytest.mark.parametrize('moves, expected', [
    ([[0,0],[2,0],[1,1],[2,1],[2,2]], "A"),
    ([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B"),
    ([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw"),
    ([[0,0],[1,1]], "Pending"),
    ([[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]], 'B'),
])
def test(moves, expected):
    assert expected == Solution().tictactoe(moves)


if __name__ == '__main__':
    sys.exit(pytest.main(['-v', '-s'] + sys.argv))
