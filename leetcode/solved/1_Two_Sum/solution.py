#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

	2 <= nums.length <= 104
	-109 <= nums[i] <= 109
	-109 <= target <= 109
	Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
import sys
from typing import List
import pytest


class Solution:
    def twoSum(self, nums, target):
        """12/28/2017 20:06"""
        for i in range(len(nums)-1):
            n1 = nums[i]
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if n1 + n2 == target:
                    return [i, j]
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, n in enumerate(nums):
            if target-n in idx:
                return [idx[target-n], i]
            idx[n] = i
        return [-1, -1]


@pytest.mark.parametrize('nums, target, expected', [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
])
def test(nums, target, expected):
    assert expected == Solution().twoSum(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
