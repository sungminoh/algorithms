#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Example 3:

Input: arr = [1], k = 1
Output: 1

Constraints:

	1 <= arr.length <= 500
	0 <= arr[i] <= 109
	1 <= k <= arr.length
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """Feb 05, 2024 22:08"""
        @lru_cache(None)
        def dp(i):
            if i == len(arr):
                return 0
            ret = 0
            m = arr[i]
            for j in range(k):
                if i+j >= len(arr): break
                m = max(m, arr[i+j])
                ret = max(ret, (j+1)*m + dp(i+j+1))
            return ret

        return dp(0)


@pytest.mark.parametrize('args', [
    (([1,15,7,9,2,5,10], 3, 84)),
    (([1,4,1,5,7,3,6,1,9,9,3], 4, 83)),
    (([1], 1, 1)),
])
def test(args):
    assert args[-1] == Solution().maxSumAfterPartitioning(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
