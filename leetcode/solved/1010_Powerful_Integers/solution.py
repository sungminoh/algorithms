#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Constraints:

	1 <= x, y <= 100
	0 <= bound <= 106
"""
import sys
from typing import List
import pytest


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        Generate powers of x and y
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def powers(n, bound):
            """Iterate powers of n less than bound"""
            if bound > 1:
                yield 1
            if n > 1:
                p = n
                while p < bound:
                    yield p
                    p *= n

        ret = set()
        for a in powers(x, bound):
            for b in powers(y, bound-a+1):
                ret.add(a+b)

        return list(ret)


@pytest.mark.parametrize('x, y, bound, expected', [
    (2, 3, 10, [2,3,4,5,7,9,10]),
    (3, 5, 15, [2,4,6,8,10,14]),
    (2,3,10,[2,3,4,5,7,9,10]),
    (2,1,10,[2,3,5,9]),
    (1,1,0,[]),
    (1,1,1,[]),
])
def test(x, y, bound, expected):
    assert set(expected) == set(Solution().powerfulIntegers(x, y, bound))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
