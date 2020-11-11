
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.

Note:
	4 <= S.length <= 12
	S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
"""
import sys
from typing import List
import pytest


def gen(s):
    if s == '0':
        yield s
    if not s.startswith('0') and not s.endswith('0'):
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            yield a + '.' + b
        yield s
    elif s.startswith('0') and not s.endswith('0'):
        yield s[0] + '.' + s[1:]
    elif not s.startswith('0') and s.endswith('0'):
        yield s


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        S = S[1:len(S) - 1]

        ret = []
        for i in range(1, len(S)):
            a, b = S[:i], S[i:]
            for x in gen(a):
                for y in gen(b):
                    ret.append("(" + x + ", " + y + ")")
        return ret


@pytest.mark.parametrize('S, expected', [
    ("(123)", ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]),
    ("(00011)", ["(0.001, 1)", "(0, 0.011)"]),
    ("(0123)", ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"])
])
def test(S, expected):
    assert set(expected) == set(Solution().ambiguousCoordinates(S))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
