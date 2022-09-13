#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true

Constraints:

	-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""
import sys
import pytest


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p2 = 0b10101010101010101010101010101010
        return n > 0 \
            and n&(n-1) == 0 \
            and n&p2 == 0


@pytest.mark.parametrize('n, expected', [
    (16, True),
    (5, False),
    (1, True),
])
def test(n, expected):
    assert expected == Solution().isPowerOfFour(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
