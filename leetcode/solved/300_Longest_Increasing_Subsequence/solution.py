#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

	1 <= nums.length <= 2500
	-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
import sys
import bisect
from typing import List
import pytest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """11/05/2019 01:36"""
        if not nums:
            return 0
        lis = [1] * len(nums)
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[:i]):
                if m < n:
                    lis[i] = max(lis[i], lis[j] + 1)
        print(lis)
        return max(lis)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """11/05/2019 02:28"""
        if not nums:
            return 0

        def bisearch(arr, n):
            left, right = 0, len(arr) - 1
            while right - left >= 0:
                mid = left + (right - left) // 2
                if arr[mid] >= n:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        lis = [nums[0]]
        for n in nums[1:]:
            smaller_idx = self.bisearch(lis, n)
            if smaller_idx + 1 == len(lis):
                lis.append(n)
            elif lis[smaller_idx + 1] > n:
                lis[smaller_idx + 1] = n
        return len(lis)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DP
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        lis_ends_at = [1] * len(nums)
        for i, n in enumerate(nums):
            m = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, lis_ends_at[j] + 1)
            lis_ends_at[i] = m
        return max(lis_ends_at)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Construct LIS greedly
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        if not nums:
            return 0
        lis = [nums[0]]
        for i in range(1, len(nums)):
            j = bisect.bisect_left(lis, nums[i])
            if j == len(lis):
                lis.append(nums[i])
            else:
                if lis[j] > nums[i]:
                    lis[j] = nums[i]
        return len(lis)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """08/21/2022 15:18"""
        lis = []
        for n in nums:
            i = bisect.bisect_left(lis, n)
            if i == len(lis):
                lis.append(n)
            else:
                lis[i] = n
        return len(lis)


@pytest.mark.parametrize('nums, expected', [
    ([10,9,2,5,3,7,101,18], 4),
    ([0,1,0,3,2,3], 4),
    ([7,7,7,7,7,7,7], 1),
])
def test(nums, expected):
    assert expected == Solution().lengthOfLIS(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
