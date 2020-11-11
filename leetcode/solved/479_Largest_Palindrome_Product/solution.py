#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""
import sys
import pytest


def is_palindrom(s):
    s = str(s)
    return s == s[::-1]


class Solution:
    def largestPalindrome(self, n: int) -> int:
        e = pow(10, n)-1
        m = -float('inf')
        for s in range(2*e, -1, -1):
            larger_than_max = False
            for i in range(s//2, min(e+1, s)):
                j = s-i
                v = i*j
                if v > m:
                    larger_than_max = True
                if is_palindrom(v):
                    m = max(m, v)
            if not larger_than_max and m >= 0:
                break

        return m % 1337

    def largestPalindrome(self, n: int) -> int:
        e = pow(10, n)-1
        for i in range(e-1, e//10, -1):
            palindrom = int(str(i) + str(i)[::-1])
            j = e
            while j*j >= palindrom:
                if palindrom % j == 0:
                    return int(palindrom % 1337)
                j -= 1
        return 0


@pytest.mark.parametrize('n, expected', [
    (2, 987),
    (8, 475),
])
def test(n, expected):
    assert expected == Solution().largestPalindrome(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
