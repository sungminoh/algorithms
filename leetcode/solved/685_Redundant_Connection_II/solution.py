#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]

Constraints:

	n == edges.length
	3 <= n <= 1000
	edges[i].length == 2
	1 <= ui, vi <= n
	ui != vi
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        rgraph = defaultdict(set)
        graph = defaultdict(set)
        edge_index = {}
        n = 0
        for i, (a, b) in enumerate(edges):
            edge_index[(a, b)] = i
            graph[a].add(b)
            rgraph[b].add(a)
            n = max(n, a, b)

        def find_cycle(u, backtrack, visited):
            if u in visited:
                for i in range(len(backtrack)):
                    if backtrack[i] == u:
                        return backtrack[i:] + [backtrack[i]]
            visited.add(u)
            backtrack.append(u)
            for v in graph[u]:
                sub = find_cycle(v, backtrack, visited)
                if sub is not None:
                    return sub
            visited.remove(u)
            backtrack.pop()

        # when there is a root
        if len(set([len(x) for x in rgraph.values()])) > 1:
            for i in range(1, n+1):
                if i not in rgraph:  # root
                    ret = find_cycle(i, [], set())
                    if ret is not None:
                        # if there is a cycle return the last edge that made cycle
                        return ret[-2:]
            # otherwise, return the later edge that makes two parents
            v = max(rgraph.keys(), key=lambda x: len(rgraph[x]))
            return max([[u, v] for u in rgraph[v]], key=lambda x: edge_index[tuple(x)])

        # when there is not a fixed root, return the latest edge in the cycle
        cycle = find_cycle(max(graph.keys(), key=lambda x: len(graph[x])), [], set())
        return max(
            [[u, v] for u, v in zip(cycle[:-1], cycle[1:])],
            key=lambda x: edge_index[tuple(x)])


@pytest.mark.parametrize('edges, expected', [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[4,1],[1,5]], [4,1]),
    ([[2,1],[3,1],[4,2],[1,4]], [2,1])
])
def test(edges, expected):
    assert expected == Solution().findRedundantDirectedConnection(edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
