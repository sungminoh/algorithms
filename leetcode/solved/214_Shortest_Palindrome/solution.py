
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"
"""
import sys
import pytest



def kmp(p, s):
    def _build_lps(p):
        ret = [0] * len(p)
        i, j = 0, 1
        while i < len(p) and j < len(p):
            if p[i] == p[j]:
                i += 1
                ret[j] = i
                j += 1
            else:
                if i != 0:
                    i = ret[i - 1]
                else:
                    ret[j] = 0
                    j += 1
        return ret

    def build_lps(p):
        ret = [0]
        for i in range(1, len(p)):
            j = ret[i-1]
            while j > 0 and p[i] != p[j]:
                j = ret[j-1]
            if p[i] == p[j]:
                j += 1
            ret.append(j)
        return ret

    lps = build_lps(p)
    i, j = 0, 0
    while j < len(p):
        if i >= len(s):
            break
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    return i - j


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rs = s[::-1]
        i = kmp(s, rs)
        return (rs + rs[:i][::-1])[::-1]


@pytest.mark.parametrize('s, expected', [
    ("aacecaaa", "aaacecaaa"),
    ("abcd", "dcbabcd"),
])
def test(s, expected):
    assert expected == Solution().shortestPalindrome(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
