#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
from collections import defaultdict
infdict = lambda: defaultdict(infdict)


NULL_CHAR = '\0'


class Trie:
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





# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    inputs = [
        [
            ('insert', 'apple'),
            ('search', 'apple'),
            ('search', 'app'),
            ('startsWith', 'app'),
            ('insert', 'app'),
            ('search', 'app')
        ]
    ]
    expecteds = [
        [None, True, False, True, None, True]
    ]
    for sequence, expected_sequence in zip(inputs, expecteds):
        trie = Trie()
        for (method, word), expected in zip(sequence, expected_sequence):
            actual = getattr(trie, method)(word)
            if expected is not None:
                print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
