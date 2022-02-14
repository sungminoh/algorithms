#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We define the usage of capitals in a word to be right when one of the following cases holds:

	All letters in this word are capitals, like "USA".
	All letters in this word are not capitals, like "leetcode".
	Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true
Example 2:
Input: word = "FlaG"
Output: false

Constraints:

	1 <= word.length <= 100
	word consists of lowercase and uppercase English letters.
"""
import sys
import pytest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        start_with_cap = word[0] == word[0].upper()
        is_cap = word[1] == word[1].upper()
        if not start_with_cap and is_cap:
            return False
        i = 2
        while i < len(word):
            cap = word[i] == word[i].upper()
            if is_cap ^ cap:
                return False
            i += 1
        return True


@pytest.mark.parametrize('word, expected', [
    ("USA", True),
    ("FlaG", False),
])
def test(word, expected):
    assert expected == Solution().detectCapitalUse(word)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
