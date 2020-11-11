#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
from typing import List, Union


class Solution:
    """
    Single integer flag to express both current and next state
    current, next -> flag
    0, 0 -> 0
    1, 1 -> 1
    0, 1 -> 2
    1, 0 -> -1
    """
    def get(self, mat, idx) -> Union[List, int]:
        ret = mat
        for i in idx:
            # Index out of bound
            if i >= len(ret) or i < 0:
                return 0
            ret = ret[i]
        return ret

    def set(self, mat, idx, val):
        self.get(mat, idx[:-1])[idx[-1]] = val

    def get_alive_hyperplane_neighbors(self, i, board, indexes, neg=False):
        idx = indexes[i]
        indexes[i] += 1 if not neg else -1
        s = 1 if abs(self.get(board, indexes)) == 1 else 0
        subboard = self.get(board, indexes[:i + 1])
        if isinstance(subboard, list):
            s += self.get_alive_neighbors(subboard, indexes[i + 1:])
        indexes[i] = idx
        return s

    def get_alive_neighbors(self, board, indexes):
        s = 0
        for i, idx in enumerate(indexes):
            s += self.get_alive_hyperplane_neighbors(i, board, indexes, neg=True)
            s += self.get_alive_hyperplane_neighbors(i, board, indexes, neg=False)
            indexes[i] = idx
        return s

    def judge(self, current, num_alive_neighbors):
        if num_alive_neighbors == 3:
            return 1
        elif num_alive_neighbors < 2 or num_alive_neighbors > 3:
            return 0
        else:
            return current

    def iter_all_indexes(self, mat):
        indexes = []
        for i, submat in enumerate(mat):
            indexes.append(i)
            if isinstance(submat, list):
                for sub_indexes in self.iter_all_indexes(submat):
                    yield indexes + sub_indexes
            else:
                yield indexes
            indexes.pop()

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for index in self.iter_all_indexes(board):
            current = self.get(board, index)
            num_alive_neighbors = self.get_alive_neighbors(board, index)
            next_state = self.judge(current, num_alive_neighbors)
            sign = current if current == next_state else 2 if next_state > current else -1
            self.set(board, index, sign)

        for index in self.iter_all_indexes(board):
            self.set(board, index, 1 if self.get(board, index) > 0 else 0)


if __name__ == '__main__':
    cases = [
        ([[0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]],
         [[0,0,0],
          [1,0,1],
          [0,1,1],
          [0,1,0]]),
        ([[[0],[1],[0]],
          [[0],[0],[1]],
          [[1],[1],[1]],
          [[0],[0],[0]]],
         [[[0],[0],[0]],
          [[1],[0],[1]],
          [[0],[1],[1]],
          [[0],[1],[0]]]),
    ]
    for case, expected in cases:
        Solution().gameOfLife(case)
        print(f'{expected == case}\texpected: {expected}\tcase: {case}')
