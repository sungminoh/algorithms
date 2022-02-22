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

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

	1 <= beginWord.length <= 10
	endWord.length == beginWord.length
	1 <= wordList.length <= 5000
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
    def ladderLength(self, beginWord, endWord, wordList):
        """05/07/2018 04:31"""
        try:
            i = wordList.index(endWord)
            words = [*wordList[:i], *wordList[i+1:]]
        except ValueError:
            return 0

        possibles = [set(x) for x in zip(*words, beginWord, endWord)]
        words = set([*words, endWord])
        queue = deque([(1, beginWord)])
        def gen_words(w):
            for i in range(len(w)):
                for c in possibles[i]:
                    ret = w[:i] + c + w[i+1:]
                    if ret in words:
                        yield ret

        while queue:
            d, word = queue.popleft()
            for w in gen_words(word):
                if w == endWord:
                    return d+1
                queue.append((d+1, w))
                words.remove(w)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """05/07/2018 04:50"""
        try:
            i = wordList.index(endWord)
            words = [*wordList[:i], *wordList[i+1:]]
        except ValueError:
            return 0

        possibles = [set(x) for x in zip(*words, beginWord)]
        words = set([*words, endWord])
        words.discard(beginWord)
        def gen_words(w):
            for i in range(len(w)):
                for c in possibles[i]:
                    ret = w[:i] + c + w[i+1:]
                    if ret in words:
                        yield ret
        begin_set = set([beginWord])
        end_set = set([endWord])
        d = 1
        while begin_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            new_set = set()
            for b in begin_set:
                for w in gen_words(b):
                    if w in end_set:
                        return d+1
                    new_set.add(w)
                    # words.remove(w)
            begin_set = new_set
            d += 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def encode(w, i):
            return w[:i] + '.' + w[i+1:]

        g = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                g[encode(w, i)].append(w)

        # bfs
        visited = set([beginWord])
        queue = [beginWord]
        dist = 1
        while queue:
            new_queue = []
            for w in queue:
                if w == endWord:
                    return dist
                for i in range(len(w)):
                    for nw in g[encode(w, i)]:
                        if nw not in visited:
                            visited.add(nw)
                            new_queue.append(nw)
            queue = new_queue
            dist += 1
        return 0


@pytest.mark.parametrize('beginWord, endWord, wordList, expected', [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
])
def test(beginWord, endWord, wordList, expected):
    assert expected == Solution().ladderLength(beginWord, endWord, wordList)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
