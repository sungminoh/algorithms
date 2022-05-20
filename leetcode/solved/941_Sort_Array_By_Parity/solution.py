#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

	1 <= nums.length <= 5000
	0 <= nums[i] <= 5000
"""
import sys
from typing import List
import pytest


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x%2)
        return nums

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = j = 0
        while j < len(nums):
            if j < i:
                j += 1
            elif nums[j]%2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j += 1
        return nums


@pytest.mark.parametrize('nums, expected', [
    ([3,1,2,4], [2,4,3,1]),
    ([0], [0]),
])
def test(nums, expected):
    assert expected == Solution().sortArrayByParity(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
