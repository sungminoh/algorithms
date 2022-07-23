#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:

	n == nums.length
	1 <= n <= 104
	-105 <= nums[i] <= 105
"""
import sys
from typing import List
import pytest


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """02/03/2021 18:41
        Two passes from left and from right
        Time complexity: O(n)
        Space complexity: O(1)
        """
        def from_left(nums):
            """increase the smaller number to the previous highest"""
            found = False
            p = nums[0]
            for i in range(1, len(nums)):
                if p > nums[i]:
                    if found:
                        return False
                    found = True
                else:
                    p = nums[i]
            return True

        def from_right(nums):
            """decrease the larger number to the previous highest"""
            found = False
            p = nums[-1]
            for i in range(len(nums)-1, -1, -1):
                if p < nums[i]:
                    if found:
                        return False
                    found = True
                else:
                    p = nums[i]
            return True

        return from_left(nums) or from_right(nums)

    def checkPossibility(self, nums: List[int]) -> bool:
        """
        One pass, inplace
        Time complexity: O(n)
        Space complexity: O(1)
        """
        flag = False
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            if flag:
                return False
            if i-2 < 0:
                nums[i-1] = nums[i]
            elif nums[i-2] <= nums[i]:
                nums[i-1] = nums[i-2]
            else:
                nums[i] = nums[i-1]
            flag = True
        return True


    def checkPossibility(self, nums: List[int]) -> bool:
        """
        One pass
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not nums:
            return True
        found = False
        nums.insert(0, -float('inf'))
        p = nums[0]
        for i in range(1, len(nums)):
            if p > nums[i]:
                if found:
                    return False
                if i>=2 and nums[i-2] <= nums[i]:
                    p = nums[i]
                found = True
            else:
                p = nums[i]
        return True


@pytest.mark.parametrize('nums, expected', [
    ([4,2,3], True),
    ([4,2,1], False),
    ([-1,4,2,3], True),
])
def test(nums, expected):
    assert expected == Solution().checkPossibility(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
