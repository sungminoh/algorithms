#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

	1 <= a.length, b.length <= 104
	a and b consist only of '0' or '1' characters.
	Each string does not contain leading zeros except for the zero itself.
"""
import itertools
import pytest
import sys


class Solution:
    def addBinary(self, a, b):
        """12/30/2017 23:58"""
        return '{0:b}'.format(int(a, 2)+int(b, 2))

    def addBinary(self, a: str, b: str) -> str:
        """Jan 29, 2022 10:51"""
        ret = ''
        c = '0'
        for x, y in itertools.zip_longest(reversed(a), reversed(b)):
            n1 = len([i for i in [x, y, c] if i == '1'])
            if n1%2 == 0:
                ret += '0'
            else:
                ret += '1'
            if n1 >= 2:
                c = '1'
            else:
                c = '0'
        if c != '0':
            ret += c

        return ret[::-1]

    def addBinary(self, a: str, b: str) -> str:
        """Mar 20, 2023 23:16"""
        ret = []
        c = 0
        for x, y in itertools.zip_longest(reversed(a), reversed(b)):
            x = x or '0'
            y = y or '0'
            c, v = divmod(int(x) + int(y) + c, 2)
            ret.append(v)
        if c:
            ret.append(c)
        return ''.join(map(str, reversed(ret)))


@pytest.mark.parametrize('args', [
    (("11", "1", "100")),
    (("1010", "1011", "10101")),
])
def test(args):
    assert args[-1] == Solution().addBinary(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
