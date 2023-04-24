#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

Constraints:

	1 <= nums.length <= 105
	-109 <= nums[i] <= 109
"""
from typing import List
import pytest
import sys


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret = 0
        zero_cnt = 0
        for n in nums:
            if n != 0:
                ret += zero_cnt * (zero_cnt+1) // 2
                zero_cnt = 0
            else:
                zero_cnt += 1
        ret += zero_cnt * (zero_cnt+1) // 2
        return ret


@pytest.mark.parametrize('args', [
    (([1,3,0,0,2,0,0,4], 6)),
    (([0,0,0,2,0,0], 9)),
    (([2,10,2019], 0)),
])
def test(args):
    assert args[-1] == Solution().zeroFilledSubarray(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
