#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

	0 <= j <= nums[i] and
	i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

	1 <= nums.length <= 104
	0 <= nums[i] <= 1000
	It's guaranteed that you can reach nums[n - 1].
"""
from heapq import heappop, heappush
from typing import List
import pytest
import sys


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

    def jump(self, nums: List[int]) -> int:
        """Mar 19, 2023 12:31
        TLE
        """
        visited = [False]*len(nums)
        visited[0] = True
        q = [(0, 0)]
        while q:
            j, ni = heappop(q)
            if -ni >= len(nums)-1:
                return j
            for i in range(-ni+1, -ni + nums[-ni]+1):
                heappush(q, (j+1, -i))
        return -1

    def jump(self, nums: List[int]) -> int:
        """Mar 19, 2023 12:37"""
        m = 0
        e = 0
        j = 0
        for i, n in enumerate(nums):
            if e >= len(nums)-1:
                return j
            m = max(m, i+n)
            if i == e:
                j += 1
                e = m
        return -1


@pytest.mark.parametrize('args', [
    (([2,3,1,1,4], 2)),
    (([2,3,0,1,4], 2)),
    (([0], 0)),
    (([1,2,0,1], 2)),
    (([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5], 13)),
])
def test(args):
    assert args[-1] == Solution().jump(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
