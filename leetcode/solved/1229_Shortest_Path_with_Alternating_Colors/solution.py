#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

	redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
	blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Constraints:

	1 <= n <= 100
	0 <= redEdges.length, blueEdges.length <= 400
	redEdges[i].length == blueEdges[j].length == 2
	0 <= ai, bi, uj, vj < n
"""
from typing import List
import pytest
import sys


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """Mar 19, 2023 13:38"""
        red_graph = [[] for _ in range(n)]
        blue_graph = [[] for _ in range(n)]
        for a, b in redEdges:
            red_graph[a].append(b)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        redblue = (red_graph, blue_graph)

        ret = [-1]*n
        dist = 0
        queue = [(0, 0), (0, 1)]
        visited = set(queue)
        while queue:
            _queue = []
            for a, color in queue:
                if ret[a] == -1:
                    ret[a] = dist
                for b in redblue[color][a]:
                    next_color = (color+1)%2
                    if (b, next_color) not in visited:
                        visited.add((b, next_color))
                        _queue.append((b, next_color))
            queue = _queue
            dist += 1
        return ret


@pytest.mark.parametrize('args', [
    ((3, [[0,1],[1,2]], [], [0,1,-1])),
    ((3, [[0,1]], [[2,1]], [0,1,-1])),
])
def test(args):
    assert args[-1] == Solution().shortestAlternatingPaths(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
