#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

	"AAJF" with the grouping (1 1 10 6)
	"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:

	1 <= s.length <= 100
	s contains only digits and may contain leading zero(s).
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    @lru_cache(None)
    def numDecodings(self, s):
        """05/05/2018 01:30"""
        memo = {}
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return 1
        if int(s[0]) == 0:
            return 0
        n = self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            n += self.numDecodings(s[2:])
        memo[s] = n
        return n

    def numDecodings(self, s: str) -> int:
        """08/24/2021 10:37
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not s:
            return 0
        if not '1' <= s[0] <= '9':
            return 0
        if len(s) == 1:
            return 1
        if s[1] == '0' and not s[0] in '12':
            return 0
        dp = [0]*2
        dp[0] = 1
        dp[1] = 1 if s[1] == '0' else \
            2 if '10' <= s[:2] <= '26' else 1
        for i in range(2, len(s)):
            if not '10' <= s[i-1:i+1] <= '26':
                dp[i%2] = 0
            if '1' <= s[i] <= '9':
                dp[i%2] += dp[(i-1)%2]
        return dp[(len(s)-1)%2]

    def numDecodings(self, s: str) -> int:
        """10/16/2022 16:44"""
        @lru_cache(None)
        def decode(i):
            if i == len(s):
                return 1
            ret = 0
            if 1 <= int(s[i]) <= 9:
                ret += decode(i+1)
            if 10 <= int(s[i:min(len(s), i+2)]) <= 26:
                ret += decode(i+2)
            return ret

        return decode(0)


@pytest.mark.parametrize('s, expected', [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("06", 0),
    ("27", 1),
    ("2611055971756562", 4),
])
def test(s, expected):
    assert expected == Solution().numDecodings(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
