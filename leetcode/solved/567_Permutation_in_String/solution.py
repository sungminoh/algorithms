#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

	1 <= s1.length, s2.length <= 104
	s1 and s2 consist of lowercase English letters.
"""
from collections import Counter
import pytest
import sys


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """06/13/2020 00:51"""
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

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = Counter(s1)
        remainders = set(s1)
        for i in range(len(s1)):
            c = s2[i]
            if c in cnt:
                cnt[c] -= 1
                if cnt[c] == 0:
                    remainders.remove(c)

        if not remainders:
            return True

        for j in range(len(s1), len(s2)):
            i = j-len(s1)
            pre = s2[i]
            nxt = s2[j]
            if pre in cnt:
                if cnt[pre] == 0:
                    remainders.add(pre)
                cnt[pre] += 1
            if nxt in cnt:
                cnt[nxt] -= 1
                if cnt[nxt] == 0:
                    remainders.remove(nxt)
            if not remainders:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Mar 18, 2023 15:03"""
        chars = set(s1)
        cnt = Counter(s1)
        i = j = 0
        while i < len(s2):
            if s2[i] in chars:
                cnt[s2[i]] -= 1
                if cnt[s2[i]] == 0:
                    cnt.pop(s2[i])
            if j <= i-len(s1):
                if s2[j] in chars:
                    cnt[s2[j]] += 1
                    if cnt[s2[j]] == 0:
                        cnt.pop(s2[j])
                j += 1
            if not cnt:
                return True
            i += 1
        return False


@pytest.mark.parametrize('args', [
    (("ab", "eidbaooo", True)),
    (("ab", "eidboaoo", False)),
    (("adc", "dcda", True)),
])
def test(args):
    assert args[-1] == Solution().checkInclusion(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
