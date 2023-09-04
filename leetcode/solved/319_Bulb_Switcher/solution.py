import math

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Example 1:

Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 1

Constraints:

	0 <= n <= 109
"""
from heapq import heappop, heappush
import pytest
import sys


class Solution:
    def bulbSwitch(self, n: int) -> int:
        ""'Dec 29, 2019 00:20"""
        def find_primes_under(n):
            is_prime = [True] * (n + 1)
            for i in range(2, n + 1):
                for j in range(2 * i, n, i):
                    is_prime[j] = False
            return [i for i in range(2, n + 1) if is_prime[i]]

        if n == 0:
            return 0
        prime_squares = [x**2 for x in find_primes_under(int(math.sqrt(n)))]
        visited = set()
        heap = [1]
        ret = 0
        while heap:
            val = heappop(heap)
            ret += 1
            for ps in prime_squares:
                new_val = ps * val
                if new_val <= n and new_val not in visited:
                    visited.add(new_val)
                    heappush(heap, new_val)
        return ret

    def bulbSwitch(self, n: int) -> int:
        """Dec 29, 2019 00:24"""
        return int(math.sqrt(n))

    def bulbSwitch(self, n: int) -> int:
        """Sep 04, 2023 12:45"""
        visited = set()
        heap = []
        for x in range(1, int(n**0.5+1)):
            visited.add(x*x)
            heappush(heap, x*x)

        ret = 0
        while heap:
            n = heap[0]
            for x in heap:
                if n*x <= n and n*x not in visited:
                    visited.add(n*x)
                    heappush(heap, n*x)
            ret += 1
            heappop(heap)

        return ret


@pytest.mark.parametrize('args', [
    ((3, 1)),
    ((0, 0)),
    ((1, 1)),
    ((1, 1)),
    ((2, 1)),
    ((3, 1)),
    ((4, 2)),
    ((5, 2)),
    ((6, 2)),
    ((7, 2)),
    ((8, 2)),
    ((9, 3)),
    ((10, 3)),
    ((11, 3)),
    ((12, 3)),
    ((13, 3)),
    ((14, 3)),
    ((15, 3)),
    ((16, 4)),
    ((17, 4)),
    ((18, 4)),
    ((19, 4)),
    ((37, 6)),
])
def test(args):
    assert args[-1] == Solution().bulbSwitch(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
