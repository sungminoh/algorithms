#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are workloads and capacities of trucks.
We want to load each workload to the earliest truck that has higher capacity
than the workload.
Return a list of truck indexes where each workload is loaded.
If there is no truck for a workload, use -1 instead.

For example,
When the workloads are [1,2,1] and truck capacities are [0,2,1].
The earliest truck that can hold the 0'th workload is the 1'th truck.
After load the 0'th workload, truck capacities became [0,1,1].
There is no truck where we can load 1'th workload on.
For the last workload, we can load it on 1'th truck.
So the return should be [1, -1, 1]
"""

import pytest
import sys
import random
from typing import List


class TreeNode:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.minidx = idx
        self.left = None
        self.right = None

    def __repr__(self):
        from itertools import zip_longest
        left_lines = repr(self.left).split('\n') if self.left else []
        right_lines = repr(self.right).split('\n') if self.right else []
        val = rf'({self.val}, {self.idx}, {self.minidx})'
        node_padding = len(val)
        left_padding = len(left_lines[0]) if left_lines else 0
        right_padding = len(right_lines[0]) if right_lines else 0
        lines = [' '*left_padding + val + ' '*right_padding]
        for ll, rl in zip_longest(left_lines, right_lines):
            if ll is not None:
                lines.append(ll + ' '*node_padding + (rl or ''))
            else:
                lines.append(' '*(node_padding + left_padding) + (rl or ''))
        return '\n'.join(lines)


class SegmentTree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def update_minidx(self, node: TreeNode):
        node.minidx = min(
            node.left.minidx if node.left else float('inf'),
            node.right.minidx if node.right else float('inf'),
            node.idx
        )

    def insert(self, node: TreeNode):
        self.nodes[node.idx] = node

        if self.root is None:
            self.root = node
            return

        def insert_recursive(root: TreeNode, node: TreeNode):
            # root.minidx = min(root.minidx, node.idx)
            if node.val < root.val:
                if not root.left:
                    root.left = node
                else:
                    insert_recursive(root.left, node)
            else:
                if not root.right:
                    root.right = node
                else:
                    insert_recursive(root.right, node)
            self.update_minidx(root)

        insert_recursive(self.root, node)

    def delete(self, node: TreeNode):
        def delete_recursive(root: TreeNode, node: TreeNode) -> TreeNode:
            if root.idx == node.idx:
                self.nodes.pop(node.idx)
                if not root.right:
                    return root.left
                if not root.left:
                    return root.right
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.idx = successor.idx
                root.right = delete_recursive(root.right, successor)
                self.nodes[root.idx] = root
            elif node.val < root.val:
                root.left = delete_recursive(root.left, node)
            else:
                root.right = delete_recursive(root.right, node)
            self.update_minidx(root)
            return root

        self.root = delete_recursive(self.root, node)

    def find(self, val: int):
        def find_recursive(root: TreeNode, val: int):
            if not root:
                return -1
            if root.val < val:
                return find_recursive(root.right, val)
            else:
                left = find_recursive(root.left, val)
                ret = min(
                    left if left >= 0 else float('inf'),
                    root.idx,
                    root.right.minidx if root.right else float('inf'))
                return -1 if ret == float('inf') else ret

        ret = find_recursive(self.root, val)
        return ret

    def get(self, idx: int):
        return self.nodes[idx]


def load(workloads: List[int], trucks: List[int]):
    tree = SegmentTree()
    for i, t in enumerate(trucks):
        tree.insert(TreeNode(t, i))

    ans = []
    for w in workloads:
        i = tree.find(w)
        ans.append(i)
        if i >= 0:
            node = tree.get(i)
            new_node = TreeNode(node.val - w, node.idx)
            tree.delete(node)
            tree.insert(new_node)

    return ans


def load_bruteforce(workloads, trucks):
    trucks = trucks[:]
    ret = []
    for w in workloads:
        for i, c in enumerate(trucks):
            if c >= w:
                ret.append(i)
                trucks[i] -= w
                break
        else:
            ret.append(-1)
    return ret


def gen_case(n, m):
    workloads = [random.randint(0, m) for _ in range(n)]
    trucks = [random.randint(0, m) for _ in range(n)]
    return workloads, trucks


@pytest.mark.parametrize(('workloads', 'trucks'), [
    ([1,2,1], [0,2,1]),
    ([3], [0]),
    ([8], [1]),
    ([9], [9]),
    ([0, 4, 8, 9, 2], [5, 5, 10, 9, 5]),
    ([40, 28, 4, 83, 4, 82, 33, 23, 63, 8],
     [79, 39, 62, 97, 92, 77, 90, 74, 97, 15]),
    gen_case(0, 0),
    gen_case(1, 10),
    gen_case(5, 10),
    gen_case(10, 100),
    gen_case(20, 100),
    gen_case(30, 100),
    gen_case(40, 100),
    gen_case(60, 100),
    gen_case(100, 100),
])
def test(workloads, trucks):
    expected = load_bruteforce(workloads, trucks)
    actual = load(workloads, trucks)
    # print()
    # print(workloads)
    # print(trucks)
    # print('exp:', expected)
    # print('act:', actual)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))




