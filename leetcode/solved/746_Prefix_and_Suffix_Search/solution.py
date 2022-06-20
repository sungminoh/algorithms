#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

	WordFilter(string[] words) Initializes the object with the words in the dictionary.
	f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:

	1 <= words.length <= 15000
	1 <= words[i].length <= 10
	1 <= prefix.length, suffix.length <= 10
	words[i], prefix and suffix consist of lower-case English letters only.
	At most 15000 calls will be made to the function f.
"""
from functools import lru_cache
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import List
import pytest


class WordFilter:
    """05/21/2021 08:59
    Prefix trie and suffix Trie
    Time complexity:
        init: O(n*l) where n = len(words), l = len(word)
        find: O(l) where l = len(prefix) + len(suffix)
    Space complexity: O(n*l*n) = #(words) * #(chars in word) * #(indexes)
    """
    def __init__(self, words: List[str]):
        def insert_trie(trie, s, v):
            t = trie
            for c in s:
                t.setdefault(c, {})
                t = t[c]
                t.setdefault(None, set())
                t[None].add(v)

        self.prefix_trie = {}
        self.suffix_trie = {}
        for i, word in enumerate(words):
            insert_trie(self.prefix_trie, word, i)
            insert_trie(self.suffix_trie, word[::-1], i)

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        def find(trie, s):
            t = trie
            for c in s:
                if c not in t:
                    return set()
                t = t[c]
            return t.get(None, set())

        prefix_indexes = find(self.prefix_trie, prefix)
        suffix_indexes = find(self.suffix_trie, suffix[::-1])
        indexes = prefix_indexes & suffix_indexes
        return max(indexes) if indexes else -1


class WordFilter:
    """05/21/2021 09:07
    Store possible (prefix, suffix) in a map
    Time complexity:
        init: O(n*l*l) without considering string slicing
        find: O(1)
    space complexity: O(n*l*l)
    """
    def __init__(self, words: List[str]):
        self.dic = {}
        for i, word in enumerate(words):
            for s in range(len(word)):
                for e in range(len(word)):
                    prefix = word[:s+1]
                    suffix = word[e:]
                    self.dic[prefix, suffix] = i

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        return self.dic.get((prefix, suffix), -1)


class WordFilter(object):
    """05/21/2021 09:11	"""
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    self.dic[word[:i]+"#"+word[j:]] = weight

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.dic.get(prefix+'#'+suffix, -1)


class WordFilter:
    """05/21/2021 09:23
    Prefix map and suffix map
    Time complexity:
        init: O(n*l) where n = len(words), l = len(word)
        find: O(l) where l = len(prefix) + len(suffix)
    Space complexity: O(n*l*n) = #(words) * #(chars in word) * #(indexes)
    """
    def __init__(self, words: List[str]):
        self.prefix_dic = {}
        self.suffix_dic = {}
        for i, word in enumerate(words):
            for j in range(len(word)):
                prefix = word[:j+1]
                suffix = word[j:]
                self.prefix_dic.setdefault(prefix, set())
                self.suffix_dic.setdefault(suffix, set())
                self.prefix_dic[prefix].add(i)
                self.suffix_dic[suffix].add(i)

    @lru_cache(None)
    def f(self, prefix: str, suffix: str) -> int:
        indexes = self.prefix_dic.get(prefix, set()) & self.suffix_dic.get(suffix, set())
        return max(indexes) if indexes else -1


class WordFilter:
    """06/19/2022 20:39"""
    def __init__(self, words: List[str]):
        self.words = {word: i for i, word in enumerate(words)}
        self.prefix_map = defaultdict(set)
        self.suffix_map = defaultdict(set)

        def add_word(word, prefix_map, i):
            k = ''
            prefix_map[k].add(i)
            for c in word:
                k += c
                prefix_map[k].add(i)

        for word, i in self.words.items():
            add_word(word, self.prefix_map, i)
            add_word(word[::-1], self.suffix_map, i)

    def f(self, prefix: str, suffix: str) -> int:
        indexes = self.prefix_map[prefix] & self.suffix_map[suffix[::-1]]
        return -1 if not indexes else max(indexes)


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["WordFilter", "f"],
     [[["apple"]], ["a", "e"]],
     [None, 0]),
    (["WordFilter","f","f","f","f","f","f","f","f","f","f"],
     [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]],
     [None,9,4,5,0,8,1,2,5,3,1]),
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](*arguments.pop(0))
    actual = []
    for cmd, arg in zip(commands, arguments):
        actual.append(getattr(obj, cmd)(*arg))
    assert expecteds[1:] == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
