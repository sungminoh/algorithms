#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:

	-231 <= dividend, divisor <= 231 - 1
	divisor != 0
"""
import sys
import pytest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """06/16/2022 11:05"""
        if dividend == -(2**31) and divisor == -1:
            return 2**31-1
        sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            return dividend if sign > 0 else -dividend
        if divisor == 2:
            if sign > 0 or (dividend >> 1) << 1 == dividend:
                # positive or even
                ret = dividend >> 1
                return ret if sign > 0 else -ret
            else:
                ret = (dividend >> 1) + 1
                return ret if sign > 0 else -ret
        ret = 0
        while dividend>=divisor:
            d = divisor
            m = 1
            while (d<<1) <= dividend:
                d <<= 1
                m <<= 1
            dividend -= d
            ret += m
        return ret if sign > 0 else -ret

    def divide(self, dividend: int, divisor: int) -> int:
        """06/16/2022 11:20"""
        # trivial case
        if divisor == 1:
            return dividend
        if divisor == -1:
            # edge case
            if dividend == -(2**31):
                return -(dividend+1)
            return -dividend
        if dividend <= 0 and divisor > 0:
            return -self.divide(dividend, -divisor)
        if dividend > 0 and divisor <= 0:
            return -self.divide(-dividend, divisor)
        if dividend > 0 and divisor > 0:
            return self.divide(-dividend, -divisor)
        if divisor == -1:
            return -dividend
        ret = 0
        while dividend <= divisor:
            d, m = divisor, 1
            while dividend <= (d<<1):
                d <<= 1
                m <<= 1
            dividend -= d
            ret += m
        return ret


@pytest.mark.parametrize('dividend, divisor, expected', [
    (10, 3, 3),
    (7, -3, -2),
    (-1, 1, -1),
    (-2147483648, -1, 2147483647),
    (-2147483648, 2, -1073741824),
    (2147483647, 3, 2147483647//3),
    (0, 1, 0),
    (-2147483648, 1, -2147483648)
])
def test(dividend, divisor, expected):
    assert expected == Solution().divide(dividend, divisor)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
