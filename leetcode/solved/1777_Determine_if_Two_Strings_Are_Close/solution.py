from collections import Counter

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Two strings are considered close if you can attain one from the other using the following operations:

	Operation 1: Swap any two existing characters.

		For example, abcde -> aecdb

	Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.

		For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

	1 <= word1.length, word2.length <= 105
	word1 and word2 contain only lowercase English letters.
"""
import pytest
import sys


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """Dec 04, 2022 20:47"""
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return set(cnt1.keys()) == set(cnt2.keys()) \
            and Counter(cnt1.values()) == Counter(cnt2.values())

    def closeStrings(self, word1: str, word2: str) -> bool:
        """Jan 24, 2024 19:49"""
        a = Counter(word1)
        b = Counter(word2)
        return set(a.keys()) == set(b.keys()) and Counter(a.values()) == Counter(b.values())


@pytest.mark.parametrize('args', [
    (("abc", "bca", True)),
    (("a", "aa", False)),
    (("cabbba", "abbccc", True)),
    (("uau", "ssx", False)),
    (("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff", False)),
])
def test(args):
    assert args[-1] == Solution().closeStrings(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
