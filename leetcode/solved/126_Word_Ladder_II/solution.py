#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

	Every adjacent pair of words differs by a single letter.
	Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
	sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

	1 <= beginWord.length <= 5
	endWord.length == beginWord.length
	1 <= wordList.length <= 1000
	wordList[i].length == beginWord.length
	beginWord, endWord, and wordList[i] consist of lowercase English letters.
	beginWord != endWord
	All the words in wordList are unique.
"""
import sys
from collections import deque
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        BFS
        Time complexity: O(n^2 * m) where m is the length of word or bfs tc
        Space complexity: O(n^n)
        """
        graph = defaultdict(list)
        wordList = list(set(wordList + [beginWord]))
        n = len(wordList)
        for i in range(n):
            for j in range(i+1, n):
                if len([1 for x, y in zip(wordList[i], wordList[j]) if x != y]) == 1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        visited = set()
        queue = deque([[beginWord]])
        ret = []
        while queue:
            track = queue.popleft()
            visited.add(track[-1])
            if ret and len(ret[0]) <= len(track):
                break
            for w in graph.get(track[-1], []):
                if w == endWord:
                    ret.append(track + [w])
                if w not in visited:
                    queue.append(track + [w])

        return ret


@pytest.mark.parametrize('beginWord, endWord, wordList, expected', [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]),
    ("hit", "cog", ["hot","dot","dog","lot","log"], []),
    ("a", "c", ["a","b","c"], [["a","c"]]),
    ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"], [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]])
])
def test(beginWord, endWord, wordList, expected):
    assert sorted(expected) == sorted(Solution().findLadders(beginWord, endWord, wordList))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
