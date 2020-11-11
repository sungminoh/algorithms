
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"

Example 2:

Input: "cbacdcbc"
Output: "acdb"

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
import sys
from collections import Counter
import pytest


def binsearch(s, c):
    i, j = 0, len(s)-1
    while i <= j:
        m = i + (j-i)//2
        if c <= s[m]:
            j = m - 1
        else:
            i = m + 1
    return i


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        ret = []
        seen = set()
        for i, c in enumerate(s):
            cnt[c] -= 1
            if c in seen:
                continue
            while ret and ret[-1] > c and cnt[ret[-1]] >= 1:
                seen.remove(ret.pop())
            ret.append(c)
            seen.add(c)
        return ''.join(ret)

    def _removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        char_idx = dict()
        ordered = []
        for i, c in enumerate(s):
            idx = binsearch(ordered, c)
            if c in char_idx:
                cnt[c] -= 1
            else:
                ordered.insert(idx, c)
                char_idx[c] = i
                for j in range(len(ordered)-1, idx, -1):
                    if cnt[ordered[j]] > 1:
                        cnt[ordered[j]] -= 1
                        char_idx.pop(ordered[j])
                        ordered.pop(j)
            if cnt[c] == 1:
                for d in ordered[:idx+1]:
                    cnt[d] = 1
                ordered = ordered[idx+1:]

        return ''.join([x[0] for x in sorted(char_idx.items(), key=lambda x: x[1])])


@pytest.mark.parametrize('s, expected', [
    ("bcabc", "abc"),
    ("cbacdcbc", "acdb"),
    ("bbcaac", "bac"),
    ("bccab", "bca"),
    ("bddbccd", "bcd"),
])
def test(s, expected):
    assert expected == Solution().removeDuplicateLetters(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
