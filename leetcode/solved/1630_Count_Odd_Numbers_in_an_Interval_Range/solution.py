#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:

	0 <= low <= high <= 10^9
"""
import pytest
import sys


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """Mar 20, 2023 23:13"""
        high += high%2
        low -= low%2
        return (high-low)//2


@pytest.mark.parametrize('args', [
    ((3, 7, 3)),
    ((8, 10, 1)),
    ((14, 17, 2)),
])
def test(args):
    assert args[-1] == Solution().countOdds(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
