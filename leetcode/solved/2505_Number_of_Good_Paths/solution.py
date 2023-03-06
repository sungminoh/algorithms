#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

	The starting node and the ending node have the same value.
	All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:

Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

Example 2:

Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.

Example 3:

Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.

Constraints:

	n == vals.length
	1 <= n <= 3 * 104
	0 <= vals[i] <= 105
	edges.length == n - 1
	edges[i].length == 2
	0 <= ai, bi < n
	ai != bi
	edges represents a valid tree.
"""
from collections import defaultdict
import bisect
import heapq
from pathlib import Path
import json
from typing import Tuple
from typing import List
import pytest
import sys


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """Mar 05, 2023 17:53
        TLE
        """
        n = len(vals)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ret = n
        def dfs(a, p):
            nonlocal ret
            leaves = {vals[a]: 1}
            for b in g[a]:
                if b == p:
                    continue
                for v, cnt in dfs(b, a).items():
                    if v < vals[a]:
                        continue
                    else:
                        leaves.setdefault(v, 0)
                        ret += leaves[v] * cnt
                        leaves[v] += cnt
            return leaves
        dfs(0, None)
        return ret

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """Mar 05, 2023 19:29"""
        n = len(vals)
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        parent = [None]*n
        def find(x):
            if parent[x] is None:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)
            parent[a] = parent[b] = min(pa, pb)

        ret = 0
        nodes = sorted(list(range(n)), key=lambda x: vals[x])
        i = 0
        while i < n:
            ps = defaultdict(int)
            j = i
            while j < n and vals[nodes[j]] == vals[nodes[i]]:
                a = nodes[j]
                for b in g[a]:
                    if b != a and vals[b] <= vals[a]:
                        union(a, b)
                ps[find(a)] += 1
                j += 1
            i = j
            for c in ps.values():
                ret += (c * (c+1))//2
        return ret


@pytest.mark.parametrize('args', [
    (([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]], 6)),
    (([1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]], 7)),
    (([1], [], 1)),
    ((*json.load(open(Path(__file__).parent/'testcase.json')), 123898)),
])
def test(args):
    assert args[-1] == Solution().numberOfGoodPaths(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
