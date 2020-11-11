
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s2 and s1, write a function to return true if s1 contains the permutation of s2. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s2 = "ab" s1 = "eidbaooo"
Output: True
Explanation: s1 contains one permutation of s2 ("ba").

Example 2:

Input:s2= "ab" s1 = "eidboaoo"
Output: False

Constraints:

	The input strings only contain lower case letters.
	The length of both given strings is in range [1, 10,000].
"""
import sys
from collections import Counter
import pytest


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        keep_cnt = Counter(s1)
        cnt = Counter(s1)
        i = j = 0
        while j < len(s2):
            if j >= n:
                if s2[i] in keep_cnt:
                    keep_cnt[s2[i]] += 1
                if keep_cnt[s2[i]] > 0:
                    if s2[i] not in cnt:
                        cnt[s2[i]] = 0
                    cnt[s2[i]] += 1
                i += 1
            if s2[j] in keep_cnt:
                keep_cnt[s2[j]] -= 1
                if s2[j] in cnt:
                    cnt[s2[j]] -= 1
                    if cnt[s2[j]] == 0:
                        cnt.pop(s2[j])
            j += 1
            if not cnt:
                return True
        return False


@pytest.mark.parametrize('s1, s2, expected', [
    ('ab', 'eidbadoo', True),
    ('ab', 'eidboaoo', False),
    ("adc", "dcda", True),
])
def test(s1, s2, expected):
    assert expected == Solution().checkInclusion(s1, s2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
