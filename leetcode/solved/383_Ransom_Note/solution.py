#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

	1 <= ransomNote.length, magazine.length <= 105
	ransomNote and magazine consist of lowercase English letters.
"""
import sys
from collections import Counter
import pytest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for c in ransomNote:
            if cnt.get(c, 0) <= 0:
                return False
            cnt[c] -= 1
        return True


@pytest.mark.parametrize('ransomNote, magazine, expected', [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
])
def test(ransomNote, magazine, expected):
    assert expected == Solution().canConstruct(ransomNote, magazine)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
