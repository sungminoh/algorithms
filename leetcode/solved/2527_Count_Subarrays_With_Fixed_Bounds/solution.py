#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

	The minimum value in the subarray is equal to minK.
	The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:

	2 <= nums.length <= 105
	1 <= nums[i], minK, maxK <= 106
"""
from typing import List
import pytest
import sys


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        oob = -1
        mni = -1
        mxi = -1
        ret = 0
        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                oob = i
            if n == minK:
                mni = i
            if n == maxK:
                mxi = i
            ret += max(0, min(mni, mxi) - oob)
        return ret


@pytest.mark.parametrize('args', [
    (([1,3,5,2,7,5], 1, 5, 2)),
    (([1,1,1,1], 1, 1, 10)),
    (([35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913],
      35054, 945315, 81)),
])
def test(args):
    assert args[-1] == Solution().countSubarrays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
