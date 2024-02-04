import itertools
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:

	1 <= word1.length, word2.length <= 103
	1 <= word1[i].length, word2[i].length <= 103
	1 <= sum(word1[i].length), sum(word2[i].length) <= 103
	word1[i] and word2[i] consist of lowercase letters.
"""
import pytest
import sys


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """11/06/2022 14:16"""
        for a, b in itertools.zip_longest(itertools.chain(*word1), itertools.chain(*word2)):
            if a != b:
                return False
        return True

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Feb 04, 2024 12:35"""
        return all(x == y for x, y in itertools.zip_longest(itertools.chain(*word1), itertools.chain(*word2)))


@pytest.mark.parametrize('args', [
    ((["ab", "c"], ["a", "bc"], True)),
    ((["a", "cb"], ["ab", "c"], False)),
    ((["abc", "d", "defg"], ["abcddefg"], True)),
    ((["abc", "d", "defg"], ["abcddef"], False)),
])
def test(args):
    assert args[-1] == Solution().arrayStringsAreEqual(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
