#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Constraints:

	0 <= c <= 231 - 1
"""
import pytest
import sys


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """12/15/2020 19:05"""
        i = 0
        while i <= c**0.5:
            r = (c - i**2) ** 0.5
            if int(r) == r:
                return True
            i += 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5)+1):
            r = (c-i**2)**0.5
            if r == int(r):
                return True
        return False

    def judgeSquareSum(self, c: int) -> bool:
        """Jun 25, 2024 18:07"""
        for i in range(int(pow(c, 0.5)), -1, -1):
            a = pow(i, 2)
            b = c - a
            if pow(int(pow(b, 0.5)), 2) == b:
                return True
        return False


@pytest.mark.parametrize('args', [
    ((5, True)),
    ((3, False)),
    ((4, True)),
    ((2, True)),
    ((1, True)),
    ((0, True)),
])
def test(args):
    assert args[-1] == Solution().judgeSquareSum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
