#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

	0 <= n <= 30
"""
from functools import lru_cache
import sys
import pytest


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        """05/03/2021 09:13"""
        return n if n <= 1 else self.fib(n-1) + self.fib(n-2)

    def fib(self, n: int) -> int:
        """07/23/2022 10:40"""
        memo = [0, 1]
        for i in range(2, n+1):
            memo[i%2] = sum(memo)
        return memo[n%2]


@pytest.mark.parametrize('n, expected', [
    (2, 1),
    (3, 2),
    (4, 3),
])
def test(n, expected):
    assert expected == Solution().fib(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
