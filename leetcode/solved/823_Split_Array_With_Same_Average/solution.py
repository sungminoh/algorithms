#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

Example 1:

Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

Example 2:

Input: nums = [3,1]
Output: false

Constraints:

	1 <= nums.length <= 30
	0 <= nums[i] <= 104
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        N = len(nums)
        avg = sum(nums)/N

        @lru_cache(None)
        def dp(i, acc, cnt):
            if i == N:
                return False
            if cnt > 0 and acc/cnt == avg:
                return True
            return dp(i+1, acc+nums[i], cnt+1) or dp(i+1, acc, cnt)

        return dp(0, 0, 0)

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """Apr 23, 2024 22:49"""
        S = sum(nums)
        N = len(nums)
        acc_cnt = set([(0, 0)])
        for n in nums:
            new = set()
            for acc, cnt in acc_cnt:
                if cnt > 0 and acc*N == S*cnt:
                    return True
                new.add((acc+n, cnt+1))
            acc_cnt.update(new)
        return False


@pytest.mark.parametrize('args', [
    (([1,2,3,4,5,6,7,8], True)),
    (([3,1], False)),
    (([6,8,18,3,1], False)),
    (([904,8738,6439,1889,138,5771,8899,5790,662,8402,3074,1844,5926,8720,7159,6793,7402,9466,1282,1748,434,842,22], False)),
    (([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5], True)),
])
def test(args):
    assert args[-1] == Solution().splitArraySameAverage(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
