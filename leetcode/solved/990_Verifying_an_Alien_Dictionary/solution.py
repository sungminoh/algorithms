#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

	1 <= words.length <= 100
	1 <= words[i].length <= 20
	order.length == 26
	All characters in words[i] and order are English lowercase letters.
"""
import sys
from typing import List
import pytest


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        def ordered(a, b):
            for x, y in zip(a, b):
                if m[x] > m[y]:
                    return False
                if m[x] < m[y]:
                    return True
            return len(a) <= len(b)

        for i in range(len(words)-1):
            a, b = words[i:i+2]
            if not ordered(a, b):
                return False

        return True


@pytest.mark.parametrize('words, order, expected', [
    (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
    (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
])
def test(words, order, expected):
    assert expected == Solution().isAlienSorted(words, order)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
