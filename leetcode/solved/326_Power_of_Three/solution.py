#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Example 2:
Input: n = 0
Output: false
Example 3:
Input: n = 9
Output: true
Example 4:
Input: n = 45
Output: false

Constraints:

	-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
import sys
import math
import pytest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n%3:
                return False
            n /= 3
        return True

    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and 1162261467%n == 0


@pytest.mark.parametrize('n, expected', [
    (27, True),
    (0, False),
    (9, True),
    (45, False),
    (243, True)
])
def test(n, expected):
    assert expected == Solution().isPowerOfThree(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
