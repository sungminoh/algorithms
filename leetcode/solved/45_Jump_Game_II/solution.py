#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

	1 <= nums.length <= 1000
	0 <= nums[i] <= 105
"""
import sys
from typing import List
import pytest


class Solution:
    def jump(self, nums):
        """08/07/2018 06:05"""
        if not nums or len(nums) == 1:
            return 0
        if nums[0]+1 >= len(nums):
            return 1
        memo = [float('inf') for _ in range(len(nums))]
        memo[0] = 0
        m = 1
        for i, n in enumerate(nums):
            for j in range(m, min(len(nums), i+n+1)):
                memo[j] = min(memo[j], memo[i]+1)
            m = max(m, i+n)
        return memo[-1]

    def jump(self, nums):
        """08/10/2018 18:13	"""
        if len(nums) == 1:
            return 0
        farthest = 0
        previous = 0
        i = 0
        cnt = 0
        while i < len(nums):
            while i <= previous:
                farthest = max(farthest, i + nums[i])
                i += 1
            if farthest <= previous:
                break
            previous = farthest
            cnt += 1
            if farthest >= len(nums)-1:
                return cnt
        return -1

    def jump(self, nums: List[int]) -> int:
        """DP
        Time complexity: O(n*m)
        Space complexity: O(n)
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i, n in enumerate(nums[:-1]):
            for j in range(1, n+1):
                if i+j >= len(nums):
                    break
                dp[i+j] = min(dp[i+j], dp[i]+1)
        return dp[-1]

    def jump(self, nums: List[int]) -> int:
        """BFS
        Time complexity: O(n)
        Space complexity: O(1)
        """
        end = 0
        far = 0
        cnt = 0
        for i, n in enumerate(nums[:-1]):
            far = max(far, i+n)
            if i == end:
                cnt += 1
                end = far
            if end >= len(nums)-1:
                return cnt
        return cnt


@pytest.mark.parametrize('nums, expected', [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
    ([2,1], 1),
    ([1,2,3], 2),
])
def test(nums, expected):
    assert expected == Solution().jump(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

