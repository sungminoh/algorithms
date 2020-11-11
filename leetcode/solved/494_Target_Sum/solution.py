
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def rec(i, s):
            if i == len(nums):
                return 1 if s == 0 else 0
            return rec(i + 1, s - nums[i]) + rec(i + 1, s + nums[i])
        return rec(0, S)


@pytest.mark.parametrize('nums, S, expected', [
    ([1,1,1,1,1], 3, 5)
])
def test(nums, S, expected):
    assert expected == Solution().findTargetSumWays(nums, S)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
