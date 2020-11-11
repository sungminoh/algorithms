#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""

import pytest
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mins = [float('inf'), None]
        for n in nums:
            if n < mins[0]:
                mins[0] = n
            elif n > mins[0]:
                if mins[1] is None:
                    mins[1] = n
                elif n > mins[1]:
                    return True
                else:
                    mins[1] = n
        return False

    def brute(self, nums):
        mins = [nums[0]]
        maxs = [nums[-1]]
        for n in nums[1:]:
            if n < mins[-1]:
                mins.append(n)
            else:
                mins.append(mins[-1])
        for n in nums[:-2:-1]:
            if n > maxs[-1]:
                maxs.append(n)
            else:
                maxs.append(maxs[-1])
        maxs = maxs[::-1]
        for mi, n, ma in zip(mins, nums, maxs):
            if mi < n < ma:
                return True
        return False


@pytest.mark.parametrize('nums', [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,1,-2,6]
])
def test(nums):
    s = Solution()
    sol = s.brute(nums)
    print(sol)
    assert sol == s.increasingTriplet(nums)

