#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: k = 1, n = 2
Output: 2
Explanation:
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example 2:

Input: k = 2, n = 6
Output: 3

Example 3:

Input: k = 3, n = 14
Output: 4

Constraints:

	1 <= k <= 100
	1 <= n <= 104
"""
import bisect
from functools import lru_cache
import math
import pytest
import sys


class Solution:
    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        """TLE"""
        if n == 0:
            return 0
        if k == 1:
            return n
        ret = float('inf')
        for i in range(1, n+1):
            ret = min(ret, 1 + max(self.superEggDrop(k-1, i-1), self.superEggDrop(k, n-i)))
        return ret

    def superEggDrop(self, k: int, n: int) -> int:
        """Bottom up"""
        dp = [[0] * (n+1) for _ in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, n+1):
                if i == 1:
                    dp[i][j] = j
                else:
                    dp[i][j] = float('inf')
                    for x in range(1, j+1):
                        dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x-1], dp[i][j-x]))

        return dp[k][n]

    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        """Apr 24, 2024 18:59"""
        if n == 0:
            return 0
        if k == 1:
            return n
        ret = float('inf')
        s, e = 1, n
        while s <= e:
            m = s + (e-s)//2
            if self.superEggDrop(k-1, m-1) < self.superEggDrop(k, n-m):
                s = m+1
            else:
                e = m-1

        i = e+1
        return 1 + max(self.superEggDrop(k-1, i-1), self.superEggDrop(k, n-i))



@pytest.mark.parametrize('args', [
    ((1, 2, 2)),
    ((2, 6, 3)),
    ((3, 14, 4)),
    ((4, 5000, 19)),
])
def test(args):
    assert args[-1] == Solution().superEggDrop(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
