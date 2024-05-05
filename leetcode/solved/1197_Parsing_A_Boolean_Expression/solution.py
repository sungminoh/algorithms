#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

	't' that evaluates to true.
	'f' that evaluates to false.
	'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
	'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
	'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation:
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation:
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

Constraints:

	1 <= expression.length <= 2 * 104
	expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
"""
import pytest
import sys


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """May 04, 2024 16:04"""
        stack = [[]]
        i = 0
        while i < len(expression):
            c = expression[i]
            if c in '!&|':
                stack.append(c)
            elif c == '(':
                stack.append([])
            elif c == ')':
                operands = stack.pop()
                operator = stack.pop()
                if operator == '!':
                    assert len(operands) == 1
                    stack[-1].append(True ^ operands[0])
                if operator == '&':
                    stack[-1].append(all(operands))
                if operator == '|':
                    stack[-1].append(any(operands))
            elif c in 'tf':
                stack[-1].append(c == 't')
            i += 1
        return stack[0][0]


@pytest.mark.parametrize('args', [
    (("&(|(f))", False)),
    (("|(f,f,f,t)", True)),
    (("!(&(f,t))", True)),
    (("&(t,t,t)", True)),
])
def test(args):
    assert args[-1] == Solution().parseBoolExpr(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
