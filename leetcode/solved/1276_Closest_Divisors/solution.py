#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:

Input: num = 123
Output: [5,25]

Example 3:

Input: num = 999
Output: [40,25]

Constraints:

	1 <= num <= 10^9
"""
import sys
from typing import List
import pytest


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def divisors(n):
            for i in range(int((n+2)**0.5), 0, -1):
                if (n+1) % i == 0:
                    return [i, (n+1)//i]
                if (n+2) % i == 0:
                    return [i, (n+2)//i]
            return [1, n+1]

        return divisors(num)


@pytest.mark.parametrize('num, expected', [
    (8, [3,3]),
    (123, [5,25]),
    (999, [40,25]),
    (785270913, [27595, 28457]),
    (2, [2,2]),
    (762311132, [26, 29319659])
])
def test(num, expected):
    assert sorted(expected) == Solution().closestDivisors(num)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
