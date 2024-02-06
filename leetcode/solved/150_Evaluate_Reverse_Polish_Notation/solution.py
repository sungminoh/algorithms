from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

	The valid operators are '+', '-', '*', and '/'.
	Each operand may be an integer or another expression.
	The division between two integers always truncates toward zero.
	There will not be any division by zero.
	The input represents a valid arithmetic expression in a reverse polish notation.
	The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

	1 <= tokens.length <= 104
	tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
import pytest
import sys


class Solution:
    def evalRPN(self, tokens):
        """07/28/2018 11:05	"""
        stack = []
        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + t + b))))
            else:
                stack.append(t)
        return int(stack.pop())

    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: (abs(x)//abs(y)) * (1 if x*y > 0 else -1)
        }
        stack = []
        while tokens:
            t = tokens.pop()
            stack.append(int(t) if t[1 if t.startswith('-') else 0:].isdigit() else t)
            while len(stack) >= 3 \
                    and isinstance(stack[-1], int) \
                    and isinstance(stack[-2], int):
                a = stack.pop()
                b = stack.pop()
                o = stack.pop()
                stack.append(operators[o](a, b))
        return stack[-1]

    def evalRPN(self, tokens: List[str]) -> int:
        """Feb 19, 2023 15:38"""
        s = []
        for t in tokens:
            if t not in '+-*/':
                s.append(int(t))
                continue
            b = s.pop()
            a = s.pop()
            if t == '+':
                s.append(a + b)
            elif t == '-':
                s.append(a - b)
            elif t == '*':
                s.append(a * b)
            elif t == '/':
                sign = -1 if a*b < -1 else 1
                s.append(sign * int(abs(a / b)))
        return s[0]

    def evalRPN(self, tokens: List[str]) -> int:
        """Feb 05, 2024 21:40"""
        stack = []
        for t in tokens:
            if t in '+-*/':
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a + b)
                if t == '-':
                    stack.append(a - b)
                if t == '*':
                    stack.append(a * b)
                if t == '/':
                    stack.append((1 if a*b>0 else -1) * (abs(a) // abs(b)))
            else:
                stack.append(int(t))
        return stack.pop()


@pytest.mark.parametrize('args', [
    ((["2","1","+","3","*"], 9)),
    ((["4","13","5","/","+"], 6)),
    ((["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)),
    ((["18"], 18)),
])
def test(args):
    assert args[-1] == Solution().evalRPN(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
