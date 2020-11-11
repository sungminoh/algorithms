#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
import pytest


class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0:4] = [0, 1, 1, 2]

        def rec(n):
            if memo[n] > 0:
                return memo[n]
            ret = max(max(i, rec(i)) * max(n - i, rec(n - i))
                      for i in range(1, n // 2 + 1))
            memo[n] = ret
            return ret
        return rec(n)


@pytest.mark.parametrize('n, expected', [
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 9),
    (7, 12),
    (8, 18),
    (9, 27),
    (10, 36),
])
def test(n, expected):
    assert Solution().integerBreak(n) == expected
