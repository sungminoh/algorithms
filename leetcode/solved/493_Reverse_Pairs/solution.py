#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

Note:

The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
import sys
import bisect
from typing import List
import pytest


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        s = []
        for i, n in enumerate(nums):
            j = bisect.bisect_right(s, 2*n)
            cnt += len(s) - j
            bisect.insort(s, n)
        return cnt


@pytest.mark.parametrize('nums, expected', [
    ([1,3,2,3,1], 2),
    ([2,4,3,5,1], 3),
])
def test(nums, expected):
    assert expected == Solution().reversePairs(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
