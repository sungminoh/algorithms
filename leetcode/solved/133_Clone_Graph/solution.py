#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:

	The number of nodes in the graph is in the range [0, 100].
	1 <= Node.val <= 100
	Node.val is unique for each node.
	There are no repeated edges and no self-loops in the graph.
	The Graph is connected and all nodes can be visited starting from the given node.
"""
import sys
from collections import defaultdict
from itertools import chain
import pytest


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return f'Node({self.val}, {[x.val for x in self.neighbors]})'


def get_all_edges_and_nodes(node):
    edges = set()
    nodes = {}
    def dfs(node):
        if id(node) in nodes:
            return
        nodes[id(node)] = node
        for n in node.neighbors:
            edges.add(tuple(sorted([id(node), id(n)])))
            dfs(n)
    dfs(node)
    return edges, nodes


def is_same(a, b, cache=None):
    if a is None and b is None:
        return True
    if id(a) > id(b):
        return is_same(b, a, cache)
    cache = cache or {}
    key = (id(a), id(b))
    if key in cache:
        return cache[key]
    if a.val != b.val:
        cache[key] = False
        return False
    cache[key] = None
    ret = True
    for n in a.neighbors:
        sub = False
        for m in b.neighbors:
            if is_same(n, m, cache) != False:
                sub = True
        ret &= sub
    return ret


def build_graph(neighbors):
    if not neighbors:
        return None

    nodes = {}
    for i in range(1, len(neighbors)+1):
        nodes.setdefault(i, Node(i))

    for i, neighbor in enumerate(neighbors, 1):
        for n in neighbor:
            if nodes[n] not in nodes[i].neighbors:
                nodes[i].neighbors.append(nodes[n])
    return nodes[1]


def serialize(node, yet=None, visited=None):
    yet = yet or set()
    visited = visited or set()
    if not node:
        return ''
    neighbors = [str(node.val)]
    for n in node.neighbors:
        if n.val in visited:
            continue
        neighbors.append(str(n.val))
        if n.val != node.val:
            yet.add(n)
    visited.add(node.val)
    if yet:
        return ','.join(neighbors) + '#' + serialize(yet.pop(), yet=yet, visited=visited)
    return ','.join(neighbors)

def deserialize(s, val):
    parsed = [ss.split(',') for ss in s.split('#')]
    node_info = defaultdict(list)
    for ns in parsed:
        i = int(ns[0])
        js = ns[1:]
        for j in js:
            j = int(j)
            if i != j:
                node_info[i].append(j)
            node_info[j].append(i)
    nodes = {n: Node(int(n)) for n in node_info.keys()}
    for n, neighbors in node_info.items():
        nodes[n].neighbors = [nodes[j] for j in neighbors]
    return nodes[val]


class Solution:
    def cloneGraph(self, node):
        """07/08/2018 05:23"""
        pool = dict()

        def get(val):
            if val not in pool:
                pool[val] = Node(val)
            return pool[val]

        def bfs(node):
            visited = set()
            ret = get(node.val)
            queue = [(node, ret)]
            while queue:
                ori, new = queue.pop()
                if ori.val in visited:
                    continue
                for on in ori.neighbors:
                    nn = get(on.val)
                    new.neighbors.append(nn)
                    queue.append((on, nn))
                visited.add(ori.val)
            return ret

        if not node:
            return
        if not node.neighbors:
            return Node(node.val)

        return bfs(node)

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        saved = {}

        def deepcopy(node):
            if id(node) in saved:
                return saved[id(node)]
            saved[id(node)] = Node(node.val)
            saved[id(node)].neighbors.extend([deepcopy(x) for x in node.neighbors])
            return saved[id(node)]

        return deepcopy(node)


@pytest.mark.parametrize('edges, expected', [
    ([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]),
    ([[]], [[]]),
    ([], []),
])
def test(edges, expected):
    a = build_graph(edges)
    b = Solution().cloneGraph(a)
    assert serialize(a) == serialize(b)
    assert is_same(a, b)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))



