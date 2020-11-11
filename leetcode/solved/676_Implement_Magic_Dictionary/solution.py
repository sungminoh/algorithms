#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:

You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
import sys
from typing import List
from collections import defaultdict
import pytest


def infdict():
    return defaultdict(infdict)


class MagicDictionary:
    _END = '__END__'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = infdict()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            d = self.d
            for c in word:
                d = d[c]
            d[self._END]

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        def search_with_tolerance(d, w, t):
            if len(w) == 0:
                return self._END in d and t == 0
            if t == 0 and w[0] not in d:
                return False
            found = False
            if w[0] in d:
                found |= search_with_tolerance(d[w[0]], w[1:], t)
            for k, v in d.items():
                if k != w[0]:
                    found |= search_with_tolerance(v, w[1:], t-1)
            return found

        return search_with_tolerance(self.d, word, 1)


@pytest.mark.parametrize('commands, args, expected', [
    (['buildDict', 'search', 'search', 'search', 'search'],
     [[["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
     [None, False, True, False, False]),
    (["buildDict", "search", "search", "search", "search"],
     [[["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
     [None,True,True,False,False])
])
def test(commands, args, expected):
    o = MagicDictionary()
    for c, a, e in zip(commands, args, expected):
        actual = getattr(o, c)(*a)
        assert e == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
