#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537

Constraints:

	0 <= n <= 37
	The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""
import pytest
import sys


class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0,1,1]
        for i in range(3, n+1):
            cache[i%3] = sum(cache)
        return cache[n%3]


@pytest.mark.parametrize('args', [
    ((4, 4)),
    ((25, 1389537)),
])
def test(args):
    assert args[-1] == Solution().tribonacci(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
