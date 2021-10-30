#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

	[4,5,6,7,0,1,4] if it was rotated 4 times.
	[0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [1,3,5]
Output: 1
Example 2:
Input: nums = [2,2,2,0,1]
Output: 0

Constraints:

	n == nums.length
	1 <= n <= 5000
	-5000 <= nums[i] <= 5000
	nums is sorted and rotated between 1 and n times.

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
import sys
from typing import List
import pytest


class Solution:
    def findMin(self, nums):
        """11/04/2018 22:58"""
        if len(nums) <= 2:
            return min(nums)
        m = len(nums)//2
        if nums[m] > nums[-1]:
            return self.findMin(nums[m+1:])
        elif nums[m] < nums[-1]:
            return self.findMin(nums[:m+1])
        else:
            if nums[0] < nums[m]:
                return nums[0]
            elif nums[0] > nums[m]:
                return self.findMin(nums[:m+1])
            else:
                if len(set(nums[m:])) == 1:
                    return self.findMin(nums[:m+1])
                else:
                    return self.findMin(nums[m+1:])

    def findMin(self, nums: List[int]) -> int:
        def find_min(s, e):
            if s == e:
                return nums[s]
            if nums[e] > nums[s]:
                return nums[s]
            m = s + ((e-s)//2)
            if nums[m] < nums[s]:
                return find_min(s, m)
            if nums[m] > nums[s]:
                return find_min(m+1, e)
            if nums[e] < nums[s]:
                return find_min(m+1, e)
            return min(find_min(s, m), find_min(m+1, e))

        return find_min(0, len(nums)-1)



@pytest.mark.parametrize('nums, expected', [
    ([1,3,5], 1),
    ([2,2,2,0,1], 0),
])
def test(nums, expected):
    assert expected == Solution().findMin(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
