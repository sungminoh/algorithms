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
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:

	3 <= nums.length <= 500
	-1000 <= nums[i] <= 1000
	-104 <= target <= 104
"""
import bisect
from typing import List
import pytest
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """08/19/2021 12:26
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
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

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """10/21/2022 20:30
        Time Complexity: O(n^2*logn)
        Space Complexity: O(1)
        """
        gap = float('inf')
        ret = 0
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                k = bisect.bisect(nums, target - s, lo=j+1)
                indexes = []
                if k < len(nums):
                    indexes.append(k)
                if k-1 >= 0 and k-1 not in (i, j):
                    indexes.append(k-1)
                for _k in indexes:
                    g = abs(s + nums[_k] - target)
                    if g < gap:
                        gap = g
                        ret = s + nums[_k]
        return ret


@pytest.mark.parametrize('nums, target, expected', [
    ([-1,2,1,-4], 1, 2),
    ([0,0,0], 1, 0),
])
def test(nums, target, expected):
    assert expected == Solution().threeSumClosest(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
