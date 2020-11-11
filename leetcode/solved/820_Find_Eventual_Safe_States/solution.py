#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Note:

	graph will have length at most 10000.
	The number of edges in the graph will not exceed 32000.
	Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
"""
import sys
from typing import List
import pytest


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph = dict(enumerate(graph))
        # 0: None, 1: visited: 2: safe, 3: danger
        safe = [0] * len(graph)
        def is_safe(s):
            if safe[s] in {2, 3}:
                return safe[s] == 2
            if not graph[s]:
                safe[s] = 2
                return True
            safe[s] = 1
            ret = True
            for e in graph[s]:
                if safe[e] == 1:
                    safe[s] = 3
                    return False
                else:
                    ret &= is_safe(e)
            safe[s] = 2 if ret else 3
            return ret

        for i in range(len(graph)):
            is_safe(i)

        return [i for i, v in enumerate(safe) if v == 2]


@pytest.mark.parametrize('graph, expected', [
    ([[1,2],[2,3],[5],[0],[5],[],[]], [2,4,5,6]),
])
def test(graph, expected):
    assert expected == Solution().eventualSafeNodes(graph)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
