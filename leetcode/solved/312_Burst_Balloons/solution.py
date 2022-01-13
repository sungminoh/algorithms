#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:

Input: nums = [1,5]
Output: 10

Constraints:

	n == nums.length
	1 <= n <= 500
	0 <= nums[i] <= 100
"""
from collections import defaultdict
from pathlib import Path
import json
import sys
from functools import cache
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """Brute-force TLE"""
        def adjmul(arr, i):
            ret = arr[i]
            if 0 < i:
                ret *= arr[i-1]
            if i < len(arr)-1:
                ret *= arr[i+1]
            return ret

        @lru_cache(None)
        def dp(nums):
            ret = 0
            for i in range(len(nums)):
                cur = adjmul(nums, i)
                sub = dp(tuple(nums[:i] + nums[i+1:]))
                ret = max(ret, cur+sub)
            return ret

        return dp(tuple(nums))

    def maxCoins(self, nums: List[int]) -> int:
        """
        Top-down DP, Recursive
        Time complexity: O(n^3)
        Space complexity: O(n^2)
        """
        def mul(a, b, c):
            ret = nums[b]
            if 0 <= a:
                ret *= nums[a]
            if c < len(nums):
                ret *= nums[c]
            return ret

        @lru_cache(None)
        def dp(i, j):
            ret = 0
            for k in range(i, j+1):
                # burst kth for the last
                l = dp(i, k-1)
                r = dp(k+1, j)
                c = mul(i-1, k, j+1)
                ret = max(ret, l+r+c)
            return ret

        return dp(0, len(nums)-1)

    def maxCoins(self, nums: List[int]) -> int:
        """
        Bottom-up DP
        Time complexity: O(n^3)
        Space complexity: O(n^2)
        """
        nums = [1] + nums + [1]
        N = len(nums)
        memo = [[0] * N for _ in range(N)]

        for d in range(N-1):
            for i in range(1, N-1-d):
                j = i+d
                memo[i][j] = max(
                    memo[i][ k-1] + memo[k+1][j] \
                    + nums[k] * nums[i-1] * nums[j+1]
                    for k in range(i, j+1))

        return memo[1][N-2]

    def maxCoins(self, nums: List[int]) -> int:
        """
        Bottom-up DP considering locality
        Time complexity: O(n^3)
        Space complexity: O(n^2)
        """
        nums = [1] + nums + [1]
        N = len(nums)
        memo = [[0] * N for _ in range(N)]
        for i in range(N-3, -1, -1):
            for j in range(i+2, N):
                memo[i][j] = max(
                    memo[i][k] + memo[k][j] \
                    + nums[i]*nums[k]*nums[j]
                    for k in range(i+1, j))
        return memo[0][N-1]


@pytest.mark.parametrize('nums, expected', [
    ([3,1,5,8], 167),
    ([1,5], 10),
    ([8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2], 3394),
    (json.load(open(Path(__file__).parent/'testcase.json')), 498010100),
])
def test(nums, expected):
    assert expected == Solution().maxCoins(nums)


if __name__ == '__main__':
   sys.exit(pytest.main(["-s", "-v"] + sys.argv))
