#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

	1 <= nums.length <= 104
	-104 < nums[i], target < 104
	All the integers in nums are unique.
	nums is sorted in ascending order.
"""
from typing import List
import pytest
import sys


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Apr 05, 2022 21:09"""
        def binsearch(arr, x):
            s, e = 0, len(arr)-1
            while s <= e:
                m = s + ((e-s)//2)
                if arr[m] < x:
                    s = m+1
                elif arr[m] > x:
                    e = m-1
                else:
                    return m
            return -1
        return binsearch(nums, target)

    def search(self, nums: List[int], target: int) -> int:
        """Apr 23, 2023 22:43"""
        def bisearch(arr, x):
            s, e = 0, len(arr)-1
            while s <= e:
                m = s + (e-s)//2
                if arr[m] < x:
                    s = m+1
                else:
                    e = m-1
            return e+1

        i = bisearch(nums, target)
        return i if i < len(nums) and nums[i] == target else -1


@pytest.mark.parametrize('args', [
    (([-1,0,3,5,9,12], 9, 4)),
    (([-1,0,3,5,9,12], 2, -1)),
])
def test(args):
    assert args[-1] == Solution().search(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
