
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:
	1. The length of the array won't exceed 10,000.
	2. You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modulo_position = {0: -1}
        s = 0
        for i, n in enumerate(nums):
            s += n
            if k != 0:
                s %= k
            if s in modulo_position:
                if modulo_position[s] + 2 <= i:
                    return True
            else:
                modulo_position[s] = i
        return False

    def _checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumsum = [0]
        for i in range(len(nums)):
            if i == 0:
                cumsum.append(nums[i])
            else:
                cumsum.append(nums[i] + cumsum[-1])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = cumsum[j+1] - cumsum[i]
                if k == 0:
                    if s == 0:
                        return True
                else:
                    if s % k == 0:
                        return True
        return False


@pytest.mark.parametrize('nums, k, expected', [
    ([23,2,4,6,7], 6, True),
    ([23,2,6,4,7], 6, True),
    ([23,2,6,4,7], 0, False),
    ([23,2,4,6,7], -6, True),
    ([0,0], 0, True)
])
def test(nums, k, expected):
    assert expected == Solution().checkSubarraySum(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
