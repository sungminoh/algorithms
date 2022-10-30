#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

Input: nums = [2,1,2]
Output: 5

Example 2:

Input: nums = [1,2,1]
Output: 0

Constraints:

	3 <= nums.length <= 104
	1 <= nums[i] <= 106
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """10/29/2022 14:19"""
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i-2] < nums[i-1]+nums[i]:
                return sum(nums[i-2:i+1])
        return 0


@pytest.mark.parametrize('nums, expected', [
    ([2,1,2], 5),
    ([1,2,1], 0),
])
def test(nums, expected):
    assert expected == Solution().largestPerimeter(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
