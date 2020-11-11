#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:

Input: s = "abc"
Output: 1

Constraints:

	3 <= s.length <= 5 x 10^4
	s only consists of a, b or c characters.
"""
import sys
from collections import defaultdict
import pytest


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        d = defaultdict(int)
        i = 0
        j = 0
        # abcabc
        while i < len(s):
            d[s[i]] += 1
            flag = False
            while len(d) == 3:
                flag = True
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    d.pop(s[j])
                j += 1
            if flag:
                j -= 1
                d[s[j]] += 1
            if len(d) == 3:
                cnt += j+1
            i += 1
        return cnt


@pytest.mark.parametrize('s, expected', [
    ('abcabc', 10),
    ('aaacb', 3),
    ('abc', 1),
])
def test(s, expected):
    assert expected == Solution().numberOfSubstrings(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
