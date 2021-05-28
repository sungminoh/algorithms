#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0

Constraints:

	0 <= n <= 5 * 106
"""
import sys
import pytest


class Solution:
    def countPrimes(self, n: int) -> int:
        def cnt_primes(n):
            cnt = 0
            for i in range(2, n):
                if i not in non_primes:
                    cnt += 1
                    for j in range(i*i, n, i):
                        non_primes.add(j)
            return cnt

        non_primes = set()
        cnt = cnt_primes(n)
        return cnt

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [1]*n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [0]*len(primes[i*i:n:i])
        return sum(primes)


@pytest.mark.parametrize('n, expected', [
    (10, 4),
    (0, 0),
    (1, 0),
    (2, 0),
])
def test(n, expected):
    assert expected == Solution().countPrimes(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
