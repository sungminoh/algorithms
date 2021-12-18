#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: n = 1, a = 2, b = 3
Output: 2
Example 2:
Input: n = 4, a = 2, b = 3
Output: 6
Example 3:
Input: n = 5, a = 2, b = 4
Output: 10
Example 4:
Input: n = 3, a = 6, b = 4
Output: 8

Constraints:

	1 <= n <= 109
	2 <= a, b <= 4 * 104
"""
import sys
from heapq import heappop
from heapq import heapify
from heapq import heappush
import pytest


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = int(1e9 + 7)
        def mul(*nums):
            ret = 1
            for n in nums:
                ret *= n%MOD
                ret %= MOD
            return ret

        def gcd(a, b):
            if a > b:
                return gcd(b, a)
            if b % a == 0:
                return a
            return gcd((b-a)%a, a)

        def nth(n, a, b):
            """a and b are coprime"""
            if a == 1 or b == 1:
                return n
            i, j = 1, 1
            ret = 0
            for _ in range(n):
                if ret == a*i:
                    i += 1
                if ret == b*j:
                    j += 1
                ret = min(a*i, b*j)
            return ret % MOD

        g = gcd(a, b)
        x = a//g
        y = b//g
        m, r = divmod(n, x*y)

        return (mul(x, y, g, m) + mul(g, nth(r, x, y))) % MOD

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        We want to find n-th element from the array of numbers is divisble
        by a or b.
        Let's say such array is arr = [a, b, ..., lcm(a, b), ...]
        If the number of elements smaller than or equal to lcm(a, b) is k,
        and n is represented as n = m * k + r, n-th number is going to be
        n-th number = m*lcm(a, b) + (r == 0 ? 0 : arr[r-1])
        """
        MOD = int(1e9 + 7)

        def mul(*nums):
            ret = 1
            for n in nums:
                ret *= n%MOD
                ret %= MOD
            return ret

        def gcd(a, b):
            if a > b:
                return gcd(b, a)
            if b % a == 0:
                return a
            return gcd((b-a)%a, a)

        def order(n, a, b):
            af = n // a
            bf = n // b
            cf = n // (a*b)
            return af+bf-cf

        def nth(n, a, b):
            s, e = 0, a*b
            while s < e:
                m = s + (e-s)//2
                o = order(m, a, b)
                if o < n:
                    s = m+1
                else:
                    e = m
            return s

        g = gcd(a, b)
        x = a//g
        y = b//g
        # the number of numbers divisible by either a or b smaller than lcm
        #  is x+y-1
        m, r = divmod(n, x+y-1)

        return (mul(x, y, g, m) + mul(g, nth(r, x, y))) % MOD


@pytest.mark.parametrize('n, a, b, expected', [
    (1, 2, 3, 2),
    (4, 2, 3, 6),
    (5, 2, 4, 10),
    (3, 6, 4, 8),
    (8, 10, 5, 40),
    (10, 10, 8, 50),
    (1000000000, 40000, 40000, 999720007),
    (1000000000, 39999, 40000, 999860007),
])
def test(n, a, b, expected):
    assert expected == Solution().nthMagicalNumber(n, a, b)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
