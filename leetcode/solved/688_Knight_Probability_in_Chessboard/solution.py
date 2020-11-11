#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:

	N will be between 1 and 25.
	K will be between 0 and 100.
	The knight always initially starts on the board.
"""
from pprint import pprint
import sys
from copy import deepcopy
import pytest


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        probs = [[0] * N for _ in range(N)]
        probs[r][c] = 1
        for _ in range(K):
            _probs = [[0] * N for _ in range(N)]
            for x in range(N):
                for y in range(N):
                    if probs[x][y] == 0:
                        continue
                    for dx, dy in directions:
                        _x, _y = x + dx, y + dy
                        if 0 <= _x < N and 0 <= _y < N:
                            _probs[_x][_y] += probs[x][y] / 8
            probs = _probs
        return sum(sum(row) for row in probs)


@pytest.mark.parametrize('N, K, r, c, expected', [
    (3,2,0,0,0.0625),
])
def test(N, K, r, c, expected):
    assert expected == Solution().knightProbability(N,K,r,c)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
