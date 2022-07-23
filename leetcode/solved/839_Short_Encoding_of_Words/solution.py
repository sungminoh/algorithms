#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A valid encoding of an array of words is any reference string s and array of indices indices such that:

	words.length == indices.length
	The reference string s ends with the '#' character.
	For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].

Constraints:

	1 <= words.length <= 2000
	1 <= words[i].length <= 7
	words[i] consists of only lowercase letters.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


def infdict():
    return defaultdict(infdict)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """05/25/2020 15:36"""
        if not words:
            return 0

        suffix_trie = infdict()
        for w in words:
            root = suffix_trie
            for c in reversed(w):
                root = root[c]

        def count(root, depth=0):
            if not root:
                return depth + 1
            else:
                return sum(count(branch, depth + 1) for branch in root.values())

        return count(suffix_trie)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = infdict()
        for word in words:
            t = trie
            for c in reversed(word):
                t = t[c]

        def dfs(t, d):
            if not t:
                return d+1
            return sum(dfs(v, d+1) for v in t.values())

        return dfs(trie, 0)


@pytest.mark.parametrize('words, expected', [
    (["time", "me", "bell"], 10),
    ([], 0),
    (["t"], 2),
    (["lime", "time", "me", "bell"], 15),
])
def test(words, expected):
    assert expected == Solution().minimumLengthEncoding(words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
