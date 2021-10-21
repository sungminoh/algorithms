#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

	0 <= left <= right <= 231 - 1
"""
import sys
import itertools
import pytest
from traitlets.config.sphinxdoc import reverse_aliases


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """12/21/2018 20:44"""
        def find_last_diff_idx(m, n):
            idx = -1
            for i in range(32):
                if m % 2 != n % 2:
                    idx = i
                m //= 2
                n //= 2
            return idx

        last_diff_idx = find_last_diff_idx(m, n)
        m -= m % pow(2, last_diff_idx + 1)
        return m

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        p = 1
        ret = 0
        for a, b in zip(reversed(bin(left)[2:]), reversed(bin(right)[2:])):
            a = int(a)
            b = int(b)
            if right-left <= p:
                ret += p*(a&b)
            p *= 2
        return ret


@pytest.mark.parametrize('left, right, expected', [
    (5, 7, 4),
    (0, 0, 0),
    (1, 2147483647, 0),
])
def test(left, right, expected):
    assert expected == Solution().rangeBitwiseAnd(left, right)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
