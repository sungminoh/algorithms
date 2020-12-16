#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true

Constraints:

	0 <= c <= 231 - 1
"""
import sys
import pytest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        i = 0
        while i <= c**0.5:
            r = (c - i**2) ** 0.5
            if int(r) == r:
                return True
            i += 1
        return False


@pytest.mark.parametrize('c, expected', [
    (5, True),
    (3, False),
    (4, True),
    (2, True),
    (1, True),
])
def test(c, expected):
    assert expected == Solution().judgeSquareSum(c)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
