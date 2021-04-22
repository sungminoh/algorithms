#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

Constraints:

	0 <= s.length <= 3 * 104
	s[i] is '(', or ')'.
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        @lru_cache(None)
        def rec(i, j):
            if i < 0 or j >= len(s) or (j-i+1)%2:
                return False
            if i >= j:
                return True
            if i +1 == j:
                return s[i] == '(' and s[j] == ')'
            ret = rec(i+1, j-1) and s[i] == '(' and s[j] == ')'
            for k in range(i+1, j-1, 2):
                ret |= rec(i, k) and rec(k+1, j)
            return ret
        ret = 0
        for i in range(len(s)):
            for j in range(i+1, len(s), 2):
                if rec(i, j):
                    ret = max(ret, j-i+1)
        return ret

    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        m = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                v = 0
                while stack and isinstance(stack[-1], int):
                    v += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                    v += 1
                    while stack and isinstance(stack[-1], int):
                        v += stack.pop()
                    stack.append(v)
                    m = max(m, v)
                else:
                    stack = []
        return m*2

    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Optimized space. Negative value in the stack means the number of open
        parenthesis. Positive value in the stack means the number of valid
        pairs
        """
        m = 0
        stack = []
        for c in s:
            if c == '(':
                opens = -1
                if stack and stack[-1] < 0:
                    opens += stack.pop()
                stack.append(opens)
            else:
                v = 0
                if stack and stack[-1] > 0:
                    v += stack.pop()
                if stack and stack[-1] < 0:
                    stack[-1] += 1
                    if stack[-1] == 0:
                        stack.pop()
                    v += 1
                    if stack and stack[-1] > 0:
                        v += stack.pop()
                    stack.append(v)
                    m = max(m, v)
                else:
                    stack = []
        return m*2

    def longestValidParentheses(self, s: str) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Optimized space. Negative value in the stack means the number of open
        parenthesis. Positive value in the stack means the number of valid
        pairs.
        Refactor some subroutines.
        """
        def was_open():
            return stack and stack[-1] < 0

        def add_open():
            if was_open():
                stack[-1] -= 1
            else:
                stack.append(-1)

        def was_valid():
            return stack and stack[-1] > 0

        def get_prev_valid_size():
            return stack.pop() if was_valid() else 0

        def close():
            stack[-1] += 1
            if stack[-1] == 0:
                stack.pop()

        m = 0
        stack = []
        for c in s:
            if c == '(':
                add_open()
            else:
                v = get_prev_valid_size()
                if was_open():
                    close()
                    v += get_prev_valid_size() + 1
                    # upate
                    stack.append(v)
                    m = max(m, v)
                else:
                    # reset
                    stack = []
        return m*2


@pytest.mark.parametrize('s, expected', [
    ("(()", 2),
    (")()())", 4),
    ("", 0),
    ("()(()", 2),
    ("((((",0),
    ("))))",0),
    ("(((()))))((((()))))",10),
    ("((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))", 168)
])
def test(s, expected):
    ()
    assert expected == Solution().longestValidParentheses(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
