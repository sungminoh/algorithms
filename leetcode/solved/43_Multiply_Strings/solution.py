#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

	1 <= num1.length, num2.length <= 200
	num1 and num2 consist of digits only.
	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
import sys
import itertools
import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        def mul(num, digit):
            d = int(digit)
            ret = ''
            c = 0
            for a in reversed(num):
                c, n = divmod(int(a)*d + c, 10)
                ret += str(n)
            if c:
                ret += str(c)
            return ret[::-1]

        def plus(num1, num2):
            ret = ''
            c = 0
            for a, b in itertools.zip_longest(reversed(num1), reversed(num2)):
                a = a or '0'
                b = b or '0'
                c, n = divmod(int(a)+int(b)+c, 10)
                ret += str(n)
            if c:
                ret += str(c)
            return ret[::-1]

        ret = '0'
        for i, d in enumerate(reversed(num2)):
            ret = plus(ret, mul(num1, d) + '0'*i)

        return ret


@pytest.mark.parametrize('num1, num2, expected', [
    ("2", "3", "6"),
    ("123", "456", "56088"),
])
def test(num1, num2, expected):
    assert expected == Solution().multiply(num1, num2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
