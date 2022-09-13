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
Explanation: 27 = 33

Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

Constraints:

	-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
import sys
import math
import pytest


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """05/13/2021 08:26"""
        if n <= 0:
            return False
        while n > 1:
            if n%3:
                return False
            n /= 3
        return True

    def isPowerOfThree(self, n: int) -> bool:
        """05/13/2021 08:29"""
        return n>0 and 1162261467%n == 0

    def isPowerOfThree(self, n: int) -> bool:
        """08/28/2022 16:39"""
        MAX_POWER_OF_3 = pow(3, int(math.log((2**31) - 1, 3)))
        return n > 0 and MAX_POWER_OF_3%n == 0


@pytest.mark.parametrize('n, expected', [
    (27, True),
    (0, False),
    (-1, False),
    (9, True),
    (45, False),
    (243, True)
])
def test(n, expected):
    assert expected == Solution().isPowerOfThree(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
