
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
import sys
from copy import deepcopy
from collections import Counter
from typing import List
import pytest


class Solution:
    def _findAnagrams(self, s: str, p: str) -> List[int]:
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


@pytest.mark.parametrize('s, p, expected', [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab", "ab", [0, 1, 2]),
])
def test(s, p, expected):
    assert expected == Solution().findAnagrams(s, p)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
