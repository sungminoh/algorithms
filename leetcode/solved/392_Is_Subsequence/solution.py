#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

	0 <= s.length <= 100
	0 <= t.length <= 104
	s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
import sys
import pytest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t):
                return False
            i += 1
            j += 1
        return True


@pytest.mark.parametrize('s, t, expected', [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
])
def test(s, t, expected):
    assert expected == Solution().isSubsequence(s, t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
