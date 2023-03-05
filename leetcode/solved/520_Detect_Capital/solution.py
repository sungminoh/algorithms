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
import pytest
import sys


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """Feb 08, 2022 12:57"""
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

    def detectCapitalUse(self, word: str) -> bool:
        """Mar 04, 2023 20:17"""
        if len(word) <= 1:
            return True
        cap1 = word[0].isupper()
        cap2 = word[1].isupper()
        if not cap1 and cap2:
            return False
        cap = cap1 and cap2
        for i in range(2, len(word)):
            if word[i].isupper() != cap:
                return False
        return True


@pytest.mark.parametrize('args', [
    (("USA", True)),
    (("FlaG", False)),
    (("mL", False)),
])
def test(args):
    assert args[-1] == Solution().detectCapitalUse(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
