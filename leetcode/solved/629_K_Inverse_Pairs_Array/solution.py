#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Constraints:

	1 <= n <= 1000
	0 <= k <= 1000
"""
import itertools
from functools import lru_cache
import sys
import pytest


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @lru_cache(None)
        def dp(n, k):
            if n == 0:
                return 0
            if k == 0:
                return 1
            ret = 0
            for i in range(min(k+1, n)):
                ret += dp(n-1, k-i)
                ret %= int(1e9+7)
            return ret

        return dp(n, k)

    def kInversePairs(self, n: int, k: int) -> int:
        """
        (n, k) = sum_i_from_0_to_n-1 {(n-1, k-i)}
        In the summation, k-i varies from k-(n-1) to k when k > (n-1)
        Time complexity: O(n*k)
        Space complexity: O(n)
        """
        if n == 0:
            return 0
        if k == 0:
            return 1
        dp = [0]*(k+1)
        dp[0] = 1
        for i in range(2, n+1):
            cum = [0]
            for v in dp:
                cum.append((cum[-1] + v) % int(1e9+7))
            new_dp = []
            for j in range(k+1):
                # if i > j : dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][0]
                # if i <= j: dp[i-1][j] + dp[i-1][j-1] + ... + dp[j-(i-1)]
                if i > j:
                    ret = (cum[j+1] - cum[0]) % int(1e9+7)
                else:
                    ret = (cum[j+1] - cum[j-(i-1)]) % int(1e9+7)
                new_dp.append(ret)
            dp = new_dp
        return dp[k]


@pytest.mark.parametrize('n, k, expected', [
    (3, 0, 1),
    (3, 1, 2),
    (2, 2, 0),
    (10, 5, 1068),
    # (1000, 1000, 425360090),
])
def test(n, k, expected):
    print()
    assert expected == Solution().kInversePairs(n, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
