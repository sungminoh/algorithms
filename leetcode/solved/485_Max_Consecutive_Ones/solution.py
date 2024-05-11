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
from typing import List
import pytest
import sys


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Oct 04, 2021 11:27"""
        ret = 0
        cnt = 0
        for n in nums:
            if n == 1:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 0
        return ret

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """May 05, 2024 12:37"""
        ret = 0
        i = 0
        j = -1
        while i < len(nums):
            if nums[i] != 1:
                ret = max(ret, i-1-j)
                j = i
            i += 1
        ret = max(ret, i-1-j)
        return ret


@pytest.mark.parametrize('args', [
    (([1,1,0,1,1,1], 3)),
    (([1,0,1,1,0,1], 2)),
])
def test(args):
    assert args[-1] == Solution().findMaxConsecutiveOnes(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
