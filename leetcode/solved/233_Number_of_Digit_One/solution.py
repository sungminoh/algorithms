
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
import sys
import pytest


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        # 1234 -> 4, 1000
        l = len(str(n))
        if l == 1:
            return 1
        ten = 10**(l - 1)
        cof = n // ten
        cnt = cof * (l-1) * (ten // 10)
        if cof > 1:
            n -= cof * ten
            cnt += ten
        else:
            n -= ten
            cnt += n + 1
        cnt += self.countDigitOne(n)
        return cnt

    def countDigitOne_bottomup(self, n: int) -> int:
        if n <= 0: return 0

        res, d, k = 0, 1, n
        while k > 0:
            k, m = divmod(k, 10)

            res += k * d
            if m == 1:
                res += n % d + 1
            elif m > 1: res += d

            d *= 10
        return res


@pytest.mark.parametrize('n, expected', [
    (13, 6),
    (-1, 0),
    (1, 1),
    (20, 12),
])
def test(n, expected):
    assert expected == Solution().countDigitOne(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
