from collections import Counter

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

Constraints:

	1 <= s.length <= 5 * 104
	s.length == t.length
	s and t consist of lowercase English letters only.
"""
import pytest
import sys


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """submitted at Jan 23, 2024 21:23"""
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
        return sum(v for c, v in cnt.items() if v > 0)


@pytest.mark.parametrize('args', [
    (("bab", "aba", 1)),
    (("leetcode", "practice", 5)),
    (("anagram", "mangaar", 0)),
])
def test(args):
    assert args[-1] == Solution().minSteps(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
