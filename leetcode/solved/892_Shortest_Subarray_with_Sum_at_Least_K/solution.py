#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1
Example 2:
Input: nums = [1,2], k = 4
Output: -1
Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3

Constraints:

	1 <= nums.length <= 105
	-105 <= nums[i] <= 105
	1 <= k <= 109
"""
from pathlib import Path
import json
from collections import deque
import bisect
import itertools
from typing import List
import pytest
import sys


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """TLE"""
        sums = [(0, -1)]
        acc = 0
        ret = float('inf')
        for i in range(len(nums)):
            acc += nums[i]
            j = bisect.bisect_right(sums, (acc-k, i))
            for x in range(j):
                ret = min(ret, i-sums[x][1])
            sums.insert(bisect.bisect_left(sums, (acc, i)), (acc, i))
        return ret if ret < float('inf') else -1

    def _shortestSubarray(self, nums: List[int], k: int) -> int:
        """Apr 18, 2024 22:47"""
        ret = float('inf')
        queue = deque([(0, -1)])
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            while queue and acc-queue[0][0] >= k:
                ret = min(ret, i-queue.popleft()[1])
            while queue and queue[-1][0] >= acc:
                queue.pop()
            queue.append((acc, i))
        return ret if ret < float('inf') else -1


@pytest.mark.parametrize('args', [
    (([1], 1, 1)),
    (([1,2], 4, -1)),
    (([2,-1,2], 3, 3)),
    (([44,-25,75,-50,-38,-42,-32,-6,-40,-47], 19, 1)),
    (([84,-37,32,40,95], 167, 3)),
    ((*json.load(open(Path(__file__).parent/'testcase.json')), 25813)),
])
def test(args):
    assert args[-1] == Solution().shortestSubarray(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
