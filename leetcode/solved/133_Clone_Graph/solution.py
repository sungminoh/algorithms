#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return f'Node({self.label}, [{",".join(str(x.label) for x in self.neighbors)}])'


from collections import defaultdict


class Solution:
    def __init__(self):
        self.yet = set()
        self.visited = set()

    def serialize(self, node):
        if not node:
            return ''
        neighbors = [str(node.label)]
        for n in node.neighbors:
            if n.label in self.visited:
                continue
            neighbors.append(str(n.label))
            if n.label != node.label:
                self.yet.add(n)
        self.visited.add(node.label)
        if self.yet:
            return ','.join(neighbors) + '#' + self.serialize(self.yet.pop())
        return ','.join(neighbors)

    def deserialize(self, s, label):
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
        nodes = {n: UndirectedGraphNode(int(n)) for n in node_info.keys()}
        for n, neighbors in node_info.items():
            nodes[n].neighbors = [nodes[j] for j in neighbors]
        return nodes[label]


    def get(self, label):
        if label not in self.pool:
            self.pool[label] = UndirectedGraphNode(label)
        return self.pool[label]

    def bfs(self, node):
        visited = set()
        ret = self.get(node.label)
        queue = [(node, ret)]
        while queue:
            ori, new = queue.pop()
            if ori.label in visited:
                continue
            for on in ori.neighbors:
                nn = self.get(on.label)
                new.neighbors.append(nn)
                queue.append((on, nn))
            visited.add(ori.label)
        return ret

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        if not node.neighbors:
            return UndirectedGraphNode(node.label)
        self.pool = dict()
        return self.bfs(node)


def main():
    nodes = dict()
    neighbors = defaultdict(list)
    s = input()
    while s:
        i, j = [int(x) for x in s.split()]
        if i not in nodes:
            nodes[i] = UndirectedGraphNode(i)
        if j not in nodes:
            nodes[j] = UndirectedGraphNode(j)
        if i != j:
            neighbors[j].append(i)
        neighbors[i].append(j)
        for i, js in neighbors.items():
            nodes[i].neighbors = [nodes[j] for j in js]
        s = input()
    print(nodes)
    print(Solution().serialize(Solution().cloneGraph(next(iter(nodes.values())))))


if __name__ == '__main__':
    main()
