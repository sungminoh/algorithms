#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does not necessarily need to be contiguous.

A string is called palindrome if is one that reads the same backward as well as forward.

Example 1:

Input: s = "ababa"
Output: 1
Explanation: s is already a palindrome, so its entirety can be removed in a single step.

Example 2:

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "".
Remove palindromic subsequence "a" then "bb".

Example 3:

Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "".
Remove palindromic subsequence "baab" then "b".

Constraints:

	1 <= s.length <= 1000
	s[i] is either 'a' or 'b'.
"""
import sys
import pytest


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if 'a' not in s or 'b' not in s or s[::-1] == s:
            return 1
        return 2


@pytest.mark.parametrize('s, expected', [
    ("ababa", 1),
    ("abb", 2),
    ("baabb", 2),
])
def test(s, expected):
    assert expected == Solution().removePalindromeSub(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
