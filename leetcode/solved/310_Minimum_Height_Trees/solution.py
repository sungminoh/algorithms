#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:

	1 <= n <= 2 * 104
	edges.length == n - 1
	0 <= ai, bi < n
	ai != bi
	All the pairs (ai, bi) are distinct.
	The given input is guaranteed to be a tree and there will be no repeated edges.
"""
from itertools import chain
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """12/27/2019 06:34"""
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        tree = [[] for _ in range(n)]
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        degrees = [len(nodes) for nodes in tree]
        ends = {n for n, degree in enumerate(degrees) if degree == 1}
        queue = [ends]
        layer = None
        while queue:
            layer = queue.pop(0)
            new_layer = set()
            for s in layer:
                for e in tree[s]:
                    degrees[e] -= 1
                    if degrees[e] == 1:
                        new_layer.add(e)
            if new_layer:
                queue.append(new_layer)
        return layer

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """TLE"""
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        distance = [[0]*n for _ in range(n)]
        stack = []

        def merge(children, parent):
            neighbors = list(children.keys())
            for i in range(len(neighbors)):
                for j in range(i+1, len(neighbors)):
                    a = neighbors[i]
                    b = neighbors[j]
                    for ac in children[a]:
                        for bc in children[b]:
                            distance[ac][bc] = distance[bc][ac] = distance[ac][parent] + distance[parent][bc]

        def dfs(i):
            for d, p in enumerate(stack):
                distance[p][i] = distance[i][p] = len(stack)-d
            children = {}
            stack.append(i)
            for j in graph[i]:
                if j != stack[-1] and distance[i][j] == 0:
                    children[j] = dfs(j)
            stack.pop()

            merge(children, i)
            return [i, *children.keys(), *chain(*children.values())]


        dfs(0)

        mh = n
        ret = []
        for i, dists in enumerate(distance):
            h = max(dists)
            if h == mh:
                ret.append(i)
            elif h < mh:
                ret = [i]
                mh = h
        return ret

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        degree = [len(neighbors) for neighbors in graph]
        shell = [i for i, d in enumerate(degree) if d == 1]
        while shell:
            new_shell = []
            for i in shell:
                for j in graph[i]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        new_shell.append(j)
            if not new_shell:
                break
            shell = new_shell

        return shell


@pytest.mark.parametrize('n, edges, expected', [
    (4, [[1,0],[1,2],[1,3]], [1]),
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3,4]),
    (6, [[0,1],[0,2],[0,3],[3,4],[4,5]], [3]),
    (1, [], [0]),
])
def test(n, edges, expected):
    print()
    assert expected == Solution().findMinHeightTrees(n, edges)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
