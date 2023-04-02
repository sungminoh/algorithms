#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums contains distinct values sorted in ascending order.
	-104 <= target <= 104
"""
from typing import List
import pytest
import sys


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Dec 03, 2021 13:53"""
        def bisearch(s, e):
            while s <= e:
                m = s + (e-s)//2
                if nums[m] < target:
                    s = m+1
                elif nums[m] > target:
                    e = m-1
                else:
                    return m
            return s

        return bisearch(0, len(nums)-1)

    def searchInsert(self, nums: List[int], target: int) -> int:
        """Mar 22, 2023 00:17"""
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return r+1


@pytest.mark.parametrize('args', [
    (([1,3,5,6], 5, 2)),
    (([1,3,5,6], 2, 1)),
    (([1,3,5,6], 7, 4)),
    ([1], 0, 0),
])
def test(args):
    assert args[-1] == Solution().searchInsert(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
