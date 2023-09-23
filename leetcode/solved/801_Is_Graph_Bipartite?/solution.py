#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

	There are no self-edges (graph[u] does not contain u).
	There are no parallel edges (graph[u] does not contain duplicate values).
	If v is in graph[u], then u is in graph[v] (the graph is undirected).
	The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:

	graph.length == n
	1 <= n <= 100
	0 <= graph[u].length < n
	0 <= graph[u][i] <= n - 1
	graph[u] does not contain u.
	All the values of graph[u] are unique.
	If graph[u] contains v, then graph[v] contains u.
"""
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """09/11/2020 23:15"""
        groups = [set(), set()]
        g = defaultdict(set)

        for i, nodes in enumerate(graph):
            for j in nodes:
                g[i].add(j)
                g[j].add(i)

        def dfs(u, i):
            result = True
            for v in g[u]:
                if v in groups[i]:
                    return False
                elif v not in groups[(i+1)%2]:
                    groups[(i+1)%2].add(v)
                    result &= dfs(v, (i+1)%2)
            return result

        for u in g.keys():
            if u not in groups[0] and u not in groups[1]:
                groups[0].add(u)
                if not dfs(u, 0):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """09/11/2020 23:17"""
        groups = [set(), set()]

        def dfs(u, i):
            result = True
            for v in graph[u]:
                if v in groups[i]:
                    return False
                elif v not in groups[(i+1)%2]:
                    groups[(i+1)%2].add(v)
                    result &= dfs(v, (i+1)%2)
            return result

        for u in range(len(graph)):
            if u not in groups[0] and u not in groups[1]:
                groups[0].add(u)
                if not dfs(u, 0):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """05/14/2022 18:22"""
        side = {}
        def dfs(a, flag):
            if a in side:
                return side[a] == flag
            side[a] = flag
            return all(dfs(b, -flag) for b in graph[a])

        ret = True
        for i in range(len(graph)):
            if i not in side:
                ret &= dfs(i, 1)
        return ret

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """Sep 22, 2023 17:41"""
        groups = {}

        def traverse(u, group=1):
            if u in groups:
                return groups[u] == group
            groups[u] = group
            return all(traverse(v, -group) for v in graph[u])

        for i in range(len(graph)):
            if i not in groups:
                if not traverse(i):
                    return False

        return True


@pytest.mark.parametrize('args', [
    (([[1,2,3],[0,2],[0,1,3],[0,2]], False)),
    (([[1,3],[0,2],[1,3],[0,2]], True)),
    (([[2,3,5,6,7,8,9],[2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[1,2,3,6,9],[0,1,2,3,7,8,9],[0,1,2,3,4,7,8,9],[0,1,2,3,5,6,8,9],[0,1,2,3,5,6,7],[0,1,2,3,4,5,6,7]], False)),
])
def test(args):
    assert args[-1] == Solution().isBipartite(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
