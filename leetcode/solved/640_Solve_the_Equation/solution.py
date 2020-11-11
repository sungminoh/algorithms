#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: "x=x"
Output: "Infinite solutions"

Example 3:

Input: "2x=x"
Output: "x=0"

Example 4:

Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:

Input: "x=x+2"
Output: "No solution"
"""
import sys
import pytest


def calc(equation):
    x = 0
    n = 0
    sign = 1
    num = 0
    for i, c in enumerate(equation):
        if c in '+-':
            n += sign*num
            num = 0
            sign = 1 if c == '+' else -1
        elif c == 'x':
            if i == 0 or (i > 0 and equation[i-1] in '+-'):
                x += sign
            else:
                x += sign*num
            num = 0
        else:
            num *= 10
            num += int(c)
    n += sign*num
    return x, n


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right =equation.split('=')
        lx, ln = calc(left)
        rx, rn = calc(right)
        x = lx - rx
        n = rn - ln
        print(lx, ln, rx, rn)
        if x == 0:
            return 'No solution' if n != 0 else 'Infinite solutions'
        else:
            return f'x={n//x}'


@pytest.mark.parametrize('equation, expected', [
    ("x+5-3+x=6+x-2", "x=2"),
    ("x=x", "Infinite solutions"),
    ("2x=x", "x=0"),
    ("2x+3x-6x=x+2", "x=-1"),
    ("x=x+2", "No solution"),
    ("-x=1","x=-1"),
    ("0x=0", "Infinite solutions")
])
def test(equation, expected):
    assert expected == Solution().solveEquation(equation)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
