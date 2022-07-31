#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:

	2 <= cost.length <= 1000
	0 <= cost[i] <= 999
"""
import sys
from typing import List
import pytest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """06/20/2021 07:05
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)
        prv = cost[0]
        cur = cost[1]
        for i, c in enumerate(cost[2:], 2):
            prv, cur = cur, min(cur, prv) + c
        return min(prv, cur)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """07/29/2022 23:43
        Time complexity: O(n)
        Space complexity: O(1)
        """
        n = len(cost)
        if n == 0:
            return 0
        dp = [0, 0]
        for i in range(2, n+1):
            dp[i%2] = min(dp[(i-1)%2] + cost[i-1], dp[(i-2)%2] + cost[i-2])
        return dp[n%2]


@pytest.mark.parametrize('cost, expected', [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6),
])
def test(cost, expected):
    assert expected == Solution().minCostClimbingStairs(cost)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
