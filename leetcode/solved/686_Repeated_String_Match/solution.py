#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings a and b, return the minimum number of times you should repeat the string a so that string b is a substring of it. If it's impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "",  repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:

Input: a = "a", b = "aa"
Output: 2

Example 3:

Input: a = "a", b = "a"
Output: 1

Example 4:

Input: a = "abc", b = "wxyz"
Output: -1

Constraints:

	1 <= a.length <= 104
	1 <= b.length <= 104
	a and b consist of lower-case English letters.
"""
import sys
import pytest


def kmp(p, s):
    def build_lps(s):
        ret = [0]
        i = 0
        for c in s[1:]:
            while c != s[i] and i>0:
                i = ret[i-1]
            if c == s[i]:
                i += 1
                ret.append(i)
            else:
                ret.append(0)
        return ret

    lps = build_lps(p)
    i = 0
    for j, c in enumerate(s):
        while c != p[i] and i > 0:
            i = lps[i-1]
        if c == p[i]:
            i += 1
        if i == len(p):
            return j - len(p) + 1
    else:
        return len(s) - i


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        i = kmp(a, b)
        if i > len(a) or (i > 0 and a[-i:] != b[:i]):
            return -1
        cnt = 0 if i == 0 else 1
        for j in range(i, len(b), len(a)):
            if not a.startswith(b[j:min(len(b), j+len(a))]):
                return -1
            cnt += 1
        return cnt


@pytest.mark.parametrize('a, b, expected', [
    ("abcd", "cdabcdab", 3),
    ("a", "aa", 2),
    ("a", "a", 1),
    ("abc", "wxyz", -1),
    ("abc", "wxyz", -1),
    ("axaxaya", "axaya", 1),
    ("abaababa", "abaabaa", 2),
    ("aaaaaaaaaaaaaaaaaaaaaab", "ba", 2)
])
def test(a, b, expected):
    assert expected == Solution().repeatedStringMatch(a, b)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
