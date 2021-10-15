#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

	m == board.length
	n = board[i].length
	1 <= m, n <= 6
	1 <= word.length <= 15
	board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
import sys
from typing import List
import pytest


class Solution:
    def exist(self, board, word):
        """05/01/2018 05:13"""
        untrod = [r[:] for r in board]

        def out_of_index(i, j):
            return not (0 <= i < len(board) and 0<= j < len(board[0]))

        def dfs(i, j, k):
            if out_of_index(i, j) or untrod[i][j] is None:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            untrod[i][j] = None
            is_success = dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            untrod[i][j] = board[i][j]
            return is_success

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, k):
            visited.add((i, j))
            if board[i][j] != word[k]:
                visited.remove((i, j))
                return False
            if k == len(word)-1:
                visited.remove((i, j))
                return True
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x = i+dx
                y = j+dy
                if 0<=x<m and 0<=y<n and (x, y) not in visited:
                    if dfs(x, y, k+1):
                        visited.remove((i, j))
                        return True
            visited.remove((i, j))
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


@pytest.mark.parametrize('board, word, expected', [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    ([["a"]], "a", True),
    ([["a","a"]], "aaa", False),
    ([["a","b"]], "ba", True),
])
def test(board, word, expected):
    assert expected == Solution().exist(board, word)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
