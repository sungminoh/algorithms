#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
from typing import List


class Solution:
    def build_tree(self, n, edges):
        tree = [[] for _ in range(n)]
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
        return tree

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        tree = self.build_tree(n, edges)
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


if __name__ == '__main__':
    cases = [
        ((4, [[1, 0], [1, 2], [1, 3]]), [1]),
        ((6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]), [3,4]),
        ((3, [[0,1],[0,2]]), [0]),
        ((1, []), [0]),
        ((2, [[0,1]]), [0,1]),
        ((6, [[0,1],[0,2],[0,3],[3,4],[4,5]]), [3]),
        ((7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]), [1,2])
        #    5
        #    3
        #  0 1 2 4 6

    ]
    for case, expected in cases:
        actual = list(sorted(Solution().findMinHeightTrees(*case)))
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
