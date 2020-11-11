#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Constraints:

	The number of nodes in the graph will be in the range [2, 15].
	You can print different paths in any order, but you should keep the order of nodes inside one path.
"""
import sys
from typing import List
import pytest


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph = dict(enumerate(graph))
        memo = [[] for _ in range(len(graph))]

        def paths(s, e):
            if s == e:
                return [[e]]
            if memo[s]:
                return memo[s]
            ret = []
            for n in graph[s]:
                ret.extend([s] + p for p in paths(n, e))
            memo[s] = ret
            return ret

        return paths(0, len(graph)-1)


@pytest.mark.parametrize('graph, expected', [
    ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
])
def test(graph, expected):
    assert expected == Solution().allPathsSourceTarget(graph)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
