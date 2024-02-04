#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:

	1 <= n <= 5000
"""
from functools import lru_cache
import pytest
import sys
sys.setrecursionlimit(50000)


class Solution:
    def knightDialer(self, n: int) -> int:
        """Feb 04, 2024 11:03"""
        MOD = int(1e9+7)
        possibles = [
            [4, 6],  # 0
            [8, 6],  # 1
            [7, 9],  # 2
            [4, 8],  # 3
            [3, 9, 0],  # 4
            [],  # 5
            [1, 7, 0],  # 6
            [2, 6],  # 7
            [1, 3],  # 8
            [2, 4],  # 9
        ]
        @lru_cache(None)
        def dp(start, remaining):
            if remaining == 1:
                return 1
            if not possibles[start]:
                return 0
            return sum(dp(p, remaining-1) for p in possibles[start]) % MOD

        return sum(dp(i, n) for i in range(10)) % MOD

    def knightDialer(self, n: int) -> int:
        """Feb 04, 2024 11:05"""
        if not n:
            return 0
        MOD = int(1e9+7)
        possibles = [
            [4, 6],  # 0
            [8, 6],  # 1
            [7, 9],  # 2
            [4, 8],  # 3
            [3, 9, 0],  # 4
            [],  # 5
            [1, 7, 0],  # 6
            [2, 6],  # 7
            [1, 3],  # 8
            [2, 4],  # 9
        ]
        dp = [1]*10
        for _ in range(1, n):
            _dp = [0]*10
            for i, c in enumerate(dp):
                for j  in possibles[i]:
                    _dp[j] += c
                    _dp[j] %= MOD
            dp = _dp
        return sum(dp)%MOD


@pytest.mark.parametrize('args', [
    ((1, 10)),
    ((2, 20)),
    ((3131, 136006598)),
])
def test(args):
    assert args[-1] == Solution().knightDialer(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
