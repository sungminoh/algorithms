#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A complex number can be represented as a string on the form "real+imaginaryi" where:

	real is the real part and is an integer in the range [-100, 100].
	imaginary is the imaginary part and is an integer in the range [-100, 100].
	i2 == -1.

Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Constraints:

	num1 and num2 are valid complex numbers.
"""
import re
import sys
import pytest


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        """06/03/2020 02:11"""
        pattern = re.compile('(-?\d+)\+(-?\d+)i')
        r1, c1 = map(int, pattern.match(a).groups())
        r2, c2 = map(int, pattern.match(b).groups())
        r = (r1 * r2) - (c1 * c2)
        c = (r1 * c2) + (r2 * c1)
        return f'{r}+{c}i'

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1[:-1].split('+')
        c, d = num2[:-1].split('+')
        x = (int(a)*int(c)) - (int(b)*int(d))
        y = (int(a)*int(d)) + (int(b)*int(c))
        return f'{x}+{y}i'


@pytest.mark.parametrize('num1, num2, expected', [
    ("1+1i", "1+1i", "0+2i"),
    ("1+-1i", "1+-1i", "0+-2i"),
])
def test(num1, num2, expected):
    assert expected == Solution().complexNumberMultiply(num1, num2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
