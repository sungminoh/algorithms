#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:

	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	All values of nums are unique.
	nums is an ascending array that is possibly rotated.
	-104 <= target <= 104
"""
import sys
import operator
from typing import List
import pytest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return i
            return 0

        p = find_pivot(nums)

        def bisearch(nums, target):
            s, e = 0, len(nums)-1
            while s <= e:
                m = s + (e-s)//2
                n = nums[(m+p)%len(nums)]
                if n < target:
                    s = m+1
                elif n > target:
                    e = m-1
                else:
                    return (m+p)%len(nums)
            return -1

        return bisearch(nums, target)


@pytest.mark.parametrize('nums, target, expected', [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
])
def test(nums, target, expected):
    assert expected == Solution().search(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
