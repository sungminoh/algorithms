
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

	Each of the array element will not exceed 100.
	The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
import random
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s = s // 2

        @lru_cache(None)
        def dp(i, s):
            if s == 0:
                return True
            if s < 0 or i >= len(nums):
                return False
            return dp(i + 1, s - nums[i]) or dp(i + 1, s)

        return dp(0, s)

    def _canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s = s // 2

        @lru_cache(None)
        def dp(i, j, s):
            if s == 0:
                return True
            if i > j:
                return False
            return dp(i + 1, j, s) or dp(i, j - 1, s) or dp(i + 1, j, s - nums[i]) or dp(i, j - 1, s - nums[j])

        return dp(0, len(nums) - 1, s)


    def __canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s = s // 2

        def dfs(s, nums):
            if s == 0:
                return True
            if not nums:
                return False
            v = nums.pop()
            ans = dfs(s, nums) or dfs(s - v, nums)
            nums.append(v)
            return ans

        return dfs(s, nums[:])


def gen_case(n):
    nums = [random.randint(1, 100) for _ in range(n)]
    expected = Solution()._canPartition(nums)
    return nums, expected


@pytest.mark.parametrize('nums, expected', [
    ([1,5,11,5], True),
    ([1,2,3,5], False),
    # gen_case(200),
    ([55,49,68,50,25,8,85,42,11,32,2,91,30,48,66,11,28,41,20,1,54,48,18,47,42,23,42,67,71,90,15,49,21,25,43,65,73,76,10,44,14,5,97,30,39,31,90,2,78,37,5,47,3,23,47,45,53,3,77,92,32,34,73,65,28,73,19,52,2,46,41,96,14,51,50,48,30,22,15,35,29,61,79,25,64,2,20,24,4,62,20,71,9,14,88,66,81,87,29,99], True)
])
def test(nums, expected):
    assert expected == Solution().canPartition(nums)
