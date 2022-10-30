#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Constraints:

	1 <= palindrome.length <= 1000
	palindrome consists of only lowercase English letters.
"""
import pytest
import sys


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """10/29/2022 14:40"""
        if len(palindrome) == 1:
            return ''
        chars = list(palindrome)
        for i in range(len(chars)):
            c = chars[i]
            # not middle and not a
            if (len(palindrome)%2 == 0 or i != len(palindrome)//2) and c != 'a':
                chars[i] = 'a'
                return ''.join(chars)
        chars[-1] = 'b'
        return ''.join(chars)


@pytest.mark.parametrize('palindrome, expected', [
    ("abccba", "aaccba"),
    ("a", ""),
    ("aba", "abb")
])
def test(palindrome, expected):
    assert expected == Solution().breakPalindrome(palindrome)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
