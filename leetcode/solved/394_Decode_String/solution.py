
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

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won&#39;t be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

&nbsp;
"""
import pytest


class Solution:
    def decodeString(self, s: str) -> str:
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


@pytest.mark.parametrize('s, expected', [
    ("3[a]2[bc]", "aaabcbc"),
    ("3[a2[c]]", "accaccacc"),
    ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ("3[a]2[b4[F]c]", "aaabFFFFcbFFFFc")
])
def test(s, expected):
    assert expected == Solution().decodeString(s)
