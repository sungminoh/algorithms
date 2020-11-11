#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""
from heapq import heappush, heappop
import math


class Solution:
    def find_primes_under(self, n):
        is_prime = [True] * (n + 1)
        for i in range(2, n + 1):
            for j in range(2 * i, n, i):
                is_prime[j] = False
        return [i for i in range(2, n + 1) if is_prime[i]]

    def _bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        prime_squares = [x**2 for x in self.find_primes_under(int(math.sqrt(n)))]
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
        return int(math.sqrt(n))


if __name__ == '__main__':
    cases = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 2),
        (6, 2),
        (7, 2),
        (8, 2),
        (9, 3),
        (10, 3),
        (11, 3),
        (12, 3),
        (13, 3),
        (14, 3),
        (15, 3),
        (16, 4),
        (17, 4),
        (18, 4),
        (19, 4),
        (37, 6),
    ]
    for case, expected in cases:
        actual = Solution().bulbSwitch(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
