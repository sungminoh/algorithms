#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

	1 <= num1.length, num2.length <= 104
	num1 and num2 consist of only digits.
	num1 and num2 don't have any leading zeros except for the zero itself.
"""
import sys
import itertools
import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        ret = ''
        offset = ord('0')
        for a, b in itertools.zip_longest(reversed(num1), reversed(num2)):
            a = 0 if a is None else (ord(a) - offset)
            b = 0 if b is None else (ord(b) - offset)
            n = (a+b+c) if a+b+c < 10 else (a+b+c-10)
            ret += str(n)
            c = 1 if a+b+c >= 10 else 0
        if c > 0:
            ret += str(c)
        return ret[::-1]


@pytest.mark.parametrize('num1, num2, expected', [
    ("11", "123", "134"),
    ("456", "77", "533"),
    ("0", "0", "0"),
    ("1", "9", "10"),
])
def test(num1, num2, expected):
    assert expected == Solution().addStrings(num1, num2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
