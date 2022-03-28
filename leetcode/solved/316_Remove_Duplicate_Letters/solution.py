#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

	1 <= s.length <= 104
	s consists of lowercase English letters.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
from functools import lru_cache
from heapq import heappop
from heapq import heappush
from collections import Counter
from collections import defaultdict
import operator
import sys
import pytest


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """06/17/2020 23:42"""
        def binsearch(s, c):
            i, j = 0, len(s)-1
            while i <= j:
                m = i + (j-i)//2
                if c <= s[m]:
                    j = m - 1
                else:
                    i = m + 1
            return i

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

    def removeDuplicateLetters(self, s: str) -> str:
        """06/17/2020 23:53"""
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

    def removeDuplicateLetters(self, s: str) -> str:
        """Memory limit exceeded"""
        offset = ord('a')

        @lru_cache(None)
        def dfs(i, remain):
            if remain == 0:
                return ''
            if i == len(s):
                return None
            bit = 1<<(ord(s[i]) - offset)
            ret = ''
            sub1 = dfs(i+1, remain)
            if sub1 is not None:
                ret = sub1
            if remain & bit:
                sub2 = dfs(i+1, remain ^ bit)
                if sub2 is not None:
                    if not ret:
                        ret = s[i] + sub2
                    else:
                        ret = min(ret, s[i] + sub2)
            return ret if ret else None

        remain = 0
        for c in s:
            remain |= 1<<(ord(c)-offset)
        return dfs(0, remain)

    def removeDuplicateLetters(self, s: str) -> str:
        def bit(c):
            return 1<<(ord(c) - ord('a'))

        ret = []
        cnt = Counter(s)
        remain = 0
        for c in cnt:
            remain |= bit(c)
        for c in s:
            cnt[c] -= 1
            if remain & bit(c) == 0:
                continue
            while ret and ret[-1] > c and cnt.get(ret[-1], 0) > 0:
                remain |= bit(ret.pop())
            ret.append(c)
            remain ^= bit(c)
        return ''.join(ret)


@pytest.mark.parametrize('s, expected', [
    ("bcabc", "abc"),
    ("cbacdcbc", "acdb"),
    ("bbbacacca", 'bac'),
    ("bccab", 'bca'),
    ("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws", 'bfegkuyjorndiqszpcaw')
])
def test(s, expected):
    assert expected == Solution().removeDuplicateLetters(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
