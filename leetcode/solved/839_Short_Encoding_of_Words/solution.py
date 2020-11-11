
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:

	1 .
	1 .
	Each word has only lowercase letters.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


def infdict():
    return defaultdict(infdict)

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
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


@pytest.mark.parametrize('words, expected', [
    (["time", "me", "bell"], 10),
    ([], 0),
    (["lime", "time", "me", "bell"], 15),
])
def test(words, expected):
    assert expected == Solution().minimumLengthEncoding(words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
