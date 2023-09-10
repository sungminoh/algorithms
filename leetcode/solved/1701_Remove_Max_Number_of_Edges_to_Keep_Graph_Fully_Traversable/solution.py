#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice and Bob have an undirected graph of n nodes and three types of edges:

	Type 1: Can be traversed by Alice only.
	Type 2: Can be traversed by Bob only.
	Type 3: Can be traversed by both Alice and Bob.

Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

Example 1:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

Constraints:

	1 <= n <= 105
	1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
	edges[i].length == 3
	1 <= typei <= 3
	1 <= ui < vi <= n
	All tuples (typei, ui, vi) are distinct.
"""
from collections import Counter
from collections import defaultdict
from enum import Enum
from typing import List
import pytest
import sys


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """Wrong"""
        unused = 0
        num_edges_per_type = defaultdict(int)
        g = defaultdict(dict)

        for t, u, v in sorted(edges, reverse=True):  # iterate both type first
            if u == v:
                unused += 1
            elif v in g[u]:
                if g[u][v] == 3 or g[u][v] == t:
                    unused += 1
                else:
                    if t == 3:
                        pt = g[u][v]
                        num_edges_per_type[pt] -= 2 if pt == 2.5 else 1
                        g[u][v] = g[v][u] = 3
                    else:
                        g[u][v] = g[v][u] = 2.5  # artificial edge type to represent having both type 1, 2 edges
                    num_edges_per_type[t] += 1
            else:
                num_edges_per_type[t] += 1
                g[u][v] = g[v][u] = t

        if num_edges_per_type[1] + num_edges_per_type[3] < n-1 \
                or num_edges_per_type[2] + num_edges_per_type[3] < n-1:
            return -1

        def dfs(u, edgetype, visited=None):
            if visited is None:
                visited = set()
            visited.add(u)
            for v, t in sorted(g[u].items(), key=lambda x: -x[1]):  # prioritize both type first
                if v not in visited and (t > 2 or t == edgetype):
                    yield t if t == 3 else edgetype
                    yield from dfs(v, edgetype, visited)

        edges1 = list(dfs(1, 1))
        edges2 = list(dfs(1, 2))
        if len(edges1) < n-1 or len(edges) < n-1:
            return -1

        edgecnt1 = Counter(edges1)
        edgecnt2 = Counter(edges2)

        return unused \
            + num_edges_per_type[3] - max(edgecnt1[3], edgecnt2[3]) \
            + num_edges_per_type[1] - edgecnt1[1] \
            + num_edges_per_type[2] - edgecnt2[2]

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """Sep 09, 2023 21:14"""
        class UnionFind:
            def __init__(self, n):
                self.parents = list(range(n))

            def find(self, i):
                if self.parents[i] != i:
                    self.parents[i] = self.find(self.parents[i])
                return self.parents[i]

            def union(self, i, j):
                pi, pj = self.find(i), self.find(j)
                if pi == pj:
                    return False
                self.parents[pi] = self.parents[pj] = min(pi, pi)
                return True

        uf1 = UnionFind(n+1)
        uf2 = UnionFind(n+1)

        ret = 0
        for t, u, v in sorted(edges, reverse=True):  # iterate both type first
            if t == 1:
                if not uf1.union(u, v):
                    ret += 1
            elif t == 2:
                if not uf2.union(u, v):
                    ret += 1
            elif t == 3:
                merge1 = uf1.union(u, v)
                merge2 = uf2.union(u, v)
                if not merge1 and not merge2:
                    ret += 1

        return ret if len(set(uf1.find(i) for i in range(1, n+1))) == 1 \
            and len(set(uf2.find(i) for i in range(1, n+1))) == 1 \
            else -1


@pytest.mark.parametrize('args', [
    ((4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2)),
    ((4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0)),
    ((4, [[3,2,3],[1,1,2],[2,3,4]], -1)),
    ((12, [[3,1,2],[2,2,3],[3,1,4],[2,3,5],[1,2,6],[2,4,7],[3,3,8],[3,2,9],[2,1,10],[2,1,11],[1,11,12],[1,10,11],[2,5,9],[2,7,10],[2,4,12],[3,9,10],[1,6,9],[2,10,12],[1,2,5],[3,5,6],[1,7,11],[1,8,9],[1,1,11],[3,4,5],[1,5,9],[2,4,9],[1,8,11],[3,6,8],[1,8,10],[2,2,4],[2,3,8],[3,2,6],[3,10,11],[2,3,11],[3,5,9],[3,3,5],[2,6,11],[3,2,7],[1,5,11],[1,1,5],[2,9,10],[1,6,7],[3,2,3],[2,8,9],[3,2,8]], 33)),
])
def test(args):
    assert args[-1] == Solution().maxNumEdgesToRemove(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
