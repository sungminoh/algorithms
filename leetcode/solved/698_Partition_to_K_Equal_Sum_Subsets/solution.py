#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:

	1 <= k <= nums.length <= 16
	1 <= nums[i] <= 104
	The frequency of each element is in the range [1, 4].
"""
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """08/29/2020 11:07"""
        q, r = divmod(sum(nums), k)
        if r > 0 or q == 0:
            return False

        @lru_cache(None)
        def fill(i, remainders):
            remainders = list(remainders)
            if i == -1:
                return True
            for j in range(len(remainders)):
                if remainders[j] < nums[i]:
                    break
                remainders[j] -= nums[i]
                if fill(i-1, tuple(sorted(remainders, key=lambda x: -x))):
                    return True
                remainders[j] += nums[i]
                if remainders[j] == 0:
                    break
            return False

        nums.sort()
        if nums[-1] > q:
            return False

        while nums and nums[-1] == q:
            nums.pop()
            k -= 1

        return fill(len(nums)-1, tuple([q] * k))

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)
        if r != 0:
            return False

        nums.sort(reverse=True)
        partitions = [q]*k
        def dfs(i):
            if i == len(nums):
                return True
            for j, partition in enumerate(partitions):
                if partition >= nums[i]:
                    partitions[j] -= nums[i]
                    if dfs(i+1):
                        return True
                    partitions[j] += nums[i]
            return False

        return dfs(0)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)
        if r != 0:
            return False

        nums.sort(reverse=True)

        if nums[0] > q:
            return False

        while nums and nums[0] == q:
            nums.pop(0)
            k -= 1

        @lru_cache(None)
        def dfs(i, partitions):
            partitions = list(partitions)
            if i == len(nums):
                return True
            for j, partition in enumerate(partitions):
                if partition >= nums[i]:
                    partitions[j] -= nums[i]
                    if dfs(i+1, tuple(sorted([x for x in partitions if x != 0], reverse=True))):
                        return True
                    partitions[j] += nums[i]
                else:
                    break
            return False

        return dfs(0, tuple([q]*k))


@pytest.mark.parametrize('nums, k, expected', [
    ([4,3,2,3,5,2,1], 4, True),
    ([1,2,3,4], 3, False),
    ([730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], 4, True),
    ([18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037], 4, True),
    ([2,2,2,2,3,4,5], 4, False),
])
def test(nums, k, expected):
    assert expected == Solution().canPartitionKSubsets(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
