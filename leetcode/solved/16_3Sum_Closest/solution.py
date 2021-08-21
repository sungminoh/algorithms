#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0

Constraints:

	3 <= nums.length <= 1000
	-1000 <= nums[i] <= 1000
	-104 <= target <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        min_sum = None
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                diff = abs(target-cur_sum)
                if diff < min_diff:
                    min_diff = diff
                    min_sum = cur_sum
                if cur_sum > target:
                    k -= 1
                elif cur_sum < target:
                    j += 1
                else:
                    return cur_sum
        return min_sum


@pytest.mark.parametrize('nums, target, expected', [
    ([-1,2,1,-4], 1, 2),
    ([0,0,0], 1, 0),
])
def test(nums, target, expected):
    assert expected == Solution().threeSumClosest(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
