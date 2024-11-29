#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"

Constraints:

	The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
	Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
	The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
	The number of given fractions will be in the range [1, 10].
	The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""
import pytest
import sys


class Solution:
    def fractionAddition(self, expression: str) -> str:
        def extract_next_num(i):
            sign = 1
            if expression[i] == '+':
                sign = 1
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '/':
                assert False
            n = ''
            while i < len(expression) and expression[i].isdigit():
                n += expression[i]
                i += 1
            if expression[i] != '/':
                return i, (sign * int(n), 1)
            i += 1
            d = ''
            while i < len(expression) and expression[i].isdigit():
                d += expression[i]
                i += 1
            return i, (sign * int(n), int(d))

        @lru_cache(None)
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if b == 0:
                return a
            if a % b == 0:
                return b
            return gcd(a - b, b)

        queue = []
        i = 0
        while i < len(expression):
            i, (n, d) = extract_next_num(i)
            queue.append((n, d))
        nominator, denominator = 0, 1
        for n, d in queue:
            nominator = nominator * d + n * denominator
            denominator = denominator * d

        common_divider = gcd(abs(nominator), denominator)
        return f'{nominator // common_divider}/{denominator // common_divider}'

    def fractionAddition(self, expression: str) -> str:
        """Nov 13, 2024 08:13"""
        N = len(expression)

        def gcd(a, b):
            a = abs(a)
            b = abs(b)
            if a > b:
                return gcd(b, a)
            if b % a == 0:
                return a
            return gcd(b%a, a)

        def trim(tup):
            if tup[0] == 0:
                return (0, 1)
            g = gcd(tup[0], tup[1])
            return (tup[0]//g, tup[1]//g)

        def add(tup1, tup2):
            (bp, bq) = tup1
            (ap, aq) = tup2
            return trim(((bp*aq) + (bq*ap), bq*aq))

        cur = 0
        i = 0
        sign = 1
        operands = []
        operator = None
        while i < N:
            c = expression[i]
            if c.isdigit():
                cur *= 10
                cur += int(c)
            else:
                operands.append((sign * cur, 1))
                cur = 0
                sign = -1 if c == '-' else 1
                if operator == '/':
                    (bp, bq) = operands.pop()
                    (ap, aq) = operands.pop()
                    operands.append(trim((ap*bq, bp*aq)))
                operator = c
            i += 1
        operands.append((sign * cur, 1))
        if operator == '/':
            (bp, bq) = operands.pop()
            (ap, aq) = operands.pop()
            operands.append(trim((ap*bq, bp*aq)))

        ret = operands[0]
        for i in range(1, len(operands)):
            ret = add(ret, operands[i])
        return '/'.join(map(str, ret))


@pytest.mark.parametrize('args', [
    (("-1/2+1/2", "0/1")),
    (("-1/2+1/2+1/3", "1/3")),
    (("1/3-1/2", "-1/6")),
])
def test(args):
    assert args[-1] == Solution().fractionAddition(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
