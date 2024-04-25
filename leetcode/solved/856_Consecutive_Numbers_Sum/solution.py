#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Constraints:

	1 <= n <= 109
"""
import pytest
import sys


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        """TLE"""
        ret = 0
        for i in range(1, (n+1)//2+1):
            if i%2 == 0:
                if n%(i//2) == 0:
                    sum_of_pair = n//(i//2)
                    if sum_of_pair%2 == 1:
                        left = sum_of_pair // 2
                        if left >= (i//2):
                            ret += 1
            else:
                if n%i == 0:
                    middle = n//i
                    if middle > (i-1)//2:
                        ret += 1
        return ret

    def consecutiveNumbersSum(self, n: int) -> int:
        """Apr 16, 2024 23:18
        n
        = a+(a+1)+...+(a+i-1)                 Exists a > 0
        = a*i + 1 + ... + i-1
        = a*i + sum(0, i-1)
        -> (n - sum(0, i-1)) / i = a
        ->
        """
        ret = 0
        acc = 0
        for i in range(1, n+1):
            acc += i-1
            if acc >= n:
                break
            if (n - acc) % i == 0:
                ret += 1
        return ret


@pytest.mark.parametrize('args', [
    ((5, 2)),
    ((9, 3)),
    ((15, 4)),
    ((3, 2)),
    ((4, 1)),
    ((34624713, 8)),
])
def test(args):
    assert args[-1] == Solution().consecutiveNumbersSum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
