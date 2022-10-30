#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

	1 <= nums.length <= 5 * 105
	-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
import bisect
from typing import List
import pytest
import sys


class Solution:
    def brute(self, nums):
        mins = [nums[0]]
        maxs = [nums[-1]]
        for n in nums[1:]:
            if n < mins[-1]:
                mins.append(n)
            else:
                mins.append(mins[-1])
        for n in nums[:-2:-1]:
            if n > maxs[-1]:
                maxs.append(n)
            else:
                maxs.append(maxs[-1])
        maxs = maxs[::-1]
        for mi, n, ma in zip(mins, nums, maxs):
            if mi < n < ma:
                return True
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        """04/07/2020 17:56"""
        if len(nums) < 3:
            return False
        mins = [float('inf'), None]
        for n in nums:
            if n < mins[0]:
                mins[0] = n
            elif n > mins[0]:
                if mins[1] is None:
                    mins[1] = n
                elif n > mins[1]:
                    return True
                else:
                    mins[1] = n
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        """10/29/2022 14:30"""
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
                if len(stack) == 3:
                    return True
            stack[bisect.bisect_left(stack, n)] = n
        return False


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4,5], True),
    ([5,4,3,2,1], False),
    ([2,1,5,0,4,6], True),
])
def test(nums, expected):
    assert expected == Solution().increasingTriplet(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
