#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:

	1 <= s.length <= 5 * 104
	t.length == s.length
	s and t consist of any valid ascii character.
"""
import sys
import pytest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        used = set()
        m = {}
        for a, b in zip(s, t):
            if a in m and m[a] != b:
                return False
            if a not in m:
                if b in used:
                    return False
                m[a] = b
            used.add(b)
        return True


@pytest.mark.parametrize('s, t, expected', [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("badc", "baba", False),
])
def test(s, t, expected):
    assert expected == Solution().isIsomorphic(s, t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
