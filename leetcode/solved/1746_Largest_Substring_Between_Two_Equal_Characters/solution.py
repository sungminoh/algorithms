#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Constraints:

	1 <= s.length <= 300
	s contains only lowercase English letters.
"""
import pytest
import sys


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """Jan 24, 2024 19:44"""
        ret = -1
        pos = {}
        for i, c in enumerate(s):
            ret = max(ret, i - pos.setdefault(c, i) - 1)
        return ret


@pytest.mark.parametrize('args', [
    (("aa", 0)),
    (("abca", 2)),
    (("cbzxy", -1)),
])
def test(args):
    assert args[-1] == Solution().maxLengthBetweenEqualCharacters(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
