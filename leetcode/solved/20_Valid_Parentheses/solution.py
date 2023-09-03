#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

	1 <= s.length <= 104
	s consists of parentheses only '()[]{}'.
"""
import pytest
import sys


class Solution:
    def isValid(self, s: str) -> bool:
        """Mar 27, 2022 15:00"""
        counter = dict(zip(')}]', '({['))
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != counter[c]:
                    return False
                stack.pop()
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        """Sep 02, 2023 17:20"""
        def match(a, b):
            return (a == '{' and b == '}')\
                or (a == '(' and b == ')')\
                or (a == '[' and b == ']')

        stack = []
        for c in s:
            if c in '})]':
                if stack and match(stack[-1], c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


@pytest.mark.parametrize('args', [
    (("()", True)),
    (("()[]{}", True)),
    (("(]", False)),
])
def test(args):
    assert args[-1] == Solution().isValid(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
