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
from collections import defaultdict
from typing import Dict
from typing import List
import pytest
import sys


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """06/14/2020 10:47, 10/15/2021 00:11"""
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
        """10/15/2021 00:11"""
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

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """11/08/2022 22:47
        TLE
        """
        trie = {}
        for w in words:
            t = trie
            for c in w:
                t.setdefault(c, {})
                t = t[c]
            else:
                t[None] = w  # end of the word

        m, n = len(board), len(board[0])
        def dfs(i, j, visited, trie):
            if not trie or board[i][j] not in trie or visited&(1<<(n*i+j)) != 0:
                return

            trie = trie[board[i][j]]
            visited |= (1<<(n*i+j))
            if None in trie:
                yield trie[None]

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n:
                    yield from dfs(x, y, visited, trie)

        ret = set()
        for i in range(m):
            for j in range(n):
                for w in dfs(i, j, 0, trie):
                    ret.add(w)
        return list(ret)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """"11/08/2022 23:10"""
        ws = set(words)
        prefixes = defaultdict(int)
        for w in ws:
            for i in range(len(w)):
                prefixes[w[:i]] += 1

        m, n = len(board), len(board[0])
        def dfs(i, j, visited, w):
            if prefixes.get(w, 0) == 0 or visited&(1<<(n*i+j)) != 0:
                return

            w += board[i][j]
            visited |= (1<<(n*i+j))

            if w in ws:
                ws.remove(w)
                for k in range(len(w)):
                    prefixes[w[:k]] -= 1
                yield w

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n:
                    yield from dfs(x, y, visited, w)

        ret = set()
        for i in range(m):
            for j in range(n):
                ret.update(dfs(i, j, 0, ''))
        return list(ret)


@pytest.mark.parametrize('board, words, expected', [
    ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"], ["eat","oath"]),
    ([["a","b"],["c","d"]], ["abcb"], []),
    ([["o","a","b","n"],
      ["o","t","a","e"],
      ["a","h","k","r"],
      ["a","f","l","v"]], ["oa","oaa"], ["oa","oaa"]),
    # (*json.load(open(Path(__file__).parent/'testcase.json')), ['ababababab']),
    # (*json.load(open(Path(__file__).parent/'testcase2.json')), ['aaaaaaaaon','aaaaaaaawv','aaaaaaaaad','aaaaaaaars','aaaaaaaanm','aaaaaaaagf','aaaaaaaast','aaaaaaaaaa','aaaaaaaayz','aaaaaaaabc','aaaaaaaaah','aaaaaaaaay','aaaaaaaabm','aaaaaaaaaf','aaaaaaaacb','aaaaaaaalk','aaaaaaaaae','aaaaaaaavu','aaaaaaaafg','aaaaaaaapq','aaaaaaaaih','aaaaaaaatu','aaaaaaaaji','aaaaaaaaed','aaaaaaaaef','aaaaaaaavw','aaaaaaaaau','aaaaaaaaut','aaaaaaaafe','aaaaaaaaat','aaaaaaaaav','aaaaaaaarq','aaaaaaaade','aaaaaaaaag','aaaaaaaazy','aaaaaaaaas','aaaaaaaaaq','aaaaaaaapo','aaaaaaaano','aaaaaaaaaw','aaaaaaaayx','aaaaaaaaap','aaaaaaaacd','aaaaaaaauv','aaaaaaaaak','aaaaaaaakj','aaaaaaaaai','aaaaaaaaar','aaaaaaaaaj','aaaaaaaagh','aaaaaaaats','aaaaaaaaab','aaaaaaaahi','aaaaaaaahg','aaaaaaaaal','aaaaaaaaij','aaaaaaaaop','aaaaaaaawx','aaaaaaaaao','aaaaaaaaza','aaaaaaaaan','aaaaaaaaaz','aaaaaaaasr','aaaaaaaaqp','aaaaaaaakl','aaaaaaaaac','aaaaaaaajk','aaaaaaaadc','aaaaaaaaqr']),
])
def test(board, words, expected):
    assert sorted(expected) == sorted(Solution().findWords(board, words))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
