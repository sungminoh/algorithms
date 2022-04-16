#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

	1 <= s.length <= 105
	s consists of lowercase English letters.
"""
import sys
import pytest


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s)-1
        while i<j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return is_palindrome(i+1, j) or is_palindrome(i, j-1)
        return True


@pytest.mark.parametrize('s, expected', [
("aba", True),
("abca", True),
("abc", False),
])
def test(s, expected):
    assert expected == Solution().validPalindrome(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
