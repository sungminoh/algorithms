#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

	Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].

		This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.

	If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
	The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

	For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:

	n == board.length == board[i].length
	2 <= n <= 20
	board[i][j] is either -1 or in the range [1, n2].
	The squares labeled 1 and n2 do not have any ladders or snakes.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """May 20, 2020 09:40"""
        nn = len(board) * len(board[0]) - 1

        def get(i):
            row, col = divmod(i, len(board[0]))
            if row % 2 != 0:
                col = len(board[0]) - 1 - col
            row = len(board) - 1 - row
            return board[row][col] - 1

        visited = set()
        queue = deque([(0, 0)])
        while queue:
            i, n = queue.popleft()
            for j in range(i + 1, i + 7):
                bj = get(j)
                if j >= nn or bj >= nn:
                    return n + 1
                if j not in visited and bj < 0:
                    visited.add(j)
                    queue.append((j, n + 1))
                if bj >= 0 and bj not in visited:
                    visited.add(bj)
                    queue.append((bj, n + 1))

        return -1


    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """Mar 11, 2023 20:37"""
        m, n = len(board), len(board[0])

        def decode(v):
            p, r = divmod(v-1, n)
            x = m-1-p
            y = r if (m-1-x)%2 == 0 else (n-1-r)
            return x, y

        visited = 1
        dist = 0
        queue = [1]
        while queue:
            _q = []
            for i in queue:
                if i == m*n:
                    return dist
                for j in range(i+1, min(i+7, m*n+1)):
                    x, y = decode(j)
                    if board[x][y] >= 0:
                        j = board[x][y]
                    if visited & 1<<(j-1):
                        continue
                    visited |= 1<<(j-1)
                    _q.append(j)
            queue = _q
            dist += 1
        return -1


@pytest.mark.parametrize('args', [
    (([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]], 4)),
    (([[-1,-1],[-1,3]], 1)),
    (([[1,1,-1],
       [1,1,1],
       [-1,1,1]], -1)),
    ([[-1,-1,30,14,15,-1],
      [23,9,-1,-1,-1,9],
      [12,5,7,24,-1,30],
      [10,-1,-1,-1,25,17],
      [32,-1,28,-1,-1,32],
      [-1,-1,23,-1,13,19]], 2),
    ([[-1,-1,-1],
      [-1,9,8],
      [-1,8,9]], 1)
])
def test(args):
    assert args[-1] == Solution().snakesAndLadders(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
