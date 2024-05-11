#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

Constraints:

	1 <= nums.length <= 104
	-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""
from typing import List
import pytest
import sys


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """May 05, 2024 12:10
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i  # first zero
        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1


@pytest.mark.parametrize('args', [
    (([0,1,0,3,12], [1,3,12,0,0])),
    (([0], [0])),
])
def test(args):
    Solution().moveZeroes(*args[:-1])
    assert args[-1] == args[0]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
