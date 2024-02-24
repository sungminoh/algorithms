#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

	For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:

	3 <= s.length <= 105
	s consists of only lowercase English letters.
"""
from collections import Counter
import pytest
import sys


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """Feb 24, 2024 13:17"""
        counter = [0] * 26
        start_end_map = {}
        acc = []
        for i, c in enumerate(s):
            counter[ord(c)-ord('a')] += 1
            acc.append(tuple(counter))
            start, end = start_end_map.get(c, (float('inf'), -float('inf')))
            start_end_map[c] = min(start, i), max(end, i)

        ret = 0
        for c, (start, end) in start_end_map.items():
            if end-start <= 1:
                continue
            for a, b in zip(acc[end-1], acc[start]):
                if a-b > 0:
                    ret += 1
        return ret


@pytest.mark.parametrize('args', [
    (("aabca", 3)),
    (("adc", 0)),
    (("bbcbaba", 4)),
])
def test(args):
    assert args[-1] == Solution().countPalindromicSubsequence(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
