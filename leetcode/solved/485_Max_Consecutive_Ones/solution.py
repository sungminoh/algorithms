#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
"""
import sys
from typing import List
import pytest


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 0
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1,1,0,1,1,1], 3),
    ([1,0,1,1,0,1], 2),
])
def test(nums, expected):
    assert expected == Solution().findMaxConsecutiveOnes(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
