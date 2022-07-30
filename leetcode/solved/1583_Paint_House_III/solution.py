#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

	For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].

Given an array houses, an m x n matrix cost and an integer target where:

	houses[i]: is the color of the house i, and 0 if the house is not painted yet.
	cost[i][j]: is the cost of paint the house i with the color j + 1.

Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
Cost of paint the first and last house (10 + 1) = 11.

Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.

Constraints:

	m == houses.length == cost.length
	n == cost[i].length
	1 <= m <= 100
	1 <= n <= 20
	1 <= target <= m
	0 <= houses[i] <= n
	1 <= cost[i][j] <= 104
"""
from functools import lru_cache
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        Brute-force DFS, TLE
        Time Complexity: O(n^m)
        """
        def dfs(i, cnt):
            if cnt < 0:
                return -1
            if i == len(houses):
                return 0 if cnt == 0 else -1
            if houses[i] != 0:
                return dfs(i+1, (cnt-1) if i == 0 or houses[i-1] != houses[i] else cnt)
            ret = float('inf')
            for clr, cst in enumerate(cost[i], 1):
                houses[i] = clr
                sub = dfs(i+1, (cnt-1) if i == 0 or houses[i-1] != houses[i] else cnt)
                if sub != -1:
                    ret = min(ret, cst+sub)
                houses[i] = 0
            return ret if ret != float('inf') else -1

        return dfs(0, target)

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """07/29/2022 23:35
        Top-Down Recursive DP
        Time Complexity: O(m*target*n)
        Space Complexity: O(m*target*n)
        """
        @lru_cache(None)
        def dfs(i, cnt, prev_clr):
            if cnt < 0:
                return -1
            if i == len(houses):
                return 0 if cnt == 0 else -1
            if houses[i] != 0:
                return dfs(i+1, (cnt-1) if prev_clr != houses[i] else cnt, houses[i])
            ret = float('inf')
            for clr, cst in enumerate(cost[i], 1):
                sub = dfs(i+1, (cnt-1) if prev_clr != clr else cnt, clr)
                if sub != -1:
                    ret = min(ret, cst+sub)
            return ret if ret != float('inf') else -1

        return dfs(0, target, -1)

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """07/29/2022 23:24
        Bottom-Up DP
        Time Complexity: O(m*target*n)
        Space Complexity: O(target*n)
        """
        dp = {}
        if houses[0] == 0:
            for clr, cst in enumerate(cost[0], 1):
                dp[(clr, 1)] = cst
        else:
            dp[(houses[0], 1)] = 0
        for i in range(1, m):
            _dp = {}
            if houses[i] == 0:
                for (cl, ct), cs in dp.items():
                    for clr, cst in enumerate(cost[i], 1):
                        cnt = ct if clr == cl else (ct+1)
                        if cnt <= target:
                            key = (clr, cnt)
                            val = cs+cst
                            _dp.setdefault(key, val)
                            _dp[key] = min(_dp[key], val)
            else:
                for (cl, ct), cs in dp.items():
                    cnt = ct if houses[i] == cl else (ct+1)
                    if cnt <= target:
                        key = (houses[i], cnt)
                        _dp.setdefault(key, cs)
                        _dp[key] = min(_dp[key], cs)
            dp = _dp

        if houses[m-1] != 0:
            return dp.get((houses[m-1], target), -1)
        else:
            ret = min(dp.get((c, target), float('inf')) for c in range(1, n+1))
            return ret if ret != float('inf') else -1


@pytest.mark.parametrize('houses, cost, m, n, target, expected', [
    ([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3, 9),
    ([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3, 11),
    ([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3, -1),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 1000000),
])
def test(houses, cost, m, n, target, expected):
    assert expected == Solution().minCost(houses, cost, m, n, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
