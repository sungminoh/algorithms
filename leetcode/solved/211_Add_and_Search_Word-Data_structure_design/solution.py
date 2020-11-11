#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
from collections import defaultdict


def infdict():
    return defaultdict(infdict)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = infdict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        m = self.trie
        for c, n in zip(word[:-1], word[1:]):
            m[c][n]
            m = m[c]
        m[word[-1]][None]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
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


if __name__ == '__main__':
    # Your WordDictionary object will be instantiated and called as such:
    cmds = ["WordDictionary","addWord","addWord","search","search","search","search","search","search","search","search"]
    args = [[],["a"],["ab"],["a"],["a."],["ab"],[".a"],[".b"],["ab."],["."],[".."]]
    obj = None
    for cmd, arg in zip(cmds, args):
        if cmd == 'WordDictionary':
            obj = WordDictionary()
        else:
            res = getattr(obj, cmd)(arg[0])
            print(f'{cmd}({arg[0]}){": -> " + str(res) if res is not None else ""}')
