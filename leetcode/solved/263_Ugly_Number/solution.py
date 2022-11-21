#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

	-231 <= n <= 231 - 1
"""
import pytest
import sys


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        for p in [5,3,2]:
            while n%p == 0:
                n //= p
        return n == 1


@pytest.mark.parametrize('n, expected', [
    (6, True),
    (1, True),
    (14, False),
])
def test(n, expected):
    assert expected == Solution().isUgly(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
