#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:

	1 <= s.length <= 500
	s consists of only lowercase English letters.
"""
import sys
import pytest


class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        ret = 0
        i = 0
        pre = s[i]
        j = 1
        while j < len(s):
            cur = s[j]
            if cur != pre:
                pre = cur
                ret = max(ret, j-i)
                i = j
            j += 1
        ret = max(ret, j-i)
        return ret


@pytest.mark.parametrize('s, expected', [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
])
def test(s, expected):
    assert expected == Solution().maxPower(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
