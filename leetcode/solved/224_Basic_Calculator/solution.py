
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:

	You may assume that the given expression is always valid.
	Do not use the eval built-in library function.
"""
import sys
import pytest


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


class Solution:
    def calculate(self, s: str) -> int:
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


@pytest.mark.parametrize('s, expected', [
    ("1 + 1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
])
def test(s, expected):
    print()
    assert expected == Solution().calculate(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
