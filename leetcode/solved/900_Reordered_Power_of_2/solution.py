#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:

Input: n = 1
Output: true

Example 2:

Input: n = 10
Output: false

Constraints:

	1 <= n <= 109
"""
import sys
import pytest


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digit(n):
            cnt = [0]*10
            while n:
                cnt[n%10] += 1
                n //= 10
            return tuple(cnt)

        signatures = set()
        p = 1
        while p <= 10**9:
            signatures.add(count_digit(p))
            p *= 2

        return count_digit(n) in signatures


@pytest.mark.parametrize('n, expected', [
    (1, True),
    (10, False),
])
def test(n, expected):
    assert expected == Solution().reorderedPowerOf2(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
