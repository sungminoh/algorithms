#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:

	2 <= n <= 105
	n - 1 <= connections.length <= 105
	0 <= ai, bi <= n - 1
	ai != bi
	There are no repeated connections.
"""
from pathlib import Path
import json
import sys
from typing import Tuple
from typing import List
import pytest


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """05/14/2021 23:16
        Tarjan's Strongly Connected Components Algorithm
        Time Complexity: O(V+E)
        Space Complexity: O(V+E)
        """
        # build graph
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        rank = [-1]*n
        def dfs(d, u, p):
            """Returns critical edges"""
            rank[u] = d
            critical_edges = []
            for v in graph[u]:
                # Ignore the edge going back to its own parent
                if v == p:
                    continue
                if rank[v] < 0:
                    critical_edges.extend(dfs(d+1, v, u))
                # If child met an ancestor,
                #  the rank of the ancestor is min rank
                rank[u] = min(rank[u], rank[v])
            # When the rank is not smaller than its own rank,
            #  there was no cycle
            if rank[u] >= d and p >= 0:
                critical_edges.append([p, u])
            return critical_edges

        return dfs(0, 0, -1)

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """06/05/2022 18:47"""
        graph = [set() for _ in range(n)]
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)

        ret = []
        visited = set()
        def dfs(a, p, parents) -> Tuple[List[int], List[int]]:
            """
            Return the nodes that can be reached from `a` and the nodes in
            `parents` that can be reached from `a`
            """
            visited.add(a)
            parents.add(a)
            reachable = set()
            met_parents = set()
            for b in graph[a]:
                if b == p:
                    continue
                reachable.add(b)
                if b in parents:
                    met_parents.add(b)
                if b not in visited:
                    sub_reachable, sub_met_parents = dfs(b, a, parents)
                    if not sub_met_parents:
                        ret.append([a, b])
                    reachable.update(sub_reachable)
                    met_parents.update(sub_met_parents)
            parents.remove(a)
            met_parents.discard(a)
            return reachable, met_parents

        dfs(0, None, set())
        return ret


@pytest.mark.parametrize('n, connections, expected', [
    (4, [[0,1],[1,2],[2,0],[1,3]], [[1,3]]),
    (2, [[0,1]], [[0,1]]),
    json.load(open(Path(__file__).parent/'testcase.json')),
])
def test(n, connections, expected):
    actual = Solution().criticalConnections(n, connections)
    assert [sorted(x) for x in expected] == [sorted(x) for x in actual]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
