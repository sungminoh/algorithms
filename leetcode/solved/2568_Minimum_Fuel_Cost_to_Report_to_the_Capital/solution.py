#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.

Example 1:

Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation:
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum.
It can be proven that 3 is the minimum number of liters of fuel needed.

Example 2:

Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation:
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum.
It can be proven that 7 is the minimum number of liters of fuel needed.

Example 3:

Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.

Constraints:

	1 <= n <= 105
	roads.length == n - 1
	roads[i].length == 2
	0 <= ai, bi < n
	ai != bi
	roads represents a valid tree.
	1 <= seats <= 105
"""
from typing import List
import pytest
import sys


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """Mar 20, 2023 23:06"""
        graph = {}
        for a, b in roads:
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)

        def dfs(a, parent=None):
            if a not in graph:
                return 0, 0, 0
            cars_total = 0
            remainders_total = 1
            cost_total = 0
            for b in graph[a]:
                if b == parent:
                    continue
                cars, remainders, cost = dfs(b, a)
                cars_total += cars
                remainders_total += remainders
                cost_total += cost + cars + min(remainders, 1)
            c, r = divmod(remainders_total, seats)
            cars_total += c
            return cars_total, r, cost_total

        return dfs(0)[2]


@pytest.mark.parametrize('args', [
    (([[0,1],[0,2],[0,3]], 5, 3)),
    (([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2, 7)),
    (([], 1, 0)),
])
def test(args):
    assert args[-1] == Solution().minimumFuelCost(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
