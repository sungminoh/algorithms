
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:

Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
    1. The input strings will not have extra blank.
    2. The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""
import sys
import pytest
import re


class Solution:
    pattern = re.compile('(-?\d+)\+(-?\d+)i')
    def complexNumberMultiply(self, a: str, b: str) -> str:
        r1, c1 = map(int, self.pattern.match(a).groups())
        r2, c2 = map(int, self.pattern.match(b).groups())
        r = (r1 * r2) - (c1 * c2)
        c = (r1 * c2) + (r2 * c1)
        return f'{r}+{c}i'



@pytest.mark.parametrize('a, b, expected', [
    ('1+1i', '1+1i', '0+2i'),
    ('1+-1i', '1+-1i', '0+-2i'),
])
def test(a, b, expected):
    assert expected == Solution().complexNumberMultiply(a, b)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
