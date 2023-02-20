#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Constraints:

	1 <= n <= 2 * 105
	0 <= edges.length <= 2 * 105
	edges[i].length == 2
	0 <= ui, vi <= n - 1
	ui != vi
	0 <= source, destination <= n - 1
	There are no duplicate edges.
	There are no self edges.
"""
from typing import List
import pytest
import sys


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """Feb 19, 2023 17:01"""
        class UnionFind:
            def __init__(self):
                self.rep = {}

            def find(self, v):
                if v not in self.rep:
                    self.rep[v] = v
                if v == self.rep[v]:
                    return self.rep[v]
                ret = self.find(self.rep[v])
                self.rep[v] = ret
                return ret

            def union(self, i, j):
                if j < i:
                    return self.union(j, i)
                ip = self.find(i)
                jp = self.find(j)
                self.rep[jp] = ip

        uf = UnionFind()
        for i, j in edges:
            uf.union(i, j)

        return uf.find(source) == uf.find(destination)


@pytest.mark.parametrize('n, edges, source, destination, expected', [
    (3, [[0,1],[1,2],[2,0]], 0, 2, True),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
])
def test(n, edges, source, destination, expected):
    assert expected == Solution().validPath(n, edges, source, destination)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
