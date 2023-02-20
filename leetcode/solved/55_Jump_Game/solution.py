#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

	1 <= nums.length <= 104
	0 <= nums[i] <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def canJump(self, nums):
        """12/30/2017 20:17"""
        m = 0
        for i, n in enumerate(nums):
            if m == len(nums)-1:
                return True
            if n == 0 and m <= i:
                return False
            m = max(m, i+n)
        return True

    def canJump(self, nums: List[int]) -> bool:
        """Oct 13, 2021 11:16"""
        reachable = 0
        i = 0
        while i < len(nums):
            if i > reachable:
                break
            reachable = max(reachable, i + nums[i])
            if reachable >= len(nums)-1:
                return True
            i += 1
        return False

    def canJump(self, nums: List[int]) -> bool:
        """Feb 19, 2023 21:40"""
        m = 0
        i = 0
        while i < len(nums) and i <= m:
            m = max(m, i+nums[i])
            i += 1
        return m >= len(nums)-1


@pytest.mark.parametrize('nums, expected', [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
])
def test(nums, expected):
    assert expected == Solution().canJump(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
