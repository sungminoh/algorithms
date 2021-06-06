#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]

Constraints:

	1 <= pattern.length <= 20
	1 <= words.length <= 50
	words[i].length == pattern.length
	pattern and words[i] are lowercase English letters.
"""
import sys
from typing import List
import pytest


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Time complexity: O(n*l)
        Space complexity: O(l)
        """
        def match(s1, s2) -> bool:
            if len(s1) != len(s2):
                return False
            m = {}
            r = {}
            for a, b in zip(s1, s2):
                if a not in m and b not in r:
                    m[a] = b
                    r[b] = a
                if m.get(a) != b:
                    return False
            return True

        return [word for word in words if match(word, pattern)]


@pytest.mark.parametrize('words, pattern, expected', [
    (["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]),
    (["a","b","c"], "a", ["a","b","c"]),
    (["ef","fq","ao","at","lx"], "ya", ["ef","fq","ao","at","lx"]),
])
def test(words, pattern, expected):
    assert expected == Solution().findAndReplacePattern(words, pattern)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
