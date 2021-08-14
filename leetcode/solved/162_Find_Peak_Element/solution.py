#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

	1 <= nums.length <= 1000
	-231 <= nums[i] <= 231 - 1
	nums[i] != nums[i + 1] for all valid i.
"""
import sys
from typing import List
import pytest


class Solution:
    def findPeakElement(self, nums):
        """07/28/2018 17:31"""
        def is_peak(i):
            return (-float('inf') if i == 0 else nums[i-1]) \
                < nums[i] \
                > (-float('inf') if i == len(nums) else nums[i+1])

        def is_asc(i):
            return nums[i] < nums[i+1]

        def find_peak_index(i, j):
            if i == j:
                return i
            m = (i+j)//2
            if is_peak(m):
                return m
            elif is_asc(m):
                return find_peak_index(m+1, j)
            else:
                return find_peak_index(i, m)

        if not nums:
            return
        if len(nums) == 1:
            return 0
        return find_peak_index(0, len(nums)-1)


    def findPeakElement(self, nums: List[int]) -> int:
        def rec(l, r, nums):
            if l == r:
                return l
            if l+1 == r:
                return r if nums[r] > nums[l] else l
            m = l + (r-l)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m
            if nums[m-1] < nums[m] < nums[m+1]:
                return rec(m+1, r, nums)
            else:
                return rec(l, m-1, nums)

        return rec(0, len(nums)-1, nums)


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,1], 2),
    ([1,2,1,3,5,6,4], 5),
    ([1,2], 1),
    ([3,1,2], 0),
])
def test(nums, expected):
    assert expected == Solution().findPeakElement(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
