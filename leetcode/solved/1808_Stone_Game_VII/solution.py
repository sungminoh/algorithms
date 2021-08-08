#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.

Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122

Constraints:

	n == stones.length
	2 <= n <= 1000
	1 <= stones[i] <= 1000
"""
import itertools
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        acc = [0] + list(itertools.accumulate(stones))

        def sum_between(i, j):
            return acc[j+1] - acc[i]

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0
            return max(
                sum_between(i+1, j) - dfs(i+1, j),
                sum_between(i, j-1) - dfs(i, j-1))

        return dfs(0, len(stones)-1)

    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        acc = [0] + list(itertools.accumulate(stones))

        memo = {}
        for i in range(len(stones)):
            memo[i, i] = 0

        for d in range(1, len(stones)):
            for i in range(len(stones)):
                j = i+d
                if j >= len(stones):
                    break
                memo[i, j] = max(
                    acc[j+1]-acc[i+1] - memo[i+1, j],
                    acc[j]-acc[i] - memo[i, j-1])

        return memo[0, len(stones)-1]

    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        acc = [0] + list(itertools.accumulate(stones))
        dp = [0]*len(stones)
        for d in range(1, len(stones)):
            new_dp = [0]*(len(stones)-d)
            for i in range(len(stones)):
                j = i+d
                if j >= len(stones):
                    break
                new_dp[i] = max(
                    acc[j+1]-acc[i+1] - dp[i+1],
                    acc[j]-acc[i] - dp[i])
            dp = new_dp
        return dp[-1]


@pytest.mark.parametrize('stones, expected', [
    ([5,3,1,4,2], 6),
    ([7,90,5,1,100,10,10,2], 122),
    ([1,100,1], 1)
])
def test(stones, expected):
    assert expected == Solution().stoneGameVII(stones)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
