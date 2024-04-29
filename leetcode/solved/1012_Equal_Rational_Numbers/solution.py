#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings s and t, each of which represents a non-negative rational number, return true if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

A rational number can be represented using up to three parts: , , and a . The number will be represented in one of the following three ways:

		For example, 12, 0, and 123.

		For example, 0.5, 1., 2.12, and 123.0001.

		For example, 0.1(6), 1.(9), 123.00(1212).

The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example:

	1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66).

Example 1:

Input: s = "0.(52)", t = "0.5(25)"
Output: true
Explanation: Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.

Example 2:

Input: s = "0.1666(6)", t = "0.166(66)"
Output: true

Example 3:

Input: s = "0.9(9)", t = "1."
Output: true
Explanation: "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".

Constraints:

	Each part consists only of digits.
	The  does not have leading zeros (except for the zero itself).
	1 <= .length <= 4
	0 <= .length <= 4
	1 <= .length <= 4
"""
import pytest
import sys


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        """Apr 28, 2024 17:45"""
        def gcd(a, b):
            if b > a:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(a%b, b)

        def reduce(a):
            if a[0] == 0:
                return (0, 1)
            g = gcd(a[0], a[1])
            return (a[0]//g, a[1]//g)

        def add(a, b):
            return reduce((a[0]*b[1] + b[0]*a[1], a[1]*b[1]))

        def to_rational(s):
            idx = s.find('(')
            if idx < 0:
                dot_idx = s.find('.')
                if dot_idx < 0:
                    return (int(s), 1)
                else:
                    integer_part = int(s[:dot_idx])
                    p = pow(10, len(s)-1 - dot_idx)
                    decimal_part = int(s[dot_idx+1:]) if p > 1 else 0
                    return reduce((integer_part * p + decimal_part, p))
            else:
                base = to_rational(s[:idx])
                p = pow(10, len(s)-3 - s.find('.'))
                a = int(s[idx+1:-1])
                b = pow(10, len(s)-idx-2)
                ss = (a*b, p*(b-1))
                return add(base, ss)

        sr = to_rational(s)
        tr = to_rational(t)
        return sr == tr


@pytest.mark.parametrize('args', [
    (("0.(52)", "0.5(25)", True)),
    (("0.1666(6)", "0.166(66)", True)),
    (("0.9(9)", "1.", True)),
])
def test(args):
    assert args[-1] == Solution().isRationalEqual(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
