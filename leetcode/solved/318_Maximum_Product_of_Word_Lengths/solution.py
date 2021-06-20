#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

Constraints:

	2 <= words.length <= 1000
	1 <= words[i].length <= 1000
	words[i] consists only of lowercase English letters.
"""
import sys
import string
from typing import List
import pytest


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """12/28/2019 14:58	"""
        binary_map = {c: pow(2, i) for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
        rep_length = {}
        for w in words:
            rep = sum(binary_map[c] for c in set(w))
            rep_length[rep] = max(rep_length.get(rep, 0), len(w))
        m = 0
        keys = list(rep_length.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    length_mul = rep_length[keys[i]] * rep_length[keys[j]]
                    if length_mul > m:
                        m = length_mul
        return m

    def maxProduct(self, words: List[str]) -> int:
        """
        Time complexity: O(n*l)
        Space complexity: O(n)
        """
        codebook = {c: 1<<i for i, c in enumerate(string.ascii_lowercase)}

        def encode(word):
            return sum(codebook[c] for c in set(word))

        ret = 0
        codes = [encode(word) for word in words]
        for i in range(len(codes)):
            for j in range(i, len(codes)):
                if codes[i] & codes[j] == 0:
                    ret = max(ret, len(words[i])*len(words[j]))
        return ret


@pytest.mark.parametrize('words, expected', [
    (["abcw","baz","foo","bar","xtfn","abcdef"], 16),
    (["a","ab","abc","d","cd","bcd","abcd"], 4),
    (["a","aa","aaa","aaaa"], 0),
])
def test(words, expected):
    assert expected == Solution().maxProduct(words)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
