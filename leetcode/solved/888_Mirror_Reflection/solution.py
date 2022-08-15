#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Example 2:

Input: p = 3, q = 1
Output: 1

Constraints:

	1 <= q <= p <= 1000
"""
import sys
import pytest


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            if a > b:
                return gcd(b, a)
            if b%a == 0:
                return a
            return gcd(b%a, a)

        g = gcd(p, q)
        #   n*p   = k*q
        # = n*a*g = k*b*g = a*b*g
        # n = abg/p = p*b/p = b = q/g
        n = p//g
        k = q//g
        return [[None, 0], [2, 1]][k%2][n%2]


@pytest.mark.parametrize('p, q, expected', [
    (2, 1, 2),
    (3, 1, 1),
])
def test(p, q, expected):
    assert expected == Solution().mirrorReflection(p, q)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
