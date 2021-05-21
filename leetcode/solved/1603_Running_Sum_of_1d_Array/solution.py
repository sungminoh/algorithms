#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

	1 <= nums.length <= 1000
	-10^6 <= nums[i] <= 10^6
"""
import sys
from typing import List
import pytest


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = [0]
        for n in nums:
            ret.append(ret[-1]+n)
        return ret[1:]


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4], [1,3,6,10]),
    ([1,1,1,1,1], [1,2,3,4,5]),
    ([3,1,2,10,1], [3,4,6,16,17]),
])
def test(nums, expected):
    assert expected == Solution().runningSum(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
