#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

	m == s.length
	n == t.length
	1 <= m, n <= 105
	s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
import sys
from collections import defaultdict
from collections import Counter
import pytest


class Solution:
    def minWindow(self, s, t):
        """08/11/2018 06:20"""
        if not s or not t:
            return ""
        if len(t) == 1:
            return t if t in s else ""

        cleared = set()
        chars = Counter(t)
        cnt = defaultdict(int)

        def found( c):
            cnt[c] += 1
            if cnt[c] >= chars[c]:
                cleared.add(c)

        def pop( c):
            cnt[c] -= 1
            if cnt[c] < chars[c]:
                cleared.pop(c)

        l = 0
        while l < len(s) and s[l] not in chars:
            l += 1
        if l == len(s):
            return ""

        found(s[l])

        r = l+1
        if r == len(s):
            return ""
        ret = s
        while r < len(s):
            if s[r] in chars:
                found(s[r])
                if s[r] == s[l] and cnt[s[r]] > chars[s[r]]:
                    pop(s[l])
                    l += 1
                    while l < r:
                        if s[l] in chars:
                            if cnt[s[l]] > chars[s[l]]:
                                pop(s[l])
                            else:
                                break
                        l += 1
                if len(cleared) == len(chars):
                    ret = min(ret, s[l:r+1], key=len)
            r += 1
        if len(cleared) == len(chars):
            return ret
        else:
            return ""

    def minWindow(self, s, t):
        """08/13/2018 04:21"""
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        n_chars = len(t)
        l, r = 0, 0
        length = float('inf')
        start = 0

        while r < len(s):
            if s[r] in cnt:
                if cnt[s[r]] > 0:
                    n_chars -= 1
                cnt[s[r]] -= 1
            while n_chars <= 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l
                if s[l] in cnt:
                    cnt[s[l]] += 1
                    if cnt[s[l]] > 0:
                        n_chars += 1
                l += 1
            r += 1
        return s[start:start+length] if length < float('inf') else ''

    def minWindow(self, s: str, t: str) -> str:
        """
        Time complexity: O(n+m)
        Space complexity: O(m)
        """
        chars = set(t)
        cnt = Counter(t)
        i = 0
        j = 0
        ret = ' ' * (len(s) + 1)
        while j < len(s):
            if s[j] in cnt:
                cnt[s[j]] -= 1
                if cnt[s[j]] == 0:
                    chars.remove(s[j])
            while i <= j and not chars:
                if j-i+1 < len(ret):
                    ret = s[i:j+1]
                if s[i] in cnt:
                    cnt[s[i]] += 1
                    if cnt[s[i]] > 0:
                        chars.add(s[i])
                i += 1
            j += 1
        return ret.strip()


@pytest.mark.parametrize('s, t, expected', [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("bba", "ab", "ba")
])
def test(s, t, expected):
    assert expected == Solution().minWindow(s, t)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
