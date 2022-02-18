#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

	1 <= s.length, p.length <= 3 * 104
	s and p consist of lowercase English letters.
"""
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """04/30/2020 23:22"""
        cnt = Counter(p)
        ret = []
        i, j = 0, 0
        while j < len(s):
            if s[j] in cnt:
                cnt[s[j]] -=1
                if cnt[s[j]] == 0:
                    cnt.pop(s[j])
                if not cnt:
                    ret.append(i)
                    cnt[s[i]] = 1
                    i += 1
                j += 1
            else:
                while s[j] not in cnt and i < j:
                    if s[i] not in cnt:
                        cnt[s[i]] = 0
                    cnt[s[i]] += 1
                    i += 1
                if i == j:
                    while i < len(s) and s[i] not in cnt:
                        i += 1
                    j = i
        return ret

    def findAnagrams(self, s: str, p: str) -> List[int]:
        required = Counter(p)
        chars = set(required.keys())

        i, j = 0, len(p)
        if j > len(s):
            return []

        for k in range(i, j):
            if s[k] in chars:
                required.setdefault(s[k], 0)
                required[s[k]] -= 1
                if required[s[k]] == 0:
                    required.pop(s[k])

        ret = []
        if not required:
            ret.append(0)

        while j < len(s):
            if s[i] in chars:
                required.setdefault(s[i], 0)
                required[s[i]] += 1
                if required[s[i]] == 0:
                    required.pop(s[i])
            if s[j] in chars:
                required.setdefault(s[j], 0)
                required[s[j]] -= 1
                if required[s[j]] == 0:
                    required.pop(s[j])
            i += 1
            j += 1
            if not required:
                ret.append(i)

        return ret


@pytest.mark.parametrize('s, p, expected', [
    ("cbaebabacd", "abc", [0,6]),
    ("abab", "ab", [0,1,2]),
])
def test(s, p, expected):
    assert expected == Solution().findAnagrams(s, p)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
