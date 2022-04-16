#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:

	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	nums is guaranteed to be rotated at some pivot.
	-104 <= target <= 104

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
import sys
import operator
from typing import List
import pytest


class Solution:
    def search(self, nums, target):
        """05/01/2018 05:51"""
        def bisearch(ns, t):
            i, j = 0, len(nums)-1
            while i <= j:
                m = (i+j)//2
                if ns[m] > t:
                    j = m-1
                elif ns[m] < t:
                    i = m+1
                else:
                    return True
            return False

        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        p = len(nums)-1
        while p >= 0 and nums[p-1] <= nums[p]:
            p -= 1
        return bisearch(nums[p:] + nums[:p], target)

    def search(self, nums: List[int], target: int) -> bool:
        def find_pivot(nums):
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return i
            return 0

        def bisearch(arr, x, pivot=0, func=operator.lt):
            l, r = 0, len(arr)-1
            while l <= r:
                m = l + (r-l)//2
                if func(arr[(m+pivot)%len(arr)], x):
                    l = m+1
                else:
                    r = m-1
            return (l+pivot)%len(arr)

        pivot = find_pivot(nums)
        i = bisearch(nums, target, pivot)
        return 0<=i<len(nums) and nums[i] == target


@pytest.mark.parametrize('nums, target, expected', [
([2,5,6,0,0,1,2], 0, True),
([2,5,6,0,0,1,2], 3, False),
])
def test(nums, target, expected):
    assert expected == Solution().search(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
