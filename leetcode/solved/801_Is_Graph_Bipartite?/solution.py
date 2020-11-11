#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

Note:

	graph will have length in range [1, 100].
	graph[i] will contain integers in range [0, graph.length - 1].
	graph[i] will not contain i or duplicate values.
	The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
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


@pytest.mark.parametrize('graph, expected', [
    ([[1,3], [0,2], [1,3], [0,2]], True),
    ([[1,2,3], [0,2], [0,1,3], [0,2]], False),
    ([[4],[],[4],[4],[0,2,3]], True),
    ([[], [2,4], [1,4], [], [1,2]], False),
    ([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]], False)
])
def test(graph, expected):
    assert expected == Solution().isBipartite(graph)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
