#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.
"""
import sys
from collections import defaultdict
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s):
        """12/28/2017 20:22"""
        if s == '':
            return 0
        cnt = {c: 0 for c in s}
        cnt[s[0]] = 1
        size = 1
        j = 0
        fi = fj = 0
        for i in range(1, len(s)):
            cnt[s[i]] += 1
            while cnt[s[i]] > 1:
                cnt[s[j]] -= 1
                j += 1
            if i - j + 1 > size:
                size = i - j + 1
                fi = i
                fj = j
        # s[fj:fi+1]
        return size

    def lengthOfLongestSubstring(self, s: str) -> int:
        """06/18/2022 16:16"""
        i = 0
        cnt = defaultdict(int)
        ret = 0
        for j, c in enumerate(s):
            cnt[c] += 1
            while i < j and cnt[c] > 1:
                cnt[s[i]] -= 1
                i += 1
            ret = max(ret, j-i+1)
        return ret


@pytest.mark.parametrize('s, expected', [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
])
def test(s, expected):
    assert expected == Solution().lengthOfLongestSubstring(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
