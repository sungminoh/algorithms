
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

    1. If a mine ('M') is revealed, then the game is over - change it to 'X'.
    2. If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    3. If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    4. Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:
    1. The range of the input matrix's height and width is [1,50].
    2. The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
    3. The input board won't be a stage when game is over (some mines have been revealed).
    4. For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""
import sys
from copy import deepcopy
from typing import List
import pytest



class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return [[]]

        n, m = len(board), len(board[0])
        i, j = click

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        def iter_neighbors(i, j):
            directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    yield x, y

        def count_adjacent_bombs(i, j):
            cnt = 0
            for x, y in iter_neighbors(i, j):
                if board[x][y] == 'M':
                    cnt += 1
            return cnt

        def dfs(i, j):
            if board[i][j] != 'E':
                return
            bombs = count_adjacent_bombs(i, j)
            if bombs > 0:
                board[i][j] = str(bombs)
            else:
                board[i][j] = 'B'
                for x, y in iter_neighbors(i, j):
                    dfs(x, y)

        dfs(i, j)
        return board


@pytest.mark.parametrize('board, click, expected', [
([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']], [3,0],
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]),
([['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']], [1,2],
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]),
])
def test(board, click, expected):
    print()
    print('--- Prev ---')
    [print(l) for l in board]
    print('--- Next ---')
    next_board = Solution().updateBoard(board, click)
    [print(l) for l in next_board]
    print('------------')
    assert expected == next_board


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
