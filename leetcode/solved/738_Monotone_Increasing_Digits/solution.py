#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:

Input: N = 10
Output: 9

Example 2:

Input: N = 1234
Output: 1234

Example 3:

Input: N = 332
Output: 299

Note:
N is an integer in the range [0, 10^9].
"""
import sys
import pytest


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        def rec(n, m):
            if n // 10 == 0:
                return min(n, m)
            if n % 10 == 9 and m >= 9:
                return 10*rec(n//10, 9) + 9
            if n % 10 == 0:
                return 10*rec(n//10-1, 9) + 9
            if m > n%10:
                return max(
                    10*rec(n//10, n%10) + n%10,
                    10*rec(n//10-1, m) + m)
            return 10*rec(n//10, min(m, n%10)) + min(m, n%10)
        return rec(N, 9)


@pytest.mark.parametrize('N, expected', [
    (10, 9),
    (1234, 1234),
    (332, 299),
    (12, 12),
])
def test(N, expected):
    assert expected == Solution().monotoneIncreasingDigits(N)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

