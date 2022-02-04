#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

	1 <= pattern.length <= 300
	pattern contains only lower-case English letters.
	1 <= s.length <= 3000
	s contains only lowercase English letters and spaces ' '.
	s does not contain any leading or trailing spaces.
	All the words in s are separated by a single space.
"""
import itertools
import sys
import pytest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cm = {}
        wm = {}
        for c, w in itertools.zip_longest(pattern, s.split()):
            if c is None or w is None \
                    or (c in cm and cm[c] != w) \
                    or (w in wm and wm[w] != c):
                return False
            cm[c] = w
            wm[w] = c
        return True


@pytest.mark.parametrize('pattern, s, expected', [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abcd", "dog cat cat dog", False),
    ("aaa", "aa aa aa aa", False),
    ("he", "unit", False)
])
def test(pattern, s, expected):
    assert expected == Solution().wordPattern(pattern, s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
