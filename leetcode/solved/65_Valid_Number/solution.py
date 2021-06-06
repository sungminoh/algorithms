#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A valid number can be split up into these components (in order):

	A decimal number or an integer.
	(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

	(Optional) A sign character (either '+' or '-').
	One of the following formats:

		One or more digits, followed by a dot '.'.
		One or more digits, followed by a dot '.', followed by one or more digits.
		A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):

	(Optional) A sign character (either '+' or '-').
	One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Example 4:

Input: s = ".1"
Output: true

Constraints:

	1 <= s.length <= 20
	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""
import re
import sys
import pytest


class Solution:
    def isNumber(self, s):
        """08/11/2018 19:57"""
        def isFloat(s):
            return re.search(r'[\d]+', s) is not None \
                and re.match(r'^[-+]?[\d]*\.?[\d]*$', s) is not None

        def isInt(s):
            return re.match(r'^[-+]?[\d]+$', s) is not None

        s = s.strip()
        if 'e' not in s and 'E' not in s:
            return isFloat(s)
        if 'e' in s:
            s = s.split('e')
        if 'E' in s:
            s = s.split('E')
        return len(s) == 2 and isFloat(s[0]) and isInt(s[1])

    def isNumber(self, s: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not s: return False
        i = 0
        if s[0] in '-+': i += 1
        if i == len(s): return False
        # starting with dot(.)
        if s[i] == '.':
            i += 1
            if i == len(s) or not s[i].isdigit(): return False
            while i < len(s) and s[i].isdigit(): i += 1
        else:
            # integer part
            if not s[i].isdigit(): return False
            while i < len(s) and s[i].isdigit(): i += 1
            # decimal part
            if i < len(s) and s[i] == '.': i += 1
            while i < len(s) and s[i].isdigit(): i += 1
        if i == len(s): return True
        # exponent part
        if s[i] not in 'eE': return False
        i += 1
        if i == len(s): return False
        if s[i] in '-+': i += 1
        if i == len(s) or not s[i].isdigit(): return False
        while i < len(s) and s[i].isdigit(): i += 1
        return i == len(s)


@pytest.mark.parametrize('s, expected', [
    ("0", True),
    ("e", False),
    (".", False),
    (".1", True),
    ("2", True),
    ("0089", True),
    ("-0.1", True),
    ("+3.14", True),
    ("4.", True),
    ("-.9", True),
    ("2e10", True),
    ("-90E3", True),
    ("3e+7", True),
    ("+6e-1", True),
    ("53.5e93", True),
    ("-123.456e789", True),
    ("abc", False),
    ("1a", False),
    ("1e", False),
    ("e3", False),
    ("99e2.5", False),
    ("--6", False),
    ("-+3", False),
    ("95a54e53", False),
    ("..2", False),
    ("e11", False),
    ("2e0", True),
])
def test(s, expected):
    assert expected == Solution().isNumber(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
