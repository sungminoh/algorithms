#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
import sys
from typing import List
import pytest


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        p = 1
        i = j = 0
        while j < len(nums):
            p *= nums[j]
            while p >= k and i <= j:
                p //= nums[i]
                i += 1
            cnt += j-i+1
            j += 1
        return cnt

    def _numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        cnt = 0
        p = nums[0]
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if p < k:
                cnt += j-i+1
                j += 1
                if j < len(nums):
                    p *= nums[j]
            else:
                p //= nums[i]
                i += 1

        return cnt


@pytest.mark.parametrize('nums, k, expected', [
    ([10, 5, 2, 6], 100, 8),
])
def test(nums, k, expected):
    assert expected == Solution().numSubarrayProductLessThanK(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
