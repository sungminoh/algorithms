#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Constraints:

	board.length == 2
	board[i].length == 3
	0 <= board[i][j] <= 5
	Each value board[i][j] is unique.
"""
import sys
import copy
from collections import deque
from typing import Iterable
from typing import List
import pytest


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def tuplize(mat):
            if isinstance(mat, Iterable):
                return tuple(tuplize(x) for x in mat)
            return mat

        def slide(board, p1, p2):
            mat = copy.deepcopy(board)
            mat[p1[0]][p1[1]], mat[p2[0]][p2[1]] = mat[p2[0]][p2[1]], mat[p1[0]][p1[1]]
            return mat

        def neighbors(board, i, j):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<len(board) and 0<=y<len(board[x]):
                    yield x, y

        def find_zero(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 0:
                        return i, j

        dest_board = [[1,2,3],[4,5,0]]
        visited = set([tuplize(board)])
        queue = [(board, find_zero(board))]
        ret = 0
        while queue:
            new_queue = []
            for b, p in queue:
                if b == dest_board:
                    return ret
                for q in neighbors(b, *p):
                    new_board = slide(b, p, q)
                    key = tuplize(new_board)
                    if key not in visited:
                        visited.add(key)
                        new_queue.append((new_board, q))
            queue = new_queue
            ret += 1
        return -1


@pytest.mark.parametrize('board, expected', [
    ([[1,2,3],[4,0,5]], 1),
    ([[1,2,3],[5,4,0]], -1),
    ([[4,1,2],[5,0,3]], 5),
])
def test(board, expected):
    assert expected == Solution().slidingPuzzle(board)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
