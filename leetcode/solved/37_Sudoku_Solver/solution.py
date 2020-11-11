#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""
from copy import deepcopy
from itertools import product


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                board[i][j] = 0 if board[i][j] == '.' else int(board[i][j])

        s, ret = self.solve(board)
        if s:
            for i in range(9):
                for j in range(9):
                    board[i][j] = str(ret[i][j])


    def solve(self, board):
        board = deepcopy(board)
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


def possible_mat(by_row, by_col, by_block):
    ret = [[set() for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            ret[i][j].update(by_row[i].intersection(by_col[j]).intersection(by_block[block(i, j)]))
    return ret


def block(i, j):
    return 3 * (i//3) + (j//3)


def print_board(board):
    for i, r in enumerate(board):
        if i % 3 == 0:
            print('-'*11)
        s = [str(x) for x in r]
        s.insert(6, '|')
        s.insert(3, '|')
        print(''.join(s))
    print()


def main():
    # board = []
    # for i in range(9):
        # board.append([x for x in input()])
    # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    # board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    board = [[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
    print_board(board)
    Solution().solveSudoku(board)
    print('#############')
    print_board(board)
    print_board([["8","5","4","2","1","9","7","6","3"],["3","9","7","8","6","5","4","2","1"],["2","6","1","4","7","3","9","8","5"],["7","8","5","1","2","6","3","9","4"],["6","4","9","5","3","8","1","7","2"],["1","3","2","9","4","7","8","5","6"],["9","2","6","3","8","4","5","1","7"],["5","1","3","7","9","2","6","4","8"],["4","7","8","6","5","1","2","3","9"]])


if __name__ == '__main__':
    main()
