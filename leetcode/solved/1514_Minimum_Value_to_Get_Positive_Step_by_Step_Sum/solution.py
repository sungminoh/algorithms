#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.

Example 3:

Input: nums = [1,-2,-3]
Output: 5

Constraints:

	1 <= nums.length <= 100
	-100 <= nums[i] <= 100
"""
import sys
from typing import List
import pytest


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = 0
        acc = 0
        for n in nums:
            acc += n
            mn = min(mn, acc)
        return (-mn+1) if mn < 0 else 1


@pytest.mark.parametrize('nums, expected', [
    ([-3,2,-3,4,2], 5),
    ([1,2], 1),
    ([1,-2,-3], 5),
])
def test(nums, expected):
    assert expected == Solution().minStartValue(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
