#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

Constraints:

	1 <= nums.length <= 2 * 104
	1 <= nums[i] < 216
	1 <= k <= floor(nums.length / 3)
"""
from pathlib import Path
import json
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """11/28/2022 14:21
        TLE
        Top down recursion
        """
        i = 0
        sums = [0]
        while i < k:
            sums[0] += nums[i]
            i += 1
        while i < len(nums):
            sums.append(sums[-1] + nums[i] - nums[i-k])
            i += 1

        @lru_cache(None)
        def dp(i, n):
            if i >= len(sums) or n == 0:
                return [], 0
            if n == 1:
                idx = i
                val = sums[i]
                for j in range(i, len(sums)):
                    if sums[j] > val:
                        idx = j
                        val = sums[j]
                return [idx], val
            use_indexes, use_val = dp(i+k, n-1)
            use_val += sums[i]
            skip_indexes, skip_val = dp(i+1, n)
            if use_val >= skip_val:
                return [i, *use_indexes], use_val
            else:
                return skip_indexes, skip_val

        return dp(0, 3)[0]

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """11/28/2022 15:22
        Bottom up dp
        """
        i = 0
        sums = [0]
        while i < k:
            sums[0] += nums[i]
            i += 1
        while i < len(nums):
            sums.append(sums[-1] + nums[i] - nums[i-k])
            i += 1

        dp = [[(0, []) for _ in range(4)] for _ in range(len(sums))]
        for i in range(len(sums)):
            for n in range(1, len(dp[i])):
                use_val, use_indexes = dp[i-k][n-1]
                use_val += sums[i]
                skip_val, skip_indexes = dp[i-1][n]
                if use_val > skip_val:
                    dp[i][n] = use_val, [*use_indexes, i]
                else:
                    dp[i][n] = skip_val, skip_indexes
        return dp[-1][3][1]


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,1,2,6,7,5,1], 2, [0,3,5]),
    ([1,2,1,2,1,2,1,2,1], 2, [0,2,4]),
    (*json.load(open(Path(__file__).parent/'testcase.json')), [763, 7486, 16045])
])
def test(nums, k, expected):
    assert expected == Solution().maxSumOfThreeSubarrays(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
