#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

Return True if the array is good otherwise return False.

Example 1:

Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1

Example 2:

Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1

Example 3:

Input: nums = [3,6]
Output: false

Constraints:

	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^9
"""
from typing import List
import pytest
import sys


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """May 12, 2024 21:13"""
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(b, a%b)

        ret = nums[0]
        for i in range(1, len(nums)):
            ret = gcd(ret, nums[i])
        return ret == 1


@pytest.mark.parametrize('args', [
    (([12,5,7,23], True)),
    (([29,6,10], True)),
    (([3,6], False)),
])
def test(args):
    assert args[-1] == Solution().isGoodArray(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
