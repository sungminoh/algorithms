#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12

Constraints:

	2 <= nums.length <= 500
	1 <= nums[i] <= 10^3
"""
from heapq import heappush, heappushpop
from typing import List
import pytest
import sys


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Feb 03, 2024 18:10"""
        h = []
        for n in nums:
            if len(h) < 2:
                heappush(h, n)
            else:
                heappushpop(h, n)
        return (h[0]-1) * (h[1]-1)


@pytest.mark.parametrize('args', [
    (([3,4,5,2], 12)),
    (([1,5,4,5], 16)),
    (([3,7], 12)),
])
def test(args):
    assert args[-1] == Solution().maxProduct(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
