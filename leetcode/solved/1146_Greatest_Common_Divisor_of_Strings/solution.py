#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

	1 <= str1.length, str2.length <= 1000
	str1 and str2 consist of English uppercase letters.
"""
import pytest
import sys


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Mar 18, 2023 14:02"""
        if len(str1)>len(str2):
            return self.gcdOfStrings(str2, str1)
        if not str2.startswith(str1):
            return ''
        if str1 == str2:
            return str1
        return self.gcdOfStrings(str2[len(str1):], str1)


@pytest.mark.parametrize('args', [
    (("ABCABC", "ABC", "ABC")),
    (("ABABAB", "ABAB", "AB")),
    (("LEET", "CODE", "")),
])
def test(args):
    assert args[-1] == Solution().gcdOfStrings(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
