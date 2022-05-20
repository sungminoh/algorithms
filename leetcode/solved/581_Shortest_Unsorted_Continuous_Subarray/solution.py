#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0

Constraints:

	1 <= nums.length <= 104
	-105 <= nums[i] <= 105

Follow up: Can you solve it in O(n) time complexity?
"""
import sys
from typing import List
import pytest


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """12/15/2020 16:17"""
        mx = -float('inf')
        mn = float('inf')
        stack = []
        for i, n in enumerate(nums):
            x = -float('inf')
            y = None
            while stack and stack[-1][0] > n:
                m, j = stack.pop()
                if m > x:
                    x = m
                    y = j
                mn = min(mn, j)
                mx = max(mx, i)
            stack.append((n, i))
            if y is not None:
                stack.append((x, y))
        return mx-mn+1 if mn != float('inf') else 0

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """12/15/2020 16:52"""
        l = 0
        while l < len(nums)-1 and nums[l] <= nums[l+1]: l += 1
        if l ==  len(nums)-1:
            return 0
        r = len(nums)-1
        while r > 0 and nums[r-1] <= nums[r]: r -= 1
        mn = min(nums[l:r+1])
        mx = max(nums[l:r+1])
        while l >= 0 and nums[l] > mn: l -= 1
        while r < len(nums) and nums[r] < mx: r += 1
        return (r-1) - (l+1) + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """05/20/2022 12:47
        When i and j are the start and end indexes of such subarray, all
        numbers before i should be smaller than min(nums[i:]) and all numbers
        after j should be larger than max(nums[:j+1])
        """
        if not nums:
            return 0
        max_from_left = [nums[0]]
        for i in range(1, len(nums)):
            max_from_left.append(max(max_from_left[-1], nums[i]))
        min_from_right = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            min_from_right.append(min(min_from_right[-1], nums[i]))
        min_from_right.reverse()
        s = None
        for i in range(len(nums)-1):
            if max_from_left[i] > min_from_right[i+1]:
                s = i
                break
        if s is None:
            return 0
        for i in range(len(nums)-1, 0, -1):
            if max_from_left[i-1] > min_from_right[i]:
                return i-s+1
        return 0


@pytest.mark.parametrize('nums, expected', [
    ([2,6,4,8,10,9,15], 5),
    ([1,2,3,4], 0),
    ([1], 0),
    ([2,1], 2),
    ([1,3,2,2,2], 4),
    ([1,3,2,3,3], 2),
])
def test(nums, expected):
    assert expected == Solution().findUnsortedSubarray(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
