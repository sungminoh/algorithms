#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

	1 <= haystack.length, needle.length <= 104
	haystack and needle consist of only lowercase English characters.
"""
import pytest
import sys


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Apr 02, 2023 20:15"""
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
                    return j-len(p)+1
            return -1

        return kmp(needle, haystack)


@pytest.mark.parametrize('args', [
    (("sadbutsad", "sad", 0)),
    (("leetcode", "leeto", -1)),
    (("mississippi", "issip", 4)),
    (("bbababaaaababbaabbbabbbaaabbbaaababbabaabbaaaaabbaaabbbbaaabaabbaababbbaabaaababbaaabbbbbbaabbbbbaaabbababaaaaabaabbbababbaababaabbaa", "bbabba", -1)),
])
def test(args):
    assert args[-1] == Solution().strStr(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
