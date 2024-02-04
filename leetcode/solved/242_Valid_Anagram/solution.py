from collections import Counter

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
import pytest
import sys


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Aug 06, 2022 22:47"""
        if len(s) != len(t):
            return False
        cnt = Counter(s)
        for c in t:
            if cnt.get(c, 0) <= 0:
                return False
            cnt[c] -= 1
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        """Feb 03, 2024 18:43"""
        return Counter(s) == Counter(t)


@pytest.mark.parametrize('args', [
    (("anagram", "nagaram", True)),
    (("rat", "car", False)),
])
def test(args):
    assert args[-1] == Solution().isAnagram(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
