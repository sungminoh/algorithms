#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The width of a sequence is the difference between the maximum and minimum elements in the sequence.

Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [2,1,3]
Output: 6
Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.

Example 2:

Input: nums = [2]
Output: 0

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 105
"""
from pathlib import Path
import json
import random
from typing import List
import pytest
import sys


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        """Sub Array case"""
        N = len(nums)
        mn = 0
        mx = 0
        increasing = []
        decreasing = []
        for i, n in enumerate(nums):
            while increasing and nums[increasing[-1]] >= n:
                j = increasing.pop()
                mn += (i-j) * (j - (increasing[-1] if increasing else -1)) * nums[j]  # min
            increasing.append(i)

            while decreasing and nums[decreasing [-1]] <= n:
                j = decreasing.pop()
                mx += (i-j) * (j - (decreasing[-1] if decreasing else -1)) * nums[j]  # max
            decreasing.append(i)

        while increasing:
            j = increasing.pop()
            mn += (N-j) * (j - (increasing[-1] if increasing else -1)) * nums[j]  # min
        while decreasing:
            j = decreasing.pop()
            mx += (N-j) * (j - (decreasing[-1] if decreasing else -1)) * nums[j]  # max

        MOD = int(1e9+7)
        return (mx-mn) % MOD

    def sumSubseqWidths(self, nums: List[int]) -> int:
        """Apr 24, 2024 20:15"""
        nums.sort()

        MOD = int(1e9+7)
        N = len(nums)
        p = pow(2, N-1)
        q = 1
        ret = 0
        for i in range(N):
            ret -= nums[i] * p
            ret += nums[i] * q
            ret %= MOD
            p //= 2
            q *= 2
        return ret


@pytest.mark.parametrize('args', [
    (([2,1,3], 6)),
    (([2], 0)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 126320753)),
])
def test(args):
    assert args[-1] == Solution().sumSubseqWidths(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
