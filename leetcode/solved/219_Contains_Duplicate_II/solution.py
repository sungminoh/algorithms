#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

	1 <= nums.length <= 105
	-109 <= nums[i] <= 109
	0 <= k <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """11/05/2022 17:42"""
        counter = {}
        i = j = 0
        while i < len(nums):
            while i-j > k:
                counter[nums[j]] -= 1
                j += 1
            if counter.get(nums[i], 0) > 0:
                return True
            counter.setdefault(nums[i], 0)
            counter[nums[i]] += 1
            i += 1
        return False


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,1], 3, True),
    ([1,0,1,1], 1, True),
    ([1,2,3,1,2,3], 2, False),
])
def test(nums, k, expected):
    assert expected == Solution().containsNearbyDuplicate(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
