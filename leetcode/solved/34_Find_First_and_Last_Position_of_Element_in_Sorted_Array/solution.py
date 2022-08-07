#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

	0 <= nums.length <= 105
	-109 <= nums[i] <= 109
	nums is a non-decreasing array.
	-109 <= target <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """05/19/2021 09:29
        Binary search
        Time complexity: O(logn)
        Space complexity: O(1)
        """
        def binsearch(nums, target, left=True):
            if not nums:
                return -1
            s, e = 0, len(nums)-1
            while s <= e:
                m = s + ((e-s)//2)
                if nums[m] < target:
                    s = m+1
                elif nums[m] > target:
                    e = m-1
                else:
                    if left:
                        e = m-1
                    else:
                        s = m+1
            idx = e+1 if left else s-1
            return idx if 0<=idx<len(nums) and nums[idx] == target else -1

        return [binsearch(nums, target, True), binsearch(nums, target, False)]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisearch(s, e, x, func):
            while s <= e:
                m = s + (e-s)//2
                if func(m, x):
                    s = m+1
                else:
                    e = m-1
            return s-1

        s = bisearch(0, len(nums)-1, target, lambda i, x: nums[i] < x) + 1
        e = bisearch(0, len(nums)-1, target, lambda i, x: nums[i] <= x)
        return [s, e] if s <= e < len(nums) else [-1, -1]


@pytest.mark.parametrize('nums, target, expected', [
    ([5,7,7,8,8,10], 8, [3,4]),
    ([5,7,7,8,8,10], 6, [-1,-1]),
    ([], 0, [-1,-1]),
    ([2,2], 3, [-1, -1]),
])
def test(nums, target, expected):
    assert expected == Solution().searchRange(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
