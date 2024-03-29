#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:

	n == graph.length
	2 <= n <= 15
	0 <= graph[i][j] < n
	graph[i][j] != i (i.e., there will be no self-loops).
	All the elements of graph[i] are unique.
	The input graph is guaranteed to be a DAG.
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """09/17/2020 22:46"""
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

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Dec 09, 2021 10:57"""
        ret = []
        def dfs(i, backtrack):
            if i == len(graph)-1:
                ret.append(backtrack[:])
            else:
                for j in graph[i]:
                    backtrack.append(j)
                    dfs(j, backtrack)
                    backtrack.pop()

        dfs(0, [0])
        return ret

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """Feb 19, 2023 22:20"""
        n = len(graph)-1

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return [[i]]
            ret = []
            for j in graph[i]:
                ret.extend([[i, *path] for path in dfs(j)])
            return ret

        return dfs(0)


@pytest.mark.parametrize('graph, expected', [
    ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
    ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
    ([[1],[]], [[0,1]]),
    ([[1,2,3],[2],[3],[]], [[0,1,2,3],[0,2,3],[0,3]]),
    ([[1,3],[2],[3],[]], [[0,1,2,3],[0,3]]),
])
def test(graph, expected):
    assert sorted(expected) == sorted(Solution().allPathsSourceTarget(graph))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
