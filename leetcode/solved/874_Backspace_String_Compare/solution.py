#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:

	1 <= s.length, t.length <= 200
	s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""
import sys
import pytest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """From the back"""
        i = len(s)-1
        j = len(t)-1
        di = dj = 0
        while i>=0 or j>=0:
            if i>=0 and s[i] == '#':
                di += 1
                i -= 1
            elif di > 0:
                di -= 1
                i -= 1
            elif j>=0 and t[j] == '#':
                dj += 1
                j -= 1
            elif dj > 0:
                dj -= 1
                j -= 1
            elif i>=0 and j>=0 and s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                return False
        return True


@pytest.mark.parametrize('s, t, expected', [
    ("ab#c", "ad#c", True),
    ("ab##", "c#d#", True),
    ("a#c", "b", False),
])
def test(s, t, expected):
    assert expected == Solution().backspaceCompare(s, t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

