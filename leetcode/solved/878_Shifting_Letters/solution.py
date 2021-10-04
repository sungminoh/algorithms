#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

	For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

Constraints:

	1 <= s.length <= 105
	s consists of lowercase English letters.
	shifts.length == s.length
	0 <= shifts[i] <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        """01/16/2021 17:13"""
        def to_int(c):
            return ord(c) - ord('a')

        def to_char(i):
            return chr(i + ord('a'))

        ret = [None] * len(S)
        acc = 0
        for i in range(len(shifts)-1, -1, -1):
            shift = shifts[i]
            acc += shift
            ret[i] = to_char((to_int(S[i]) + acc) % 26)

        return ''.join(ret)

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        offset = ord('a')
        ret = ''
        total_shift = 0
        for i, shift in enumerate(reversed(shifts)):
            total_shift += shift
            ret = chr(offset + (ord(s[len(s)-1-i]) - offset + total_shift) % 26) + ret
        return ret


@pytest.mark.parametrize('s, shifts, expected', [
    ("abc", [3,5,9], "rpl"),
    ("aaa", [1,2,3], "gfd"),
])
def test(s, shifts, expected):
    assert expected == Solution().shiftingLetters(s, shifts)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
