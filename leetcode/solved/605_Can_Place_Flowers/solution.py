#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

	1 <= flowerbed.length <= 2 * 104
	flowerbed[i] is 0 or 1.
	There are no two adjacent flowers in flowerbed.
	0 <= n <= flowerbed.length
"""
import sys
from typing import List
import pytest


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (i == 0 or flowerbed[i-1] == 0) \
                    and flowerbed[i] == 0 \
                    and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <== 0:
                return True
        return n <= 0


@pytest.mark.parametrize('flowerbed, n, expected', [
    ([1,0,0,0,1], 1, True),
    ([1,0,0,0,1], 2, False),
    ([1,0,0,0,0,1], 2, False),
    ([0,0,0,0,0,1,0,0], 0, True),
])
def test(flowerbed, n, expected):
    assert expected == Solution().canPlaceFlowers(flowerbed, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))