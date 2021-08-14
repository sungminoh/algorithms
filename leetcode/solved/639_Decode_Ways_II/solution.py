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

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".

Example 2:

Input: s = "1*"
Output: 18
Explanation: The encoded message can represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19".
Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K").
Hence, there are a total of 9 * 2 = 18 ways to decode "1*".

Example 3:

Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".

Constraints:

	1 <= s.length <= 105
	s[i] is a digit or '*'.
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Recursion
        Time complexity: O(n)
        Space complexity: O(n)
        """
        MOD = int(1e9+7)

        @lru_cache(None)
        def rec(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if s[i] == '*':
                sub1 = 9*rec(i+1)
            else:
                sub1 = rec(i+1)

            sub2 = 0
            if i < len(s)-1:
                if s[i] == '1':
                    sub2 = (9 if s[i+1] == '*' else 1) * rec(i+2)
                elif s[i] == '2':
                    sub2 = (6 if s[i+1] == '*' \
                            else 1 if s[i+1] in '0123456' \
                            else 0) * rec(i+2)
                elif s[i] == '*':
                    sub2 = (15 if s[i+1] == '*' \
                            else 2 if s[i+1] in '0123456' \
                            else 1) * rec(i+2)
                else:
                    sub2 = 0
            return (sub1 + sub2) % MOD

        return rec(0)

    def numDecodings(self, s: str) -> int:
        """
        Bottom up
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not s:
            return 1
        MOD = int(1e9+7)
        ret = [1]
        if s[-1] == '*':
            ret.append(9)
        elif s[-1] == '0':
            ret.append(0)
        else:
            ret.append(1)
        for i in range(len(s)-2, -1, -1):
            a = s[i]
            b = s[i+1]
            if a == '*':
                sub1 = 9 * ret[-1]
            elif a == '0':
                sub1 = 0
            else:
                sub1 = ret[-1]
            if a == '1':
                sub2 = (9 if b == '*' else 1) * ret[-2]
            elif a == '2':
                sub2 = (6 if b == '*' \
                        else 1 if b in '0123456' \
                        else 0) * ret[-2]
            elif a == '*':
                sub2 = (15 if b == '*' \
                        else 2 if b in '0123456' \
                        else 1) * ret[-2]
            else:
                sub2 = 0
            ret.append((sub1 + sub2) % MOD)
            ret.pop(0)
        return ret[-1]


@pytest.mark.parametrize('s, expected', [
    ("*", 9),
    ("1*", 18),
    ("2*", 15),
    ("**", 96),
    ("2839", 1),
    ("621", 2),
    ("21", 2),
    ("*********", 291868912),
    ("*0**0", 36),
])
def test(s, expected):
    assert expected == Solution().numDecodings(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
