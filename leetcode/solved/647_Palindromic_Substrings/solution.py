#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

	The input string length won't exceed 1000.
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j):
            cnt = 0
            while 0 <= i and j < len(s) and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
            return cnt

        return sum(expand(i, i) for i in range(len(s))) + sum(expand(i, i+1) for i in range(len(s)-1))

    def _countSubstrings(self, s: str) -> int:
        @lru_cache(None)
        def is_palindrome(i, j):
            if i == j:
                return True
            if i+1 == j and s[i] == s[j]:
                return True
            return s[i] == s[j] and is_palindrome(i+1,j-1)
        return sum(1 if is_palindrome(i, j) else 0 for j in range(len(s)) for i in range(j+1))



@pytest.mark.parametrize('s, expected', [
    ("abc", 3),
    ("aaa", 6),
])
def test(s, expected):
    assert expected == Solution().countSubstrings(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
