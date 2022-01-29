#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:

	1 <= s.length <= 16
	s contains only lowercase English letters.
"""
from collections import defaultdict
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def partition(self, s):
        """07/08/2018 03:52"""
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j-1]:
                    return False
                i += 1
                j -= 1
            return True

        @lru_cache(None)
        def part(i):
            if i == len(s):
                return [[]]
            ret = []
            for j in range(i+1, len(s)+1):
                if is_palindrome(i, j):
                    ret.extend([[s[i:j], *x] for x in part(j)])
            return ret

        return part(0)

    def partition(self, s: str) -> List[List[str]]:
        """12/04/2021 10:59"""
        @lru_cache(None)  # O(n^2)
        def is_palindrome(i, j):
            if i == j:
                return True
            if i+1 == j:
                return s[i] == s[j]
            return is_palindrome(i+1, j-1) and s[i] == s[j]

        @lru_cache(None)  # O(n^2)
        def palindromes_ends_at_i(i):
            ret = []
            for j in range(i+1):
                if is_palindrome(j, i):
                    ret.append(s[j:i+1])
            return ret

        @lru_cache(None)
        def partition(i):
            if i < 0:
                return [[]]
            ret = []
            palindromes = palindromes_ends_at_i(i)
            for palindrome in palindromes:  # at most n: a
                for part in partition(i-len(palindrome)):  # O(2^(n-a))
                    ret.append(part + [palindrome])
            return ret

        return partition(len(s)-1)

    @lru_cache(None)
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(None)
        def is_palindrome(s):
            return s == s[::-1]

        ret = []
        for i in range(1, len(s)):
            if is_palindrome(s[:i]):
                for sub in self.partition(s[i:]):
                    ret.append([s[:i]] + sub)
        if is_palindrome(s):
            ret.append([s])
        return ret



@pytest.mark.parametrize('s, expected', [
    ("aab", [["a","a","b"],["aa","b"]]),
    ("a", [["a"]]),
])
def test(s, expected):
    assert sorted(expected) == sorted(Solution().partition(s))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
