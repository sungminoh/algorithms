#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        stack = []
        mx = 0
        for c in s:
            # print(stack)
            if c == ')':
                if stack:
                    prev = 0
                    while stack and stack[-1] != '(':
                        prev += stack.pop()
                    if not stack:
                        stack = []
                        continue
                    else:
                        stack.pop()
                        prev += 2
                        while stack and stack[-1] != '(':
                            prev += stack.pop()
                        stack.append(prev)
                        mx = max(mx, prev)
            elif c == '(':
                stack.append(c)
        return mx


def main():
    s = input()
    print(Solution().longestValidParentheses(s))


if __name__ == '__main__':
    main()
