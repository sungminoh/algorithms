from collections import defaultdict
from functools import lru_cache

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have n dice, and each dice has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.

Constraints:

	1 <= n, k <= 30
	1 <= target <= 1000
"""
import pytest
import sys


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """10/21/2022 21:09
        Top down
        """
        @lru_cache(None)
        def dfs(n, target):
            if target < 0 or k*n < target:
                return 0
            if n == target:
                return 1
            return sum(dfs(n-1, target-i) for i in range(1, k+1))%int(1e9+7)

        return dfs(n, target)

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """10/21/2022 21:26
        Bottom up
        """
        MOD = int(1e9+7)
        dp = {0: 1}
        for i in range(n):
            _dp = defaultdict(int)
            for s, cnt in dp.items():
                if k*(n-i) + s < target:
                    continue
                if (n-i) + s > target:
                    continue
                if (n-i) + s == target:
                    _dp[s+1] += cnt
                    _dp[s+1] %= MOD
                    continue
                for j in range(1, k+1):
                    _dp[s+j] += cnt
                    _dp[s+j] %= MOD
            dp = _dp
        return dp.get(target, 0)

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Jan 27, 2024 14:47"""
        @lru_cache(None)
        def rec(n, remain):
            if n == 0:
                return 1 if remain == 0 else 0
            if remain <= 0:
                return 0
            return sum(rec(n-1, remain-i) for i in range(1, min(k, remain)+1)) % int(1e9+7)

        return rec(n, target)



@pytest.mark.parametrize('args', [
    ((1, 6, 3, 1)),
    ((2, 6, 7, 6)),
    ((30, 30, 500, 222616187)),
    ((1, 2, 3, 0)),
])
def test(args):
    assert args[-1] == Solution().numRollsToTarget(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
