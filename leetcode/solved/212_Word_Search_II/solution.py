#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

	m == board.length
	n == board[i].length
	1 <= m, n <= 12
	board[i][j] is a lowercase English letter.
	1 <= words.length <= 3 * 104
	1 <= words[i].length <= 10
	words[i] consists of lowercase English letters.
	All the strings of words are unique.
"""
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import Set
from typing import Dict
from typing import List
import pytest


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """06/14/2020 10:47"""
        if not board or not board[0]:
            return []

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

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])

        # build trie
        infdict = lambda: defaultdict(infdict)
        trie = infdict()
        for w in words:
            d = trie
            for c in w:
                d = d[c]
            else:
                d[None] = w

        visited = set()
        def dfs(i, j, t: Dict):
            if (i, j) in visited or not t or board[i][j] not in t:
                return

            visited.add((i, j))
            t = t[board[i][j]]

            if None in t:
                ret.add(t[None])

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n:
                    dfs(x, y, t)

            visited.remove((i, j))

        ret = set()
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)
        return list(ret)


@pytest.mark.parametrize('board, words, expected', [
    ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"], ["eat","oath"]),
    ([["a","b"],["c","d"]], ["abcb"], []),
    ([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"], ["oa","oaa"]),
    (*json.load(open(Path(__file__).parent/'testcase.json')), ['ababababab']),
])
def test(board, words, expected):
    assert sorted(expected) == sorted(Solution().findWords(board, words))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
