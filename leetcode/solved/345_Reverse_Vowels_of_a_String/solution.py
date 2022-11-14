#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:

	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.
"""
import pytest
import sys


class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        i = 0
        j = len(l)-1
        while i < j:
            if l[i] not in 'aeiouAEIOU':
                i += 1
            elif l[j] not in 'aeiouAEIOU':
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return ''.join(l)


@pytest.mark.parametrize('s, expected', [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
    ("aA", "Aa"),
])
def test(s, expected):
    assert expected == Solution().reverseVowels(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
