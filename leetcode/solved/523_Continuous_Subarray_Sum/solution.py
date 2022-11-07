#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

	its length is at least two, and
	the sum of the elements of the subarray is a multiple of k.

Note that:

	A subarray is a contiguous part of the array.
	An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 109
	0 <= sum(nums[i]) <= 231 - 1
	1 <= k <= 231 - 1
"""
from typing import List
import pytest
import sys


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """05/31/2020 17:30"""
        cumsum = [0]
        for i in range(len(nums)):
            if i == 0:
                cumsum.append(nums[i])
            else:
                cumsum.append(nums[i] + cumsum[-1])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = cumsum[j+1] - cumsum[i]
                if k == 0:
                    if s == 0:
                        return True
                else:
                    if s % k == 0:
                        return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """05/31/2020 17:39"""
        modulo_position = {0: -1}
        s = 0
        for i, n in enumerate(nums):
            s += n
            if k != 0:
                s %= k
            if s in modulo_position:
                if modulo_position[s] + 2 <= i:
                    return True
            else:
                modulo_position[s] = i
        return False

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """11/06/2022 14:29"""
        exists = {0: -1}
        acc = 0
        for i, n in enumerate(nums):
            acc += n
            if k != 0:
                acc %= k
            if exists.get(acc, i) < i-1:
                return True
            exists.setdefault(acc, i)
        return False


@pytest.mark.parametrize('nums, k, expected', [
    ([23,2,4,6,7], 6, True),
    ([23,2,6,4,7], 6, True),
    ([23,2,6,4,7], 0, False),
    ([23,2,4,6,7], -6, True),
    ([23,2,4,6,6], 7, True),
    ([0,0], 0, True),
])
def test(nums, k, expected):
    assert expected == Solution().checkSubarraySum(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
