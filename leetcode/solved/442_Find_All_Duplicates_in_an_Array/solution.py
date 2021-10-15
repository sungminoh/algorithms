#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:
Input: nums = [1,1,2]
Output: [1]
Example 3:
Input: nums = [1]
Output: []

Constraints:

	n == nums.length
	1 <= n <= 105
	1 <= nums[i] <= n
	Each element in nums appears once or twice.
"""
import sys
from typing import List
import pytest


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """05/01/2020 00:31"""
        for i, n in enumerate(nums):
            if n - 1 == i:
                continue
            while True:
                if n - 1 == i or nums[n - 1] == n:
                    nums[i] = n
                    break
                else:
                    tmp = nums[n - 1]
                    nums[n - 1] = n
                    n = tmp
        return [n for i, n in enumerate(nums) if n - 1 != i]

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for n in nums:
            idx = abs(n)-1
            if nums[idx] < 0:
                ret.append(abs(n))
            else:
                nums[idx] *= -1
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([1,1,2], [1]),
    ([1], []),
])
def test(nums, expected):
    assert expected == Solution().findDuplicates(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
