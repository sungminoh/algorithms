#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:

The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""
from functools import lru_cache
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import List
import pytest



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



@pytest.mark.parametrize('words, expected', [
    (["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], ["catsdogcats","dogcatsdog","ratcatdogcat"]),
    (json.load(open(Path(__file__).parent/'testcase.json')), json.load(open(Path(__file__).parent/'testcase.json'))[1:])
])
def test(words, expected):
    assert sorted(expected) == sorted(Solution().findAllConcatenatedWordsInADict(words))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
