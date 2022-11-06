#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false

Constraints:

	1 <= sentence.length <= 1000
	sentence consists of lowercase English letters.
"""
import pytest
import sys


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


@pytest.mark.parametrize('sentence, expected', [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
])
def test(sentence, expected):
    assert expected == Solution().checkIfPangram(sentence)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
