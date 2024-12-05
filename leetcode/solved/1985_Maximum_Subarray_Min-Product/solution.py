#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

	For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.

Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 107
"""
from itertools import accumulate
from typing import List
import pytest
import sys


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        """Dec 05, 2024 12:24"""
        MOD = int(1e9+7)
        cumsum = list(accumulate(nums, initial=0))
        ret = 0
        stack = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                j = stack.pop()
                ret = max(ret, (cumsum[i] - cumsum[(stack[-1]+1) if stack else 0]) * nums[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            ret = max(ret, (cumsum[-1] - cumsum[(stack[-1]+1) if stack else 0]) * nums[j])
        return ret % MOD


@pytest.mark.parametrize('args', [
    (([1,2,3,2], 14)),
    (([2,3,3,1,2], 18)),
    (([3,1,5,6,4,2], 60)),
])
def test(args):
    assert args[-1] == Solution().maxSumMinProduct(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
