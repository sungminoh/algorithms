#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

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
import sys
import operator
from typing import List
import pytest


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


@pytest.mark.parametrize('tokens, expected', [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
])
def test(tokens, expected):
    assert expected == Solution().evalRPN(tokens)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
