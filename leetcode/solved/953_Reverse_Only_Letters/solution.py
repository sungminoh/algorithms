#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, reverse the string according to the following rules:

	All the characters that are not English letters remain in the same position.
	All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"
Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

	1 <= s.length <= 100
	s consists of characters with ASCII values in the range [33, 122].
	s does not contain '\"' or '\\'.
"""
import sys
import pytest


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        alphas = [c for c in reversed(s) if c.isalpha()]
        ret = ''
        i = 0
        for c in s:
            if c.isalpha():
                ret += alphas[i]
                i += 1
            else:
                ret += c
        return ret

    def reverseOnlyLetters(self, s: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        j = len(s)-1
        ret = ''
        for i, c in enumerate(s):
            if not c.isalpha():
                ret += c
            else:
                while j > 0 and not s[j].isalpha():
                    j -= 1
                ret += s[j]
                j -= 1
        return ret


@pytest.mark.parametrize('s, expected', [
    ("ab-cd", "dc-ba"),
    ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
])
def test(s, expected):
    assert expected == Solution().reverseOnlyLetters(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
