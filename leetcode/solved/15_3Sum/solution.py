#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []

Constraints:

	0 <= nums.length <= 3000
	-105 <= nums[i] <= 105
"""
import sys
from collections import defaultdict
from collections import Counter
from typing import List
import pytest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^3)
        """
        N = len(nums)

        m = defaultdict(list)
        for i, n in enumerate(nums):
            m[n].append(i)

        visited = set()
        ret = []
        for i in range(N-1):
            for j in range(i+1, N):
                target = -(nums[i] + nums[j])
                key = tuple(sorted([nums[i], nums[j], target]))
                if key in visited:
                    continue
                visited.add(key)
                if target in m and m[target][-1] > j:
                    ret.append([nums[i], nums[j], target])

        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity: O(n^2)
        Space complexity: O(1)  Exclude return
        """
        nums.sort()
        N = len(nums)
        ret = []
        for i in range(N-2):
            l, r = i+1, N-1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ret.append((nums[i], nums[l], nums[r]))
                    while (l < r) and nums[l] == ret[-1][1]:
                        l += 1
                    while (l < r) and nums[r] == ret[-1][2]:
                        r -= 1
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([], []),
    ([0], []),
])
def test(nums, expected):
    assert sorted([sorted(x) for x in expected]) == sorted([sorted(x) for x in Solution().threeSum(nums)])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
