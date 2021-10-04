#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.

Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23

Example 3:

Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.

Constraints:

	0 <= edges.length <= min(n * (n - 1) / 2, 104)
	edges[i].length == 3
	0 <= ui < vi < n
	There are no multiple edges in the graph.
	0 <= cnti <= 104
	0 <= maxMoves <= 109
	1 <= n <= 3000
"""
from heapq import heappush
from heapq import heappop
from pathlib import Path
import json
import sys
from collections import deque
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(set)
        for u, v, d in edges:
            graph[u].add((v, d))
            graph[v].add((u, d))

        passed = defaultdict(int)
        marked = set()
        visited = set()
        def dfs(i, n):
            ret = 1 if i not in marked else 0
            marked.add(i)
            visited.add(i)
            for j, d in graph[i]:
                if j in visited or d >= n:
                    assert passed[i,j]+passed[j,i] <= d
                    from_i = min(n, d - passed[j, i])
                    ret += max(0, from_i - passed[i, j])
                    passed[i, j] = max(passed[i, j], from_i)
                else:
                    ret += d - passed[i, j] - passed[j, i]
                    passed[i, j] = d - passed[j, i]
                    ret += dfs(j, n-d-1)
            visited.remove(i)
            return ret

        return dfs(0, maxMoves)

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """
        Dijkstra
        """
        graph = defaultdict(set)
        for u, v, d in edges:
            graph[u].add((v, d))
            graph[v].add((u, d))

        ret = 0

        passed = defaultdict(int)
        visited = set()
        h = [(-maxMoves, 0)]
        while h:
            r, i = heappop(h)
            r = -r
            if i in visited:
                continue
            ret += 1
            visited.add(i)
            for j, d in graph[i]:
                from_i = min(r, d-passed[j, i])
                new_from_i = max(0, from_i - passed[i, j])
                passed[i, j] = max(passed[i, j], from_i)
                ret += new_from_i
                if d < r:
                    heappush(h, (-(r-d-1), j))

        return ret


@pytest.mark.parametrize('edges, maxMoves, n, expected', [
    ([[0,1,10],[0,2,1],[1,2,2]], 6, 3, 13),
    ([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4, 23),
    ([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5, 1),
    ([[0,1,1],[1,2,1],[2,0,1]], 20, 3, 6),
    ([[2,4,2],[3,4,5],[2,3,1],[0,2,1],[0,3,5]], 14, 5, 18),
    ([[0,3,8],[0,1,4],[2,4,3],[1,2,0],[1,3,9],[0,4,7],[3,4,9],[1,4,4],[0,2,7],[2,3,1]], 8, 5, 40),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 4343908),
])
def test(edges, maxMoves, n, expected):
    assert expected == Solution().reachableNodes(edges, maxMoves, n)


if __name__ == '__main__':
    sys.exit(pytest.main(['-v', '-s'] + sys.argv))
