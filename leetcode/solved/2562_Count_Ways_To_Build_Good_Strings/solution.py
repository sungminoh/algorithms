#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

	Append the character '0' zero times.
	Append the character '1' one times.

This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation:
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011".
All binary strings from "000" to "111" are good strings in this example.

Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".

Constraints:

	1 <= low <= high <= 105
	1 <= zero, one <= low
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Sep 17, 2023 13:55"""
        MOD = int(1e9+7)

        @lru_cache(None)
        def dp(i):
            if i > high:
                return 0
            ret = 0 if i < low else 1
            ret += dp(i+zero) + dp(i+one)
            ret %= MOD
            return ret

        return dp(0)


@pytest.mark.parametrize('args', [
    ((3, 3, 1, 1, 8)),
    ((2, 3, 1, 2, 5)),
])
def test(args):
    assert args[-1] == Solution().countGoodStrings(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
