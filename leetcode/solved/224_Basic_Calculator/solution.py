#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:

	1 <= s.length <= 3 * 105
	s consists of digits, '+', '-', '(', ')', and ' '.
	s represents a valid expression.
	'+' is not used as a unary operation.
	'-' could be used as a unary operation and in this case, it will not be used directly after a +ve or -ve signs (will be inside parentheses).
	There will be no two consecutive operators in the input.
	Every number and running calculation will fit in a signed 32-bit integer.
"""
import sys
import pytest


class Solution:
    def calculate(self, s: str) -> int:
        """06/14/2020 14:40"""
        def process_stack(stack):
            operand = []
            operator = []
            while True:
                if not stack:
                    break
                if stack[-1] == '(':
                    stack.pop()
                    break
                elif isinstance(stack[-1], int):
                    operand.append(stack.pop())
                else:
                    operator.append(stack.pop())
            while operator:
                n1 = operand.pop()
                n2 = operand.pop()
                op = operator.pop()
                operand.append((n1 + n2) if op == '+' else (n1 - n2))
            stack.append(operand[0])

        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':
                pass
            elif c in '(+-':
                stack.append(c)
            elif c == ')':
                process_stack(stack)
            else:
                n = 0
                while i < len(s) and s[i].isdigit():
                    n *= 10
                    n += int(s[i])
                    i += 1
                stack.append(n)
                continue
            i += 1
        process_stack(stack)
        return stack[0]

    def calculate(self, s: str) -> int:
        def calc(stack):
            while len(stack)>=2:
                if not isinstance(stack[-2], str):
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                elif stack[-2] in '-+':
                    b = stack.pop()
                    stack.append(b if stack.pop() == '+' else -b)
                else:
                    break

        stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in '(+-':
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                c = stack.pop()
                stack.pop()
                stack.append(c)
                calc(stack)
                i += 1
            else:
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j
                calc(stack)
        return stack[0]


@pytest.mark.parametrize('s, expected', [
    ("1 + 1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
    ("2147483647", 2147483647),
    ("-2+ 1", -1),
    ("- (3 + (4 + 5))", -12)
])
def test(s, expected):
    assert expected == Solution().calculate(s)


if __name__ == '__main__':
    sys.exit(pytest.main(['-v', '-s', ] + sys.argv))
