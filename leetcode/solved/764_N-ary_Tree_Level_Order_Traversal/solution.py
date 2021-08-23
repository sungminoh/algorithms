#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:

	The height of the n-ary tree is less than or equal to 1000
	The total number of nodes is between [0, 104]
"""
import sys
from itertools import zip_longest
from collections import deque
from typing import List
import pytest


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        if not self.children:
            return '%2s' % str(self.val)
        children = [repr(c).split('\n') for c in self.children]
        total_length = sum(len(x[0]) for x in children)
        ret = [('%2s' % str(self.val)).center(total_length + len(children) - 1)]
        for lines in zip_longest(*children):
            line = []
            for i, l in enumerate(lines):
                if l is None:
                    l = ' ' * len(children[i][0])
                line.append(l)
            ret.append('|'.join(line))
        return '\n'.join(ret)


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """04/28/2020 23:57"""
        if not root:
            return []
        queue = deque([(0, root)])
        ret = []
        while queue:
            l, n = queue.popleft()
            if l < len(ret):
                ret[l].append(n.val)
            else:
                ret.append([n.val])
            if n.children:
                for c in n.children:
                    queue.append((l + 1, c))
        return ret

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ret = []
        nodes = [root]
        while nodes:
            ret.append([n.val for n in nodes])
            next_level = []
            for n in nodes:
                for c in (n.children or []):
                    next_level.append(c)
            nodes = next_level
        return ret


def build_tree(arr) -> 'Node':
    """04/28/2020 23:57"""
    if not arr:
        return None
    root = Node(arr[0])
    queue = deque([root])
    i = 2
    while i < len(arr):
        vals = []
        while i < len(arr) and arr[i] is not None:
            vals.append(Node(arr[i]))
            queue.append(vals[-1])
            i += 1
        node = queue.popleft()
        node.children = vals
        i += 1
    return root


def build_tree(nodes):
    if not nodes:
        return None
    root = Node(nodes[0])
    queue = deque([root])
    cur = None
    children = []
    for i, n in enumerate(nodes[1:]):
        if n is None:
            cur = queue.popleft()
        else:
            if cur.children is None:
                cur.children = []
            node = Node(n)
            cur.children.append(node)
            queue.append(node)
    return root


@pytest.mark.parametrize('nodes, expected', [
    ([1,None,3,2,4,None,5,6], [[1],[3,2,4],[5,6]]),
    ([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]),
    ([], [])
])
def test(nodes, expected):
    tree = build_tree(nodes)
    print()
    print(tree)
    assert expected == Solution().levelOrder(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
