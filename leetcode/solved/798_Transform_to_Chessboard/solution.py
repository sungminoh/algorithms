#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

Example 1:

Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.

Example 2:

Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.

Example 3:

Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.

Constraints:

	n == board.length
	n == board[i].length
	2 <= n <= 30
	board[i][j] is either 0 or 1.
"""
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])
        # A row must contain the same number of 0s and 1s or differ by one
        counter = Counter(board[0])
        if len(counter) != 2:
            return -1
        (_, c1), (_, c2) = counter.most_common(2)
        if c1 - c2 >= 2:
            return -1
        # When there are more than one row, half of rows should be the same
        #  with the first row and the others should be reverse of the first row
        if m != 1:
            counter = Counter(tuple(row) for row in board)
            # Check if there are only two types of rows
            if len(counter) != 2:
                return -1
            (k1, c1), (k2, c2) = counter.most_common(2)
            # Check if each type is reverse of the other
            if any(a == b for a, b in zip(k1, k2)):
                return -1
            # Check if the number of rows per type are the same or differ by one
            if c1 - c2 >= 2:
                return -1
        # Count the number of mismatches assuming that 0 comes first
        row_diff = sum(1 if board[0][i] != i%2 else 0 for i in range(n))
        col_diff = sum(1 if board[j][0] != j%2 else 0 for j in range(m))
        # If the number of mismatches is odd or the other way around has fewer
        #  mismatches, 1 should come first
        if row_diff%2 != 0 or (n%2 == 0 and (n-row_diff) < row_diff):
            row_diff = n-row_diff
        if col_diff%2 != 0 or (m%2 == 0 and (m-col_diff) < col_diff):
            col_diff = m-col_diff
        return (row_diff + col_diff) // 2


@pytest.mark.parametrize('board, expected', [
    ([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]], 2),
    ([[0,1],[1,0]], 0),
    ([[1,0],[1,0]], -1),
    ([[1,1,0],[0,0,1],[0,0,1]], 2),
    ([[1,0],[0,1]], 0),
    ([[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]], -1),
])
def test(board, expected):
    assert expected == Solution().movesToChessboard(board)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
