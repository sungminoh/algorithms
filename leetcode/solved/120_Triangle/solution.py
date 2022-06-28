#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

	1 <= triangle.length <= 200
	triangle[0].length == 1
	triangle[i].length == triangle[i - 1].length + 1
	-104 <= triangle[i][j] <= 104

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
from functools import lru_cache
import sys
from typing import List
import pytest


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bruteforce dfs
        Time complexity: O(n!)
        Space complexity: O(n)  # callstack
        """
        mn = float('inf')
        def dfs(d, i, cur):
            nonlocal mn
            if d == len(triangle):
                mn = min(mn, cur)
                return
            cur += triangle[d][i]
            dfs(d+1, i, cur)
            dfs(d+1, i+1, cur)

        dfs(0, 0, 0)
        return mn

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Recursive DP
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        @lru_cache(None)
        def dp(d, i):
            if d == 0:
                assert i == 0
                return triangle[d][i]
            m = float('inf')
            if i > 0:
                m = min(m, dp(d-1, i-1))
            if i < len(triangle[d])-1:
                m = min(m, dp(d-1, i))
            return m + triangle[d][i]

        return min([dp(len(triangle)-1, i) for i in range(len(triangle[-1]))])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom-up DP
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not triangle:
            return 0
        cost = triangle[0]
        for row in triangle[1:]:
            new_cost = []
            for i, v in enumerate(row):
                m = float('inf')
                if i < len(row)-1:
                    m = min(m, cost[i])
                if i > 0:
                    m = min(m, cost[i-1])
                new_cost.append(m+v)
            cost = new_cost
        return min(cost)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """05/05/2021 08:55
        Top-down DP
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        if not triangle:
            return 0
        cost = triangle[-1]
        for row in reversed(triangle[:-1]):
            for j, v in enumerate(row):
                cost[j] = v + min(cost[j], cost[j+1])
        return cost[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """06/19/2022 15:56"""
        if not triangle:
            return 0
        cur = triangle[0]
        for row in triangle[1:]:
            cur = [
                x + min([cur[j] for j in range(max(0, i-1), min(len(cur), i+1))])
                for i, x in enumerate(row)
            ]
        return min(cur)


@pytest.mark.parametrize('triangle, expected', [
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-10]], -10),
])
def test(triangle, expected):
    assert expected == Solution().minimumTotal(triangle)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
