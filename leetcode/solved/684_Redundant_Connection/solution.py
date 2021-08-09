#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:

	n == edges.length
	3 <= n <= 1000
	edges[i].length == 2
	1 <= ai < bi <= edges.length
	ai != bi
	There are no repeated edges.
	The given graph is connected.
"""
import sys
from collections import deque
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_edges = [0] * (len(edges) + 1)
        num_nodes_having_n_edges = defaultdict(int)
        num_nodes_having_n_edges[0] = len(edges)
        for u, v in edges:
            num_nodes_having_n_edges[num_edges[u]] -= 1
            num_nodes_having_n_edges[num_edges[v]] -= 1
            num_edges[u] += 1
            num_edges[v] += 1
            num_nodes_having_n_edges[min(3, num_edges[u])] += 1
            num_nodes_having_n_edges[min(3, num_edges[v])] += 1
            if num_nodes_having_n_edges[1] < 2 + num_nodes_having_n_edges[3]:
                return [u, v]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        group_cohort = dict()
        node_group = dict()

        def add_edge(u, v, node_group, group_cohort):
            if u in node_group and v in node_group:
                if group_cohort[node_group[u]] == group_cohort[node_group[v]]:
                    return False
                g1, g2 = sorted([node_group[u], node_group[v]])
                group_cohort[g1].update(group_cohort[g2])
                group_cohort[g2] = group_cohort[g1]
            elif u in node_group and v not in node_group:
                node_group[v] = node_group[u]
                group_cohort[node_group[u]].add(v)
            elif u not in node_group and v in node_group:
                node_group[u] = node_group[v]
                group_cohort[node_group[v]].add(u)
            else:
                g = len(node_group)
                node_group[u] = node_group[v] = g
                group_cohort[g] = {u, v}
            return True

        for u, v in edges:
            if not add_edge(u, v, node_group, group_cohort):
                return [u, v]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """08/28/2020 00:42"""
        def find_root(x):
            if x != parents[x]:
                parents[x] = find_root(parents[x])
            return parents[x]

        parents = [None]*(len(edges)+1)
        for u, v in edges:
            if not parents[u] and not parents[v]:
                parents[u] = parents[v] = min(u, v)
            elif not parents[u] and parents[v]:
                parents[u] = parents[v]
            elif parents[u] and not parents[v]:
                parents[v] = parents[u]
            else:
                up, vp = find_root(u), find_root(v)
                if up == vp:
                    return [u, v]
                else:
                    parents[up] = vp

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {}

        def find_root(v):
            if v in rep and rep[v] is None:
                return v
            root = find_root(rep[v])
            rep[v] = root
            return root

        for u, v in edges:
            if u in rep and v in rep:
                ur = find_root(u)
                vr = find_root(v)
                if ur == vr:
                    return [u, v]
                rep[min(ur, vr)] = max(ur, vr)
            elif u in rep:
                rep[v] = u
            elif v in rep:
                rep[u] = v
            else:
                rep[min(u, v)] = max(u, v)
                rep[max(u, v)] = None
        return None


@pytest.mark.parametrize('edges, expected', [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
])
def test(edges, expected):
    assert expected == Solution().findRedundantConnection(edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
