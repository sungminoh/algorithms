#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges.  Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.  The answer edge [u, v] should be in the same format, with u < v.
Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Example 2:

Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3

Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
"""
from collections import defaultdict
import sys
from typing import List
import pytest


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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

    def _findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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

    def _findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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


@pytest.mark.parametrize('edges, expected', [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
    ([[1,2],[2,3],[2,4],[4,5],[1,5]], [1,5]),
    ([[2,4],[3,4],[1,4],[2,5],[4,5]], [4,5]),
    ([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]], [4,10]),
    ([[21,22],[4,7],[12,13],[13,25],[12,15],[17,23],[15,16],[8,21],[23,24],
      [3,9],[19,21],[13,21],[4,10],[5,6],[1,20],[10,16],[1,4],[10,14],[5,20],
      [1,2],[3,24],[2,11],[11,24],[24,25],[17,18]], [24,25])
])
def test(edges, expected):
    assert expected == Solution().findRedundantConnection(edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
