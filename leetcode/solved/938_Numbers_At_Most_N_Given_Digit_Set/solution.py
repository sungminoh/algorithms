#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.

Example 3:

Input: digits = ["7"], n = 8
Output: 1

Constraints:

	1 <= digits.length <= 9
	digits[i].length == 1
	digits[i] is a digit from '1' to '9'.
	All the values in digits are unique.
	digits is sorted in non-decreasing order.
	1 <= n <= 109
"""
from bisect import bisect_left
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        ub = str(n)

        @lru_cache(None)
        def dp(i, relaxed):
            if i == len(ub):
                return 1
            ret = 0
            for d in digits:
                if relaxed or d < ub[i]:
                    ret += dp(i+1, True)
                elif d == ub[i]:
                    ret += dp(i+1, False)
            return ret

        ret = dp(0, False)
        for i in range(1, len(ub)):
            ret += dp(i, True)

        return ret

    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        ub = str(n)
        l = len(ub)
        nd = len(digits)

        ret = 0
        # All relaxed cases that the length of number is smaller than n
        for i in range(1, l):
            ret += nd ** i

        for i, c in enumerate(ub):
            n_smaller = bisect_left(digits, c)
            # If we use a smaller digit than c,
            #  all digits can come for next positions
            ret += n_smaller * (nd ** (l-i-1))
            # If all digits are smaller than c
            #  or there isn't a digit that is same to c,
            #  there is no more cases to count
            if n_smaller == nd or digits[n_smaller] != c:
                return ret

        return ret+1


@pytest.mark.parametrize('digits, n, expected', [
    (["1","3","5","7"], 100, 20),
    (["1","4","9"], 1000000000, 29523),
    (["7"], 8, 1),
    (["3","4","8"], 4, 2),
])
def test(digits, n, expected):
    assert expected == Solution().atMostNGivenDigitSet(digits, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
