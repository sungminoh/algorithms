#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2

Constraints:

	2 <= s.length <= 50
	s consists of only '(' and ')'.
	s is a balanced parentheses string.
"""
import sys
import pytest


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def foo(i):
            ret = 0
            cnt = 0
            if s[i] == '(':
                subscore_sum = 0
                j = i
                while j < len(s) and s[j] != ')':
                    j, subscore = foo(j+1)
                    subscore_sum += subscore
                if j < len(s) and s[j] == ')':
                    subscore_sum *= 2
                ret += subscore_sum
                return j+1, ret
            else:
                return i+1, 1

        return foo(0)[1]

    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            elif c == ')':
                if stack[-1] == 0:
                    stack[-1] = 1
                else:
                    stack[-1] = stack.pop()*2
                sm = 0
                while len(stack)>1 and stack[-1] != 0:
                    sm += stack.pop()
                stack.append(sm)
        return sum(stack)

    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return sum(stack)


@pytest.mark.parametrize('s, expected', [
    ("()", 1),
    ("(())", 2),
    ("()()", 2),
])
def test(s, expected):
    assert expected == Solution().scoreOfParentheses(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
