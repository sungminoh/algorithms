#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:

	n == graph.length
	1 <= n <= 12
	0 <= graph[i].length < n
	graph[i] does not contain i.
	If graph[a] contains b, then graph[b] contains a.
	The input graph is always connected.
"""
from functools import lru_cache
import math
from heapq import heappop
from heapq import heappush
import sys
from typing import List
import pytest


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        1. Convert the graph to a bidirectional weighted graph
            whose all pairs are connected
        2. Return the minium traverse distance

        Time complexity: O(n^3) (max of FW and n times of DFS)
            Floyd-Warshall: O(n^3)
            DFS: O(V+E) = O(n + n^2)
        Space complexity: O(n*2^n)
        """
        n = len(graph)
        # Floyd-Warshall
        g = [[float('inf')]*n for _ in range(n)]
        for i, js in enumerate(graph):
            for j in js:
                g[i][j] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        g[i][j] = 0
                    else:
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        # dfs
        @lru_cache(None)
        def dfs(i, remain):
            if remain == 0:
                return 0
            ret = float('inf')
            for j, d in enumerate(g[i]):
                if remain&(1<<j) != 0:
                    ret = min(ret, d + dfs(j, remain ^ (1<<j)))
            return ret

        full_mask = (1<<n)-1
        return min(dfs(i, full_mask^(1<<i)) for i in range(n))

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        BFS
        Visit once per each status when the status is the current node and
        visited nodes
        """
        n = len(graph)
        steps = 0
        all_visited = (1<<n)-1
        queue = [(i, 1<<i) for i in range(n)]
        visited_status = set(queue)
        while queue:
            new_queue = []
            for i, visited in queue:
                if visited == all_visited:
                    return steps
                for j in graph[i]:
                    status = (j, visited | (1<<j))
                    if status not in visited_status:
                        visited_status.add(status)
                        new_queue.append(status)
            steps += 1
            queue = new_queue

        return -1


@pytest.mark.parametrize('graph, expected', [
    ([[1,2,3],[0],[0],[0]], 4),
    ([[1],[0,2,4],[1,3,4],[2],[1,2]], 4),
    ([[6,8],[2,9],[1,3,5],[2,6],[5],[2,6,4],[5,3,0,7],[6],[0],[1]], 12),
])
def test(graph, expected):
    print()
    assert expected == Solution().shortestPathLength(graph)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
