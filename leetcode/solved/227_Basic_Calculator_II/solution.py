#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:

	1 <= s.length <= 3 * 105
	s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
	s represents a valid expression.
	All the integers in the expression are non-negative integers in the range [0, 231 - 1].
	The answer is guaranteed to fit in a 32-bit integer.
"""
import sys
import pytest


class Solution:
    def calculate(self, s: str) -> int:
        class Cursor():
            def __init__(self, idx, s):
                self.idx = idx
                self.s = s

            def plus(self):
                self.idx+= 1

            def char(self):
                return self.s[self.idx]

            def is_end(self):
                return self.idx >= len(self.s)

            def remove_spaces(self):
                while not self.is_end() and self.char() == ' ':
                    self.plus()

            def get_next(self):
                self.remove_spaces()
                if self.is_end():
                    return None
                if not ('0' <= self.char() <= '9'):
                    ret = self.char()
                    self.plus()
                    return ret
                else:
                    start = self.idx
                    while not self.is_end() and '0' <= self.char() <= '9':
                        self.plus()
                    return int(self.s[start:self.idx])

        nums = []
        ops = []
        cur = Cursor(0, s)
        while not cur.is_end():
            v = cur.get_next()
            if v is None:
                break
            elif isinstance(v, int):
                nums.append(v)
            elif v == '/':
                nums.append(nums.pop() // cur.get_next())
            elif v == '*':
                nums.append(nums.pop() * cur.get_next())
            else:
                ops.append(v)
        while ops:
            if ops.pop(0) == '+':
                nums.insert(0, nums.pop(0) + nums.pop(0))
            else:
                n1, n2 = nums.pop(0), nums.pop(0)
                nums.insert(0, n1 - n2)
        return nums[0]

    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[j:i])
                if stack and stack[-1] in '/*':
                    o = stack.pop()
                    if o == '/':
                        stack.append(stack.pop() // num)
                    elif o == '*':
                        stack.append(stack.pop() * num)
                else:
                    stack.append(num)
            elif s[i] in '/*+-':
                stack.append(s[i])
                i += 1
            else:
                i += 1

        ret = 0
        op = '+'
        i = 0
        for c in stack:
            if c == '+':
                op = '+'
            elif c == '-':
                op = '-'
            else:
                if op == '+':
                    ret += c
                elif op == '-':
                    ret -= c
                else:
                    assert Exception('Not reachable')
        return ret


@pytest.mark.parametrize('s, expected', [
    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5),
    ("42", 42),
    ("0-2147483647", -2147483647),
    ("1-1+1", 1),
    ("1+1-1", 1),
])
def test(s, expected):
    assert expected == Solution().calculate(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
