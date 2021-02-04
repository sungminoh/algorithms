#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation:
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.

Note:

	1 <= S.length = shifts.length <= 20000
	0 <= shifts[i] <= 10 ^ 9
"""
import sys
from typing import List
import pytest


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
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


@pytest.mark.parametrize('S, shifts, expected', [
("abc", [3,5,9], "rpl"),

])
def test(S, shifts, expected):
    assert expected == Solution().shiftingLetters(S, shifts)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
