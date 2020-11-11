#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    class Cursor(object):
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

    def calculate(self, s: str) -> int:
        nums = []
        ops = []
        cur = self.Cursor(0, s)
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


if __name__ == "__main__":
    cases = [
        "3+2*2",
        " 3/2 ",
        " 3+5 / 2 ",
        "42",
        "0-2147483647",
        "1-1+1",
        "1+1-1"
    ]
    expecteds = [
        7,
        1,
        5,
        42,
        -2147483647,
        1,
        1
    ]
    for case, expected in zip(cases, expecteds):
        actual = Solution().calculate(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')

