#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

	Any live cell with fewer than two live neighbors dies as if caused by under-population.
	Any live cell with two or three live neighbors lives on to the next generation.
	Any live cell with more than three live neighbors dies, as if by over-population.
	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

	m == board.length
	n == board[i].length
	1 <= m, n <= 25
	board[i][j] is 0 or 1.

Follow up:

	Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
	In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
import sys
from typing import Union
from typing import List
import pytest


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        11/04/2019 00:04
        Do not return anything, modify board in-place instead.

        Generic solution for arbitrary dimension
        Single integer flag to express both current and next state
        current, next -> flag
        0, 0 -> 0
        1, 1 -> 1
        0, 1 -> 2
        1, 0 -> -1
        """
        def get(mat, idx) -> Union[List, int]:
            ret = mat
            for i in idx:
                # Index out of bound
                if i >= len(ret) or i < 0:
                    return 0
                ret = ret[i]
            return ret

        def set(mat, idx, val):
            get(mat, idx[:-1])[idx[-1]] = val

        def get_alive_hyperplane_neighbors(i, board, indexes, neg=False):
            idx = indexes[i]
            indexes[i] += 1 if not neg else -1
            s = 1 if abs(get(board, indexes)) == 1 else 0
            subboard = get(board, indexes[:i + 1])
            if isinstance(subboard, list):
                s += get_alive_neighbors(subboard, indexes[i + 1:])
            indexes[i] = idx
            return s

        def get_alive_neighbors(board, indexes):
            s = 0
            for i, idx in enumerate(indexes):
                s += get_alive_hyperplane_neighbors(i, board, indexes, neg=True)
                s += get_alive_hyperplane_neighbors(i, board, indexes, neg=False)
                indexes[i] = idx
            return s

        def judge(current, num_alive_neighbors):
            if num_alive_neighbors == 3:
                return 1
            elif num_alive_neighbors < 2 or num_alive_neighbors > 3:
                return 0
            else:
                return current

        def iter_all_indexes(mat):
            indexes = []
            for i, submat in enumerate(mat):
                indexes.append(i)
                if isinstance(submat, list):
                    for sub_indexes in iter_all_indexes(submat):
                        yield indexes + sub_indexes
                else:
                    yield indexes
                indexes.pop()

        for index in iter_all_indexes(board):
            current = get(board, index)
            num_alive_neighbors = get_alive_neighbors(board, index)
            next_state = judge(current, num_alive_neighbors)
            sign = current if current == next_state else 2 if next_state > current else -1
            set(board, index, sign)

        for index in iter_all_indexes(board):
            set(board, index, 1 if get(board, index) > 0 else 0)

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        04/17/2021 16:54
        Do not return anything, modify board in-place instead.

        Set -1 if a cell was alive but dies.
        Set 2 if a cell was die but revives.
        This supports arbitrary n dimension.
        """
        def traverse(board):
            """Get all possible indexes of the board"""
            if board and not isinstance(board[0], list):
                yield from ((i, ) for i in range(len(board)))
            else:
                for i, subboard in enumerate(board):
                    for subpos in traverse(subboard):
                        yield i, *subpos

        def neighbors(board, pos):
            """Generate all neighbors"""
            def surroundings(board, pos):
                if not pos:
                    yield tuple()
                else:
                    for subpos in surroundings(board[pos[0]], pos[1:]):
                        yield pos[0], *subpos
                        if pos[0] > 0:
                            yield pos[0]-1, *subpos
                        if pos[0] < len(board)-1:
                            yield pos[0]+1, *subpos
            gen = surroundings(board, pos)
            next(gen)
            yield from gen

        def get(board, pos):
            for x in pos:
                board = board[x]
            return board

        def set(board, pos, val):
            for x in pos[:-1]:
                board = board[x]
            board[pos[-1]] = val

        for pos in traverse(board):
            cnt = sum(1 for neighbor in neighbors(board, pos) if abs(get(board, neighbor)) == 1)
            subboard = get(board, pos[:-1])
            if (cnt < 2 or cnt > 3) and subboard[pos[-1]] == 1:
                subboard[pos[-1]] *= -1
            elif cnt == 3 and subboard[pos[-1]] == 0:
                subboard[pos[-1]] = 2

        for pos in traverse(board):
            subboard = get(board, pos[:-1])
            status = subboard[pos[-1]]
            if status == 2:
                subboard[pos[-1]] = 1
            elif status == -1:
                subboard[pos[-1]] = 0


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Fill with a negative number that represents status change and update
        -1: 1 -> 1
        -2: 1 -> 0
        -3: 0 -> 0
        -4: 0 -> 1
        """
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])
        def iter_neighbor(i, j):
            for dx, dy in [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, 1), (1, 0), (1, -1)
            ]:
                _i, _j = i+dx, j+dy
                if 0 <= _i < n and 0 <= _j < m:
                    yield _i, _j

        def count_lives(i, j):
            ret = 0
            for x, y in iter_neighbor(i, j):
                if board[x][y] in {-1, -2, 1}:
                    ret += 1
            return ret

        for i in range(n):
            for j in range(m):
                cnt = count_lives(i, j)
                if cnt == 2:
                    board[i][j] = -1 if board[i][j] == 1 else -3
                elif cnt == 3:
                    board[i][j] = -1 if board[i][j] == 1 else -4
                else:
                    board[i][j] = -2 if board[i][j] == 1 else -3

        for i in range(n):
            for j in range(m):
                board[i][j] = 1 if board[i][j] in {-1, -4} else 0
        return


@pytest.mark.parametrize('board, expected', [
    ([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]),
    ([[1,1],[1,0]], [[1,1],[1,1]]),
    ([[[0],[1],[0]],
      [[0],[0],[1]],
      [[1],[1],[1]],
      [[0],[0],[0]]],
     [[[0],[0],[0]],
      [[1],[0],[1]],
      [[0],[1],[1]],
      [[0],[1],[0]]]),
])
def test(board, expected):
    Solution().gameOfLife(board)
    assert expected == board


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
