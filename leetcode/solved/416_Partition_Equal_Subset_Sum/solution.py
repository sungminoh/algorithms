#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= 100
"""
import random
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        nums.sort(reverse=True)

        @lru_cache(None)
        def napsack(i, s):
            if s == 0:
                return True
            if s < 0 or i == len(nums):
                return False
            return napsack(i+1, s - nums[i]) or napsack(i+1, s)

        return napsack(0, s//2)


def gen_case(n):
    nums = [random.randint(1, 100) for _ in range(n)]
    expected = Solution()._canPartition(nums)
    return nums, expected


@pytest.mark.parametrize('nums, expected', [
    ([1,5,11,5], True),
    ([1,2,3,5], False),
    ([55,49,68,50,25,8,85,42,11,32,2,91,30,48,66,11,28,41,20,1,54,48,18,47,42,23,42,67,71,90,15,49,21,25,43,65,73,76,10,44,14,5,97,30,39,31,90,2,78,37,5,47,3,23,47,45,53,3,77,92,32,34,73,65,28,73,19,52,2,46,41,96,14,51,50,48,30,22,15,35,29,61,79,25,64,2,20,24,4,62,20,71,9,14,88,66,81,87,29,99], True)
])
def test(nums, expected):
    assert expected == Solution().canPartition(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
