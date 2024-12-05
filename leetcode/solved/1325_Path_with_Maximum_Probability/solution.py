#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:

	2 <= n <= 10^4
	0 <= start, end < n
	start != end
	0 <= a, b < n
	a != b
	0 <= succProb.length == edges.length <= 2*10^4
	0 <= succProb[i] <= 1
	There is at most one edge between every two nodes.
"""
from collections import defaultdict, deque
from typing import List
from heapq import heappop, heappush
import pytest
import sys


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """Dec 09, 2024 08:35"""
        g = [defaultdict(int) for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            g[a][b] = g[b][a] = p

        def dijkstra(s, e):
            dists = [0 for _ in range(n)]
            queue = [(-1, s)]
            while queue:
                np, a = heappop(queue)
                p = -np
                if a == end_node:
                    return p
                if p > dists[a]:
                    dists[a] = p
                    for b, q in g[a].items():
                        heappush(queue, (-p*q, b))
            return dists[e]

        return dijkstra(start_node, end_node)


@pytest.mark.parametrize('args', [
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2, 0.25000)),
    ((3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2, 0.30000)),
    ((3, [[0,1]], [0.5], 0, 2, 0.00000)),
    ((5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4, 0.21390)),
])
def test(args):
    assert args[-1] == Solution().maxProbability(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
