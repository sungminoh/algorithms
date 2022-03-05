#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

	n == nums.length
	1 <= n <= 5 * 104
	-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
import sys
from typing import List
import pytest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(nlogn)
        Space complexity: O(1)
        """
        nums.sort()
        return nums[(len(nums)-1)//2]

    def majorityElement(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        major = nums[0]
        cnt = 0
        for n in nums:
            if n == major:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    major = n
                    cnt = 1
        return major


@pytest.mark.parametrize('nums, expected', [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
])
def test(nums, expected):
    assert expected == Solution().majorityElement(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
