#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:

	1 <= n <= 1690
"""
import heapq
import pytest
import sys


class Solution:
    def nthUglyNumber_(self, n: int) -> int:
        primeIdx = {2: 0, 3: 0, 5: 0}
        size = 1
        nums = [1]
        while size < n:
            m = min(p * nums[i] for p, i in primeIdx.items())
            for p, i in primeIdx.items():
                if p * nums[i] == m:
                    primeIdx[p] += 1
            nums.append(m)
            size += 1
        return nums[-1]

    def nthUglyNumber(self, n: int) -> int:
        primeIdx = {2: 0, 3: 0, 5: 0}
        size = 1
        offset = 0
        nums = [1]
        while size < n:
            m = min(p * nums[i - offset] for p, i in primeIdx.items())
            for p, i in primeIdx.items():
                if p * nums[i - offset] == m:
                    primeIdx[p] += 1
            nums.append(m)
            size += 1
            minIdx = min(primeIdx.values())
            nums = nums[minIdx - offset:]
            offset = minIdx
        return nums[-1]

    def nthUglyNumber(self, n: int) -> int:
        """Nov 12, 2024 19:56"""
        visited = set()
        h = [1]
        for _ in range(n-1):
            a = heapq.heappop(h)
            for x in [2,3,5]:
                b = a*x
                if b not in visited:
                    visited.add(b)
                    heapq.heappush(h, b)
        return heapq.heappop(h)


@pytest.mark.parametrize('args', [
    ((10, 12)),
    ((1, 1)),
])
def test(args):
    assert args[-1] == Solution().nthUglyNumber(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
