#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

	N will be in the range [1, 100].
	K will be in the range [1, N].
	The length of times will be in the range [1, 6000].
	All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
import sys
from heapq import heappush
from heapq import heappop
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
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


@pytest.mark.parametrize('times, N, K, expected', [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]], 5, 5, 31),
])
def test(times, N, K, expected):
    assert expected == Solution().networkDelayTime(times, N, K)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
