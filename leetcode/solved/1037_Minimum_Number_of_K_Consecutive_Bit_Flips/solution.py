#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

Constraints:

	1 <= nums.length <= 105
	1 <= k <= nums.length
"""
from collections import deque
from typing import List
import pytest
import sys


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """Apr 28, 2024 18:45"""
        N = len(nums)
        i = 0
        flips = deque([])
        ret = 0
        while i < N:
            while flips and flips[0] <= i-k:
                flips.popleft()
            if nums[i] ^ (len(flips) % 2) == 0:
                if i > N-k:
                    return -1
                flips.append(i)
                ret += 1
            i += 1
        return ret


@pytest.mark.parametrize('args', [
    (([0,1,0], 1, 2)),
    (([1,1,0], 2, -1)),
    (([0,0,0,1,0,1,1,0], 3, 3)),
])
def test(args):
    assert args[-1] == Solution().minKBitFlips(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
