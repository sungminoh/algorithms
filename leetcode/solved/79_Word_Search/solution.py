#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
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


def get_input():
    s = input().split()
    mat = []
    while s:
        mat.append(s)
        s = input().split()
    return mat


def main():
    board = get_input()
    word = input()
    while word:
        print(Solution().exist(board, word))
        word = input()


if __name__ == '__main__':
    main()
