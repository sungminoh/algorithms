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
import sys
import pytest


class Solution:
    def isValid(self, s: str) -> bool:
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


@pytest.mark.parametrize('s, expected', [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
])
def test(s, expected):
    assert expected == Solution().isValid(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
