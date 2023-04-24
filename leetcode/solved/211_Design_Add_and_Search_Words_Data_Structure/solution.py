#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

	WordDictionary() Initializes the object.
	void addWord(word) Adds word to the data structure, it can be matched later.
	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

	1 <= word.length <= 25
	word in addWord consists of lowercase English letters.
	word in search consist of '.' or lowercase English letters.
	There will be at most 2 dots in word for search queries.
	At most 104 calls will be made to addWord and search.
"""
from collections import defaultdict
import pytest
import sys


def infdict():
    return defaultdict(infdict)


class WordDictionary:
    """04/28/2019 23:24"""
    def __init__(self):
        self.trie = infdict()

    def addWord(self, word: str) -> None:
        m = self.trie
        for c, n in zip(word[:-1], word[1:]):
            m[c][n]
            m = m[c]
        m[word[-1]][None]

    def search(self, word: str) -> bool:
        return self.search_from(self.trie, word)

    @classmethod
    def search_from(cls, m, word):
        if m and word:
            for c in word:
                if c == '.':
                    return any(cls.search_from(m[k], word[1:]) for k in m.keys())
                else:
                    return cls.search_from(m[c], word[1:])
        if not word and None in m:
            return True
        return False


class WordDictionary:
    """Feb 12, 2022 21:29"""
    def __init__(self):
        self.trie = infdict()

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            t = t[c]
        else:
            t[None] = None

    def search(self, word: str) -> bool:
        ts = [self.trie]
        for c in word:
            if not ts:
                break
            _ts = []
            for t in ts:
                if c == '.':
                    for v in t.values():
                        if v:
                            _ts.append(v)
                elif c in t:
                    _ts.append(t[c])
            ts = _ts
        for t in ts:
            if None in t:
                return True
        return False


class WordDictionary:
    """Apr 23, 2023 18:33"""
    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        d = self.d
        for c in word:
            d = d.setdefault(c, {})
        d[None] = {}

    def search(self, word: str) -> bool:
        tries = [self.d]
        for c in word:
            _tries = []
            for d in tries:
                if c == '.':
                    _tries.extend(d.values())
                elif c in d:
                    _tries.append(d[c])
            tries = _tries
        return any(None in d for d in tries)


@pytest.mark.parametrize('args', [
    ((["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
      [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
      [None,None,None,None,False,True,True,True])),
    ((["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
      [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]],
      [None, None, None, True, True, False, True, False, False])),
])
def test(args):
    commands, arguments, expecteds = args
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    print(actual)
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
