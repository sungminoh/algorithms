#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
"""
import pytest

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # f(k) = f(k-1) * (10 - (k-1))
        # f(0) = 1
        # f(1) = 9 != 1 * (10 - 0)
        # f(2) = 81 = 9 * (10 - 1)
        # f(3) = 81 * (10 - 2)
        # ...
        if n == 0:
            return 1
        elif n == 1:
            return 10
        ret = [0] * (n + 1)
        ret[0] = 1
        ret[1] = 9
        for i in range(2, n+1):
            ret[i] = ret[i-1] * (11 - i)
        return sum(ret)


@pytest.mark.parametrize('n, expected', [
    (0, 1),
    (1, 10),
    (2, 91),
    (3, 739),
])
def test(n, expected):
    assert expected == Solution().countNumbersWithUniqueDigits(n)


