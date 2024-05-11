#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

Two sequences are considered different if at least one element differs from each other.

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30

Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181

Constraints:

	1 <= n <= 5000
	rollMax.length == 6
	1 <= rollMax[i] <= 15
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """May 07, 2024 16:09"""
        MOD = int(1e9+7)
        dp = {(1, 0): 1}
        for _ in range(n):
            _dp = defaultdict(int)
            for (num, cnt), acc in dp.items():
                for i in range(1, 7):
                    if i != num:
                        _dp[i, 1] += acc
                    elif cnt < rollMax[num-1]:
                        _dp[i, cnt+1] += acc
            dp = {k: v % MOD for k, v in _dp.items()}
        return sum(dp.values()) % MOD

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """May 07, 2024 19:37"""
        MOD = int(1e9+7)
        dp = [[0]*7 for _ in range(n+1)]
        dp[0][-1] = 1
        for i in range(1, n+1):
            acc = 0
            for j in range(6):
                dp[i][j] = dp[i-1][-1]
                if i > rollMax[j]:
                    dp[i][j] -= dp[i - rollMax[j] - 1][-1] - dp[i - rollMax[j] - 1][j]
                dp[i][j] %= MOD
                acc += dp[i][j]
                acc %= MOD
            dp[i][-1] = acc
        return dp[n][-1] % MOD


@pytest.mark.parametrize('args', [
    ((2, [1,1,2,2,2,3], 34)),
    ((2, [1,1,1,1,1,1], 30)),
    ((3, [1,1,1,2,2,3], 181)),
    ((4, [2,1,1,3,3,2], 1082)),
])
def test(args):
    assert args[-1] == Solution().dieSimulator(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
