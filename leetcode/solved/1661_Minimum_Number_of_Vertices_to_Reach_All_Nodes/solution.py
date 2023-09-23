from pathlib import Path
import json
from collections import deque
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

Constraints:

	2 <= n <= 10^5
	1 <= edges.length <= min(10^5, n * (n - 1) / 2)
	edges[i].length == 2
	0 <= fromi, toi < n
	All pairs (fromi, toi) are distinct.
"""
import pytest
import sys


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """TLE. Works for cyclic"""
        class Graph:
            def __init__(self, n, edges):
                self.g = [set() for _ in range(n)]
                indegree = [0 for _ in range(n)]
                for f, t in edges:
                    self.g[f].add(t)
                    indegree[t] += 1
                self.queue = list(sorted([[cnt, v] for v, cnt in enumerate(indegree)]))
                self.qi = 0
                self.index = {v: i for i, (cnt, v) in enumerate(self.queue)}
                self.remain = set(range(n))

            def traverse(self, u):
                self.remain.discard(u)
                for v in self.g[u]:
                    vi = self.index[v]
                    self.queue[vi][0] -= 1
                    while vi>0 and self.queue[vi-1][0] > self.queue[vi][0]:
                        self.index[self.queue[vi-1][1]] = vi
                        self.index[self.queue[vi][1]] = vi-1
                        self.queue[vi-1], self.queue[vi] = self.queue[vi], self.queue[vi-1]
                        vi -= 1
                    if v in self.remain:
                        self.traverse(v)

            def iterate(self):
                while self.qi < len(self.queue):
                    if self.queue[self.qi][1] not in self.remain:
                        self.qi += 1
                    else:
                        yield self.queue[self.qi][1]

        g = Graph(n, edges)
        ret = []
        for v in g.iterate():
            ret.append(v)
            g.traverse(v)

        return ret

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """Sep 22, 2023 17:22"""
        g = [set() for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for f, t in edges:
            g[f].add(t)
            indegree[t] += 1


        remain = set(range(n))

        def traverse(i):
            remain.remove(i)
            for j in g[i]:
                indegree[j] -= 1
                if j in remain:
                    traverse(j)

        ret = []
        while remain:
            for _, i in sorted([(cnt, i) for i, cnt in enumerate(indegree)]):
                if i in remain:
                    ret.append(i)
                    traverse(i)
        return ret


@pytest.mark.parametrize('args', [
    ((6, [[0,1],[0,2],[2,5],[3,4],[4,2]], [0,3])),
    ((5, [[0,1],[2,1],[3,1],[1,4],[2,4]], [0,2,3])),
    ((json.load(open(Path(__file__).parent/'testcase.json')))),
])
def test(args):
    assert args[-1] == Solution().findSmallestSetOfVertices(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
