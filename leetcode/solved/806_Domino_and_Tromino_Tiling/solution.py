#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:

Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1

Constraints:

	1 <= n <= 1000
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def numTilings(self, N: int) -> int:
        """12/16/2021 23:42"""
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        s = 1
        ret = [1, 1, 2]
        for i in range(3, N+1):
            ret[i%3] = (ret[i%3-1] + ret[i%3-2] + 2*s) % (1e9+7)
            s += ret[i%3-2]
            s %= 1e9+7
        return int(ret[N%3] % (1e9+7))

    @lru_cache(None)
    def numTilings(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        ret = self.numTilings(n-1) + self.numTilings(n-2)
        for i in range(n-2):
            ret += 2*self.numTilings(i)
            ret %= 1e9+7
        return int(ret)

    def numTilings(self, n: int) -> int:
        dp = [1, 1, 2, 5]
        for i in range(4, n+1):
            ret = dp[-1] + dp[-2]
            for j in range(i-2):
                ret += 2*dp[j]
                ret %= 1e9+7
            dp.append(int(ret))
        return dp[n]


@pytest.mark.parametrize('n, expected', [
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 11),
    (5, 24),
    (30, 312342182),
    (60, 882347204)
])
def test(n, expected):
    assert expected == Solution().numTilings(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
