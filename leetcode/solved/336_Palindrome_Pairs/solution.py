#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

	0 <= i, j < word.length,
	i != j, and
	words[i] + words[j] (the concatenation of the two strings) is a palindrome string.

Return an array of all the palindrome pairs of words.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]

Constraints:

	1 <= words.length <= 5000
	0 <= words[i].length <= 300
	words[i] consists of lowercase English letters.
"""
from functools import lru_cache
from pathlib import Path
import json
from collections import defaultdict
from typing import List
import pytest
import sys


def infdict():
    return defaultdict(infdict)


def to_dict(d):
    return {k: to_dict(v) for k, v in d.items()} if isinstance(d, dict) else d


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """10/08/2020 09:59"""
        @lru_cache(None)
        def is_palindrome(s):
            return s == s[::-1]

        def find_all(d, stack):
            for k, v in d.items():
                if k is not None:
                    yield from find_all(v, stack + [k])
                else:
                    if is_palindrome(''.join(stack)):
                        yield from v

        ret = []
        trie = infdict()
        for i, word in enumerate(words):
            d = trie
            for c in reversed(word):
                d = d[c]
            else:
                d.setdefault(None, [])
                d[None].append(i)
        # print(to_dict(trie))
        for i, word in enumerate(words):
            d = trie
            for _i, c in enumerate(word):
                if None in d:
                    if is_palindrome(word[_i:]):
                        for j in d[None]:
                            ret.append([i, j])
                if c not in d:
                    break
                d = d[c]
            else:
                for j in find_all(d, []):
                    if i != j:
                        ret.append([i, j])

        return ret

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        @lru_cache(None)
        def is_palindrome(w):
            return w == w[::-1]

        word_index = {word: i for i, word in enumerate(words)}
        postfix = {}
        for i, word in enumerate(words):
            for p in range(1, len(word)+1):
                head, tail = word[:p], word[p:]
                if is_palindrome(head):
                    postfix.setdefault(tail, [])
                    postfix[tail].append(i)

        ret = []
        for i, word in enumerate(words):
            for p in range(len(word)):
                reversed_head, tail = word[:p][::-1], word[p:]
                if reversed_head in word_index and is_palindrome(tail):
                    ret.append([i, word_index[reversed_head]])
            if word[::-1] in word_index:
                j = word_index[word[::-1]]
                if i != j:
                    ret.append([i, j])
            for j in postfix.get(word[::-1], []):
                ret.append([i, j])

        return ret

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        @lru_cache(None)
        def is_palindrome(w):
            return w == w[::-1]

        word_index = {word: i for i, word in enumerate(words)}

        ret = []
        for i, word in enumerate(words):
            for p in range(len(word)+1):
                head, tail = word[:p], word[p:]
                if tail and is_palindrome(tail) and head[::-1] in word_index:
                    ret.append([i, word_index[head[::-1]]])
                if is_palindrome(head) and tail[::-1] in word_index:
                    j = word_index[tail[::-1]]
                    if i != j:
                        ret.append([j, i])

        return ret

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """10/15/2022 16:35
        TLE or Memory limit exceeded if cached
        """
        def is_palindrom(s):
            return s == s[::-1]

        prefix_map = defaultdict(set)
        suffix_map = defaultdict(set)
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                p, s = w[:j], w[j:]
                if is_palindrom(p):
                    suffix_map[s].add(i)
                if is_palindrom(s):
                    prefix_map[p].add(i)

        ret = set()
        for i, w in enumerate(words):
            for j in prefix_map.get(w[::-1], set()):
                if i != j:
                    ret.add((j, i))
            for j in suffix_map.get(w[::-1], set()):
                if i != j:
                    ret.add((i, j))

        return [list(x) for x in ret]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """10/15/2022 16:54"""
        @lru_cache(None)
        def is_palindrom(s):
            return s == s[::-1]

        index = {w: i for i, w in enumerate(words)}
        ret = set()
        for i, w in enumerate(words):
            for k in range(len(w)+1):
                p, s = w[:k], w[k:]
                suffix_match = index.get(s[::-1], -1)
                if is_palindrom(p) and suffix_match >= 0:
                    if suffix_match != i:
                        ret.add((suffix_match, i))
                prefix_match = index.get(p[::-1], -1)
                if is_palindrom(s) and prefix_match >= 0:
                    if prefix_match != i:
                        ret.add((i, prefix_match))

        return [list(x) for x in ret]


@pytest.mark.parametrize('words, expected', [
    (["abcd","dcba","lls","s","sssll"], [[0,1],[1,0],[3,2],[2,4]]),
    (["bat","tab","cat"], [[0,1],[1,0]]),
    (["a",""], [[0,1],[1,0]]),
    (["ab","ba","abc","cba"], [[0,1],[1,0],[2,1],[2,3],[0,3],[3,2]])
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(words, expected):
    actual = Solution().palindromePairs(words)
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
