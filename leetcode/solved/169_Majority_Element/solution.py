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
from typing import List
import pytest
import sys


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Mar 03, 2022 16:13
        Time complexity: O(nlogn)
        Space complexity: O(1)
        """
        nums.sort()
        return nums[(len(nums)-1)//2]

    def majorityElement(self, nums: List[int]) -> int:
        """Mar 03, 2022 16:17
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

    def majorityElement(self, nums: List[int]) -> int:
        """Feb 19, 2024 14:52"""
        ret = None
        cnt = 0
        for n in nums:
            if cnt == 0:
                ret = n
            cnt += 1 if ret == n else -1
        return ret


@pytest.mark.parametrize('args', [
    (([3,2,3], 3)),
    (([2,2,1,1,1,2,2], 2)),
])
def test(args):
    assert args[-1] == Solution().majorityElement(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
