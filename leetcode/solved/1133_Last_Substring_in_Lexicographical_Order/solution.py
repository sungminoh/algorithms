#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the last substring of s in lexicographical order.

Example 1:

Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:

Input: s = "leetcode"
Output: "tcode"

Constraints:

	1 <= s.length <= 4 * 105
	s contains only lowercase English letters.
"""
import pytest
import sys


class Solution:
    def lastSubstring(self, s: str) -> str:
        """May 04, 2024 17:40"""
        ret = ''
        acc = ''
        for i in range(len(s)-1, -1, -1):
            acc = s[i] + acc
            if acc > ret:
                ret = acc
        return ret


@pytest.mark.parametrize('args', [
    (("abab", "bab")),
    (("leetcode", "tcode")),
])
def test(args):
    assert args[-1] == Solution().lastSubstring(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
