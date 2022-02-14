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
	There will be at most 3 dots in word for search queries.
	At most 104 calls will be made to addWord and search.
"""
from collections import defaultdict
import sys
import pytest


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


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
     [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
     [None,None,None,None,False,True,True,True]),
    (["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
     [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]],
     [[],None,None,True,True,False,True,False,False]),
])
def test(commands, arguments, expecteds):
    obj = WordDictionary(*arguments[0])
    for cmd, arg, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*arg)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
