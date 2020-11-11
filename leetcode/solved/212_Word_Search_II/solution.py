
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:

	All inputs are consist of lowercase letters a-z.
	The values of words are distinct.
"""
import sys
from collections import defaultdict
from typing import List
import pytest



def build_trie(words):
    trie = dict()
    for word in words:
        d = trie
        for i, c in enumerate(word):
            if c not in d:
                d[c] = dict()
            d = d[c]
        d['.'] = word
    return trie


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        trie = build_trie(words)
        m, n = len(board), len(board[0])

        def dfs(i, j, ret, visited, trie):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            if (i, j) in visited:
                return
            c = board[i][j]
            if c not in trie:
                return
            visited.add((i, j))
            if '.' in trie[c]:
                ret.add(trie[c]['.'])
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y, ret, visited, trie[c])
            visited.remove((i, j))

        ret = set()
        for i in range(m):
            for j in range(n):
                dfs(i, j, ret, set(), trie)

        return list(ret)



@pytest.mark.parametrize('board, words, expected', [
    ([['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']], ["oath","pea","eat","rain"], ["eat","oath"]),
    ([["a","a"]], ["a"], ["a"]),
    ([["a","a"]], ["aa"], ["aa"]),
    ([["a","b"],["a","a"]], ["aba","baa","bab","aaab","aaa","aaaa","aaba"], ["aaa","aaab","aaba","aba","baa"])
])
def test(board, words, expected):
    assert set(expected) == set(Solution().findWords(board, words))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
