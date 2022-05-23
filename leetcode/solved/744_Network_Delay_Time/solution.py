#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:

	1 <= k <= n <= 100
	1 <= times.length <= 6000
	times[i].length == 3
	1 <= ui, vi <= n
	ui != vi
	0 <= wi <= 100
	All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
from pathlib import Path
import json
from collections import defaultdict
import sys
from heapq import heappush
from heapq import heappop
from typing import List
import pytest


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """09/05/2020 13:38"""
        cost = [-1] * (N+1)
        cost[0] = 0
        g = defaultdict(dict)
        for u, v, w in times:
            g[u][v] = w
        if K not in g:
            return -1
        h = [(0, K)]
        while h:
            w, v = heappop(h)
            if cost[v] != -1:
                continue
            cost[v] = w
            for _v in g[v]:
                if cost[_v] > 0:
                    continue
                heappush(h, (w + g[v][_v], _v))
        if all(x >= 0 for x in cost[1:]):
            return max(cost)
        return -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """05/22/2022 20:59
        Dijkstra
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        graph = [{} for _ in range(n)]
        for u, v, t in times:
            graph[u-1][v-1] = t

        dists = [float('inf')] * n
        rest = set(range(n))
        dists[k-1] = 0
        while rest:
            # get the closest next node
            u = min(rest, key=lambda x: dists[x])
            # when there is no reachable node
            if dists[u] == float('inf'):
                return -1
            rest.remove(u)
            for v, t in graph[u].items():
                dists[v] = min(dists[v], dists[u] + t)
        return max(dists)

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """05/22/2022 21:11
        Dijkstra using heap
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        graph = [{} for _ in range(n)]
        for u, v, t in times:
            graph[u-1][v-1] = t

        dists = [-1] * n
        heap = [(0, k-1)]
        while heap:
            d, u = heappop(heap)
            if dists[u] == -1:
                continue
            dists[u] = d
            for v, t in graph[u].items():
                if dists[v] == -1:
                    heappush(heap, (d+t, v))
        return -1 if -1 in dists else max(dists)


@pytest.mark.parametrize('times, n, k, expected', [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1),
    ([[1,2,1]], 2, 2, -1),
    ([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5, 31),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 12),
])
def test(times, n, k, expected):
    assert expected == Solution().networkDelayTime(times, n, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
