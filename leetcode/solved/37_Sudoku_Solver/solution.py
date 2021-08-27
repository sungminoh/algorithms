#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

	Each of the digits 1-9 must occur exactly once in each row.
	Each of the digits 1-9 must occur exactly once in each column.
	Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

	board.length == 9
	board[i].length == 9
	board[i][j] is a digit or '.'.
	It is guaranteed that the input board has only one solution.
"""
from pprint import pprint
import copy
import sys
from collections import deque
from typing import List
import pytest


class Solution:
    def solveSudoku(self, board):
        """08/06/2018 00:50"""
        def solve(board):
            def possible_mat(by_row, by_col, by_block):
                ret = [[set() for _ in range(9)] for _ in range(9)]
                for i in range(9):
                    for j in range(9):
                        ret[i][j].update(by_row[i].intersection(by_col[j]).intersection(by_block[block(i, j)]))
                return ret

            def block(i, j):
                return 3 * (i//3) + (j//3)

            board = copy.deepcopy(board)
            by_row = [set(range(1, 10)) for _ in range(9)]
            by_col = [set(range(1, 10)) for _ in range(9)]
            by_block = [set(range(1, 10)) for _ in range(9)]
            blank = []
            for i in range(9):
                for j in range(9):
                    if board[i][j]:
                        by_row[i].remove(board[i][j])
                        by_col[j].remove(board[i][j])
                        by_block[block(i, j)].remove(board[i][j])
                    else:
                        blank.append((i, j))

            while blank:
                filled = []
                possibles = possible_mat(by_row, by_col, by_block)
                for i, j in blank:
                    possible = possibles[i][j]
                    if len(possible) == 1:
                        p = possible.pop()
                        if p not in by_row[i] or p not in by_col[j] or p not in by_block[block(i, j)]:
                            return False, board
                        board[i][j] = p
                        by_row[i].remove(p)
                        by_col[j].remove(p)
                        by_block[block(i, j)].remove(p)
                        filled.append((i, j))
                for x in filled:
                    blank.remove(x)
                if not filled:
                    break

            if not blank:
                return True, board

            possibles = sorted([(i, j, possibles[i][j]) for i, j in blank], key=lambda t: len(t[-1]))
            for i, j, ps in possibles:
                if board[i][j] != 0:
                    continue
                for p in ps:
                    board[i][j] = p
                    suc, ret = self.solve(board)
                    if suc:
                        return True, ret
                    board[i][j] = 0
                break

            if blank:
                return False, board
            else:
                return True, board

        # main
        for i in range(9):
            for j in range(9):
                board[i][j] = 0 if board[i][j] == '.' else int(board[i][j])

        s, ret = solve(board)
        if s:
            for i in range(9):
                for j in range(9):
                    board[i][j] = str(ret[i][j])

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        class Sudoku:
            def __init__(self, board):
                self.board = board
                self.rows = [set('123456789') for _ in range(9)]
                self.columns = [set('123456789') for _ in range(9)]
                self.blocks = [set('123456789') for _ in range(9)]

                self.todo_rows = [set() for _ in range(9)]
                self.todo_columns = [set() for _ in range(9)]
                self.todo_blocks = [set() for _ in range(9)]
                self.todo = set()

                for i in range(9):
                    for j in range(9):
                        v = self.board[i][j]
                        if v != '.':
                            self.rows[i].remove(v)
                            self.columns[j].remove(v)
                            self.blocks[3*(i//3)+(j//3)].remove(v)
                        else:
                            self.todo_rows[i].add(j)
                            self.todo_columns[j].add(i)
                            self.todo_blocks[3*(i//3)+(j//3)].add((i, j))
                            self.todo.add((i, j))

            def affected_by_mark(self, i, j, v):
                self.rows[i].remove(v)
                self.columns[j].remove(v)
                self.blocks[3*(i//3)+(j//3)].remove(v)

                self.todo_rows[i].remove(j)
                self.todo_columns[j].remove(i)
                self.todo_blocks[3*(i//3)+(j//3)].remove((i, j))
                self.todo.remove((i, j))

                self.board[i][j] = v

                affected_points = set()
                for _j in self.todo_rows[i]:
                    affected_points.add((i, _j))
                for _i in self.todo_columns[j]:
                    affected_points.add((_i, j))
                for _i, _j in self.todo_blocks[3*(i//3)+(j//3)]:
                    affected_points.add((_i, _j))
                return affected_points

            def erase(self, i, j):
                v = self.board[i][j]
                self.rows[i].add(v)
                self.columns[j].add(v)
                self.blocks[3*(i//3)+(j//3)].add(v)

                self.todo_rows[i].add(j)
                self.todo_columns[j].add(i)
                self.todo_blocks[3*(i//3)+(j//3)].add((i, j))
                self.todo.add((i, j))

            def get_possible_values(self, i, j):
                return self.rows[i] \
                    & self.columns[j] \
                    & self.blocks[3*(i//3)+(j//3)]

            def is_done(self):
                return len(self.todo) == 0

            def solve_until_deadend(self, points=None):
                if not points:
                    points = {(i, j) for i in range(9) for j in range(9) if self.board[i][j] == '.'}
                while points:
                    marked_points = set()
                    affected_points = set()
                    for i, j in points:
                        possible_values = self.get_possible_values(i, j)
                        if len(possible_values) == 0:
                            return False
                        if len(possible_values) == 1:
                            v = possible_values.pop()
                            marked_points.add((i, j))
                            affected_points.update(self.affected_by_mark(i, j, v))
                    points = affected_points - marked_points
                return True

        def dfs(sudoku, points=None):
            if not sudoku.solve_until_deadend(points):
                return False, sudoku

            if sudoku.is_done():
                return True, sudoku

            i, j = min(sudoku.todo, key=lambda ij: sudoku.get_possible_values(*ij))
            for v in sudoku.get_possible_values(i, j):
                backup = copy.deepcopy(sudoku)
                success, result = dfs(sudoku, sudoku.affected_by_mark(i, j, v))
                if success:
                    return success, result
                sudoku = backup

            return False, sudoku

        success_board = dfs(Sudoku(board))[1].board
        for i in range(9):
            for j in range(9):
                board[i][j] = success_board[i][j]
        return


def print_board(board):
    for i, r in enumerate(board):
        if i % 3 == 0:
            print('-'*11)
        s = [str(x) for x in r]
        s.insert(6, '|')
        s.insert(3, '|')
        print(''.join(s))
    print()


@pytest.mark.parametrize('board, expected', [
    ([["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]], [["5","3","4","6","7","8","9","1","2"],
                                               ["6","7","2","1","9","5","3","4","8"],
                                               ["1","9","8","3","4","2","5","6","7"],
                                               ["8","5","9","7","6","1","4","2","3"],
                                               ["4","2","6","8","5","3","7","9","1"],
                                               ["7","1","3","9","2","4","8","5","6"],
                                               ["9","6","1","5","3","7","2","8","4"],
                                               ["2","8","7","4","1","9","6","3","5"],
                                               ["3","4","5","2","8","6","1","7","9"]]),
    ([[".",".","9","7","4","8",".",".","."],
      ["7",".",".",".",".",".",".",".","."],
      [".","2",".","1",".","9",".",".","."],
      [".",".","7",".",".",".","2","4","."],
      [".","6","4",".","1",".","5","9","."],
      [".","9","8",".",".",".","3",".","."],
      [".",".",".","8",".","3",".","2","."],
      [".",".",".",".",".",".",".",".","6"],
      [".",".",".","2","7","5","9",".","."]], [["5","1","9","7","4","8","6","3","2"],
                                               ["7","8","3","6","5","2","4","1","9"],
                                               ["4","2","6","1","3","9","8","7","5"],
                                               ["3","5","7","9","8","6","2","4","1"],
                                               ["2","6","4","3","1","7","5","9","8"],
                                               ["1","9","8","5","2","4","3","6","7"],
                                               ["9","7","5","8","6","3","1","2","4"],
                                               ["8","3","2","4","9","1","7","5","6"],
                                               ["6","4","1","2","7","5","9","8","3"]]),
    ([[".",".","9","7","4","8",".",".","."],
      ["7",".",".",".",".",".",".",".","."],
      [".","2",".","1",".","9",".",".","."],
      [".",".","7",".",".",".","2","4","."],
      [".","6","4",".","1",".","5","9","."],
      [".","9","8",".",".",".","3",".","."],
      [".",".",".","8",".","3",".","2","."],
      [".",".",".",".",".",".",".",".","6"],
      [".",".",".","2","7","5","9",".","."]], [["5","1","9","7","4","8","6","3","2"],
                                               ["7","8","3","6","5","2","4","1","9"],
                                               ["4","2","6","1","3","9","8","7","5"],
                                               ["3","5","7","9","8","6","2","4","1"],
                                               ["2","6","4","3","1","7","5","9","8"],
                                               ["1","9","8","5","2","4","3","6","7"],
                                               ["9","7","5","8","6","3","1","2","4"],
                                               ["8","3","2","4","9","1","7","5","6"],
                                               ["6","4","1","2","7","5","9","8","3"]]),
])
def test(board, expected):
    print()
    Solution().solveSudoku(board)
    assert expected == board


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
