#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

	1 <= s.length <= 30
	s consists of lowercase English letters, digits, and square brackets '[]'.
	s is guaranteed to be a valid input.
	All the integers in s are in the range [1, 300].
"""
import sys
import pytest


class Solution:
    def decodeString(self, s: str) -> str:
        """04/19/2020 15:01"""
        def _rec(i: int):
            if i >= len(s) or s[i] == ']':
                return '', i + 1
            if not s[i].isdigit():
                sub, idx = _rec(i + 1)
                return s[i] + sub, idx
            else:
                # get repeat
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                repeat = int(s[i:j])
                sub, idx = _rec(j + 1)
                later, idx = _rec(idx)
                return sub * repeat + later, idx

        ret = ''
        idx = 0
        while idx < len(s):
            sub, idx = _rec(idx)
            ret += sub
        return ret

    def decodeString(self, s: str) -> str:
        stack = ['']
        repeats = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append('')
                i += 1
            elif s[i].isdigit():
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                repeats.append(int(s[j:i]))
            elif s[i] == ']':
                subs = repeats.pop() * stack.pop()
                stack[-1] += subs
                i += 1
            else:
                stack[-1] += s[i]
                i += 1

        return stack[0]


@pytest.mark.parametrize('s, expected', [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("3[a]2[b4[F]c]", "aaabFFFFcbFFFFc")
])
def test(s, expected):
    assert expected == Solution().decodeString(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
