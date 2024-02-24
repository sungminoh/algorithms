from pathlib import Path
import json
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

	For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:

	1 <= routes.length <= 500.
	1 <= routes[i].length <= 105
	All the values of routes[i] are unique.
	sum(routes[i].length) <= 105
	0 <= routes[i][j] < 106
	0 <= source, target < 106
"""
import pytest
import sys


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """Feb 24, 2024 11:52 MLE"""
        g = {}
        for route in routes:
            for i in range(len(route)):
                for j in range(i):
                    g.setdefault(route[i], set()).add(route[j])
                    g.setdefault(route[j], set()).add(route[i])

        cnt = 0
        visited = set()
        q = set([source])
        while q:
            _q = set()
            for stop in q:
                if stop == target:
                    return cnt
                if stop not in visited:
                    visited.add(stop)
                    _q.update(g[stop])
            cnt += 1
            q =  _q - visited
        return -1

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """Feb 24, 2024 12:52"""
        if source == target:
            return 0

        routes = [set(route) for route in routes]
        g = [set() for _ in routes]
        q = set()
        t = set()
        for i in range(len(routes)):
            if source in routes[i]:
                q.add(i)
            if target in routes[i]:
                t.add(i)
            for j in range(i):
                if routes[i] & routes[j]:
                    g[i].add(j)
                    g[j].add(i)

        visited = set()
        cnt = 1
        while q:
            _q = set()
            for cur in q:
                if cur in t:
                    return cnt
                for nxt in g[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        _q.add(nxt)
            q = _q
            cnt += 1
        return -1


@pytest.mark.parametrize('args', [
    (([[1,2,7],[3,6,7]], 1, 6, 2)),
    (([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12, -1)),
    (([[1,7],[3,5]], 5, 5, 0)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 0, 100000, -1)),
])
def test(args):
    assert args[-1] == Solution().numBusesToDestination(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
