#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

	Trie() Initializes the trie object.
	void insert(String word) Inserts the string word into the trie.
	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:

	1 <= word.length, prefix.length <= 2000
	word and prefix consist only of lowercase English letters.
	At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
import sys
from collections import defaultdict
import pytest


infdict = lambda: defaultdict(infdict)
NULL_CHAR = '\0'


class Trie:
    """03/11/2019 04:01"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = infdict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dic = self.dic
        for c in word:
            dic = dic[c]
        else:
            dic[NULL_CHAR]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        dic = self.dic
        for c in word:
            if c in dic:
                dic = dic[c]
            else:
                return False
        return NULL_CHAR in dic

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        dic = self.dic
        for c in prefix:
            if c in dic:
                dic = dic[c]
            else:
                return False
        return True

    def __repr__(self):
        def repr(dic, indent=0):
            for k, v in dic.items():
                return ' ' * indent + f'{k}:\n{repr(v, indent+1)}'
        return repr(self.dic)



class Trie:
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        d = self.d
        for c in word:
            d.setdefault(c, {})
            d = d[c]
        else:
            d[None] = None

    def search(self, word: str) -> bool:
        d = self.d
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return None in d

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
     [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
     [None, None, True, False, True, None, True]),
])
def test(commands, arguments, expecteds):
    obj = Trie()
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
