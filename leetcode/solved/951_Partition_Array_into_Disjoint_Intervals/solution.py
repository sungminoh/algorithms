#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

	Every element in left is less than or equal to every element in right.
	left and right are non-empty.
	left has the smallest possible size.

Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

Constraints:

	2 <= nums.length <= 105
	0 <= nums[i] <= 106
	There is at least one valid answer for the given input.
"""
import sys
from typing import List
import pytest


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(2*n)
        """
        if not nums:
            return 0
        left_max = [nums[0]]
        for n in nums[1:]:
            left_max.append(max(left_max[-1], n))

        right_min = [nums[-1]]
        for n in reversed(nums[:-1]):
            right_min.append(min(right_min[-1], n))
        right_min.reverse()

        for i in range(len(left_max)-1):
            l = left_max[i]
            r = right_min[i+1]
            if l <= r:
                return i+1
        return -1

    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not nums:
            return 0
        right_min = [nums[-1]]
        for n in reversed(nums[:-1]):
            right_min.append(min(right_min[-1], n))
        right_min.reverse()

        left_max = -float('inf')
        for i, n in enumerate(nums[:-1], 1):
            left_max = max(left_max, n)
            if left_max <= right_min[i]:
                return i
        return -1


@pytest.mark.parametrize('nums, expected', [
    ([5,0,3,8,6], 3),
    ([1,1,1,0,6,12], 4),
    ([26,51,40,58,42,76,30,48,79,91], 1),
    ([1,1], 1),
])
def test(nums, expected):
    print()
    assert expected == Solution().partitionDisjoint(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
