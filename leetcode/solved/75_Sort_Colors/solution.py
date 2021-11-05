#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:
Input: nums = [0]
Output: [0]
Example 4:
Input: nums = [1]
Output: [1]

Constraints:

	n == nums.length
	1 <= n <= 300
	nums[i] is 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
import copy
import random
import sys
from typing import List
import pytest


class Solution:
    def sortColors(self, nums):
        """04/25/2018 00:11"""
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            else:
                i += 1
        return nums

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l, i, r = 0, 0, len(nums)-1
        while i <= r:
            if nums[i] == 2:
                swap(i, r)
                r -= 1
            elif nums[i] == 0:
                swap(l, i)
                i += 1
                l += 1
            else:
                i += 1


def gen_testcase():
    case = [random.randint(0, 2) for _ in range(random.randint(1, 300))]
    return (case, sorted(case))


@pytest.mark.parametrize('nums, expected', [
    ([2,0,2,1,1,0], [0,0,1,1,2,2]),
    ([2,0,1], [0,1,2]),
    ([0], [0]),
    ([1], [1]),
    ([1,1,2], [1,1,2]),
    ([0,1,1,2], [0,1,1,2]),
    ([1,0,1,2], [0,1,1,2]),
    ([1, 0, 0, 1, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 1, 0, 2, 0, 0, 0, 2, 2, 0, 1, 1, 2, 2, 1],
     sorted([1, 0, 0, 1, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 1, 0, 2, 0, 0, 0, 2, 2, 0, 1, 1, 2, 2, 1])),
    *[gen_testcase() for _ in range(10)],
])
def test(nums, expected):
    print()
    org_nums = copy.copy(nums)
    Solution().sortColors(nums)
    if nums != expected:
        print(org_nums)
        print(nums)
    assert expected == nums


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
