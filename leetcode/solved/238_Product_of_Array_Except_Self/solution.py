#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

	2 <= nums.length <= 105
	-30 <= nums[i] <= 30
	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
import sys
from typing import List
import pytest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """08/25/2019 19:56"""
        ret = [1] * len(nums)
        accum = 1
        for i, n in enumerate(nums):
            ret[i] *= accum
            accum *= n
        accum = 1
        for i, n in enumerate(nums[-1::-1]):
            ret[len(nums) - 1 - i] *= accum
            accum *= n
        return ret

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """12/03/2021 20:57"""
        if not nums:
            return []
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[i]*nums[i])
        suffix = [1]
        for i in range(len(nums)):
            suffix.append(suffix[i] * nums[len(nums)-1-i])
        suffix = suffix[::-1]
        return [prefix[i] * suffix[i+1] for i in range(len(nums))]


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4], [24,12,8,6]),
    ([-1,1,0,-3,3], [0,0,9,0,0]),
])
def test(nums, expected):
    assert expected == Solution().productExceptSelf(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
