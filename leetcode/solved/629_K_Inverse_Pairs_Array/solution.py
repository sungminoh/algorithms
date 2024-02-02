import itertools
from functools import lru_cache

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
import pytest
import sys


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
        """07/18/2021 00:22
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

    @lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        """TLE, Maximum Recursion"""
        MOD = int(1e9+7)
        m = n*(n-1)//2
        if k < 0 or k > m:
            return 0
        if k == 0 or k == m:
            return 1

        ret = 0
        for i in range(min(n, k+1)):
            ret += self.kInversePairs(n-1, k-i)
            ret %= MOD
        return ret

    def kInversePairs(self, n: int, k: int) -> int:
        """
        Time Complexity: O(n*k)
        Space Complexity: O(k)
        """
        MOD = int(1e9+7)
        dp = [0]*(k+1)
        for i in range(1, n+1):
            m = i*(i-1)//2
            # init
            _dp = [0]*(k+1)
            _dp[0] = 1
            if len(_dp) > m:
                _dp[m] = 1
            # update
            s = dp[0]
            for j in range(1, min(m, k+1)):
                # (i, j) -> sum from j-min(i-1, j) ~ j
                s += dp[j]
                if i-1 < j:
                    s -= dp[j-i]
                s %= MOD
                _dp[j] = s
            dp = _dp
        return dp[-1]

    @lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        """Feb 01, 2024 19:49 TLE"""
        if k == 0:
            return 1
        if n == 0:
            return 0

        return sum(self.kInversePairs(n-1, k-i) for i in range(min(n, k+1))) % int(1e9+7)

    def kInversePairs(self, n: int, k: int) -> int:
        """Feb 01, 2024 20:21 TLE (bottom up)"""
        cnt = [0]*(k+1)
        cnt[0] = 1
        for i in range(1, n+1):
            _cnt = [0]*(k+1)
            for j in range(min(i, k+1)):
                for l in range(j, k+1):
                    _cnt[l] += cnt[l-j]
                    _cnt[l] %= int(1e9+7)
            cnt = _cnt
        return cnt[-1]

    def kInversePairs(self, n: int, k: int) -> int:
        """Feb 01, 2024 20:40"""
        cnt = [0]*(k+1)
        cnt[0] = 1
        acc = list(itertools.accumulate(cnt))
        for i in range(1, n+1):
            _cnt = [0]*(k+1)
            for j in range(k+1):
                # sum from cnt[j] to cnt[j-(i-1)]
                _cnt[j] = acc[j] - (acc[j-(i-1)-1] if j-(i-1)-1>=0 else 0)
            cnt = [x%int(1e9+7) for x in _cnt]
            acc = list(itertools.accumulate(cnt))
        return cnt[-1]


@pytest.mark.parametrize('args', [
    ((3, 0, 1)),
    ((3, 1, 2)),
    (3, 2, 2),
    (2, 2, 0),
    (4, 0, 1),
    (4, 1, 3),
    (4, 2, 5),
    (4, 3, 6),
    (4, 4, 5),
    (4, 5, 3),
    (4, 6, 1),
    (10, 3, 155),
    (10, 4, 440),
    (10, 5, 1068),
    ((1000, 1000, 663677020)),
])
def test(args):
    assert args[-1] == Solution().kInversePairs(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
