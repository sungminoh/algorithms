#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

	1 <= piles.length <= 104
	piles.length <= h <= 109
	1 <= piles[i] <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_all(n):
            return sum((pile + n - 1) // n for pile in piles) <= h

        def bisearch(s, e, key=can_eat_all):
            while s <= e:
                m = s + (e-s)//2
                if key(m):
                    e = m-1
                else:
                    s = m+1
            return e+1

        return bisearch(1, max(piles))


@pytest.mark.parametrize('piles, h, expected', [
    ([3,6,7,11], 8, 4),
    ([30,11,23,4,20], 5, 30),
    ([30,11,23,4,20], 6, 23),
])
def test(piles, h, expected):
    assert expected == Solution().minEatingSpeed(piles, h)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
