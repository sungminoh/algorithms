
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Example 3:
Input: nums = [3,3,7,7,10,10,11]
Output: 11

Constraints:
    1. 1 <= nums.length <= 10^5
    2. 0 <= nums[i] <= 10^5
"""
import sys
from typing import List
import pytest



class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            m = i + (j-i)//2  # 2k or 2k+1
            e = 2 * (m // 2)
            o = e + 1
            if nums[e] == nums[o]:
                i = o + 1
            else:
                j = e - 1
        return nums[i]


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2,3,3,4,4,8,8], 2),
    ([3,3,7,7,10,11,11], 10),
    ([3,3,7,7,10,10,11], 11),
])
def test(nums, expected):
    assert expected == Solution().singleNonDuplicate(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
