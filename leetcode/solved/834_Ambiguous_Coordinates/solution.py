#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.

	For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".

Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:

Input: s = "(123)"
Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]

Example 2:

Input: s = "(0123)"
Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
Explanation: 0.0, 00, 0001 or 00.01 are not allowed.

Example 3:

Input: s = "(00011)"
Output: ["(0, 0.011)","(0.001, 1)"]

Example 4:

Input: s = "(100)"
Output: ["(10, 0)"]
Explanation: 1.0 is not allowed.

Constraints:

	4 <= s.length <= 12
	s[0] == '(' and s[s.length - 1] == ')'.
	The rest of s are digits.
"""
import sys
from typing import List
import pytest



class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        """05/26/2020 06:51"""
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

        S = S[1:len(S) - 1]

        ret = []
        for i in range(1, len(S)):
            a, b = S[:i], S[i:]
            for x in gen(a):
                for y in gen(b):
                    ret.append("(" + x + ", " + y + ")")
        return ret


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        def is_valid_digit(digit):
            if len(digit) == 1:
                return True
            return digit[0] != '0'

        def is_valid_decimal(decimal):
            return len(decimal) == 0 or decimal[-1] != '0'

        def possibles(s):
            for i in range(1, len(s)+1):
                digit = s[:i]
                decimal = s[i:]
                if is_valid_digit(digit) and is_valid_decimal(decimal):
                    dg = ''.join(digit)
                    dc = ''.join(decimal)
                    if dc:
                        yield f'{dg}.{dc}'
                    else:
                        yield dg

        head = []
        tail = list(s[1:-1])
        ret = set()
        for i in range(len(s)-2):
            head.append(tail.pop(0))
            for a in possibles(head):
                for b in possibles(tail):
                    ret.add(f'({a}, {b})')
        return list(ret)


@pytest.mark.parametrize('s, expected', [
    ("(123)", ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]),
    ("(0123)", ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]),
    ("(00011)", ["(0, 0.011)","(0.001, 1)"]),
    ("(100)", ["(10, 0)"]),
])
def test(s, expected):
    assert set(expected) == set(Solution().ambiguousCoordinates(s))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
