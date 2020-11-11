
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
from collections import Counter
from collections import defaultdict
import pytest


def split(s, chars):
    ret = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] not in chars:
            j += 1
        word = s[i:j]
        if word:
            ret.append(word)
        i = j + 1
    return ret


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = Counter(s)
        scants = set()
        for c, cnt in cnt.items():
            if cnt < k:
                scants.add(c)
        if not scants:
            return len(s)
        return max([self.longestSubstring(sub, k) for sub in split(s, scants)], default=0)


    def _longestSubstring(self, s: str, k: int) -> int:
        m = 0
        i = 0
        while i < len(s):
            cnt = defaultdict(int)
            fulfilled = set()
            next_i = i + 1
            for j in range(i, len(s)):
                if s[j] not in fulfilled:
                    cnt[s[j]] += 1
                    if cnt[s[j]] >= k:
                        cnt.pop(s[j])
                        fulfilled.add(s[j])
                if not cnt and j - i+ 1 > m:
                    m = j - i + 1
                    next_i = j + 1
            i = next_i
        return m


@pytest.mark.parametrize('s, k, expected', [
    ("aaabb", 3, 3),
    ("ababbc", 2, 5),
    ("aaabbb", 3, 6),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100000, 0),
    ("bbaaacbd", 3, 3)
])
def test(s, k, expected):
    assert expected == Solution().longestSubstring(s, k)
