#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

Constraints:

	1 <= words.length <= 104
	1 <= words[i].length <= 30
	words[i] consists of only lowercase English letters.
	All the strings of words are unique.
	1 <= sum(words[i].length) <= 105
"""
from pathlib import Path
import json
from collections import defaultdict
from functools import lru_cache
from typing import List
import pytest
import sys


def infdict():
    return defaultdict(infdict)


class Trie:
    def __init__(self):
        self.d = infdict()
        self.s = set()

    def add(self, word):
        self.s.add(word)
        d = self.d
        for c in word:
            d = d[c]
        else:
            d['__end__'] = True


class Solution:
    def _findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        words.sort(key=len)

        @lru_cache(None)
        def num_components(word: str):
            d = trie.d
            ret = [-float('inf')]
            for i, c in enumerate(word):
                if c in d:
                    d = d[c]
                    if d.get('__end__') is True:
                        if i == len(word)-1:
                            ret.append(1)
                        else:
                            rest = word[i+1:]
                            if rest in trie.s or num_components(rest) > 0:
                                ret.append(2)
                                break
                else:
                    break
            return max(ret)

        ret = []
        for word in words:
            n = num_components(word)
            if n > 1:
                ret.append(word)
            trie.add(word)
        return ret

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in s and (suffix in s or dfs(suffix)):
                    return True
            return False

        return [word for word in words if dfs(word)]


    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """Mar 12, 2023 17:51 TLE"""
        @lru_cache(None)
        def dfs(word, init=True):
            if not word and not init:
                return True
            for w in words:
                if word.startswith(w) and (not init or word!=w):
                    if dfs(word[len(w):], init=False):
                        return True
            return False

        return [word for word in words if dfs(word)]

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """Mar 12, 2023 17:59"""
        dic = set(words)

        @lru_cache(None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in dic and (suffix in dic or dfs(suffix)):
                    return True
            return False

        return [word for word in words if dfs(word)]


@pytest.mark.parametrize('args', [
    ((["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], ["catsdogcats","dogcatsdog","ratcatdogcat"])),
    ((["cat","dog","catdog"], ["catdog"])),
    (json.load(open(Path(__file__).parent/'testcase.json'))),
    (json.load(open(Path(__file__).parent/'testcase2.json'))),
])
def test(args):
    assert sorted(args[-1]) == sorted(Solution().findAllConcatenatedWordsInADict(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
