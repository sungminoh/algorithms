#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Let's define a function countUniqueChars(s) that returns the number of unique characters in s.

	For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

Example 3:

Input: s = "LEETCODE"
Output: 92

Constraints:

	1 <= s.length <= 105
	s consists of uppercase English letters only.
"""
import pytest
import sys


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """Apr 16, 2024 11:26"""
        N = len(s)
        ret = 0

        positions = {}
        for i, c in enumerate(s):
            if c not in positions:
                positions[c] = [-1, i]
            else:
                p, j = positions.pop(c)
                left = j-p
                right = i-1-j
                ret += left + right + (left-1)*right
                positions[c] = [j, i]

        for c, (p, j) in positions.items():
            left = j-p
            right = N-1-j
            ret += left + right + (left-1)*right
        return ret



@pytest.mark.parametrize('args', [
    (("ABC", 10)),
    (("ABA", 8)),
    (("LEETCODE", 92)),
])
def test(args):
    assert args[-1] == Solution().uniqueLetterString(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
