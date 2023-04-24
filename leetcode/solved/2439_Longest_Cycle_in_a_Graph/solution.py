#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

Example 1:

Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.

Example 2:

Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.

Constraints:

	n == edges.length
	2 <= n <= 105
	-1 <= edges[i] < n
	edges[i] != i
"""
from pathlib import Path
import json
from typing import List
import pytest
import sys


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """Apr 23, 2023 23:08
        TLE
        Maximum recusion error"""
        def dfs(a, d, dist):
            if a in dist:
                return d-dist[a]
            dist[a] = d
            if edges[a] >= 0:
                d = dfs(edges[a], d+1, dist)
                if d >= 0:
                    return d
            return -1

        return max(dfs(i, 0, {}) for i in set(edges) if i >= 0)

    def longestCycle(self, edges: List[int]) -> int:
        """Apr 23, 2023 23:26"""
        ret = -1
        for i in range(len(edges)):
            d = 0
            dist = {i: d}
            j = edges[i]
            while j >= i and j not in dist:
                d += 1
                dist[j] = d
                j = edges[j]
            if j >= i:
                ret = max(ret, d-dist[j]+1)
        return ret

    def longestCycle(self, edges: List[int]) -> int:
        """Apr 23, 2023 23:33"""
        ret = -1
        d = 0
        dist = {}
        for i in range(len(edges)):
            if i in dist:
                continue
            s = d
            j = i
            while j >= 0 and j not in dist:
                dist[j] = d
                j = edges[j]
                d += 1
            if j >= 0 and dist[j] >= s:
                ret = max(ret, d-dist[j])
        return ret


@pytest.mark.parametrize('args', [
    (([3,3,4,2,3], 3)),
    (([2,-1,3,1], -1)),
    (([3,4,0,2,-1,2], 3)),
    (([4,3,3,4,7,2,3,3], 3)),
    (([-1,4,-1,2,0,4], -1)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 43242)),
])
def test(args):
    assert args[-1] == Solution().longestCycle(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
