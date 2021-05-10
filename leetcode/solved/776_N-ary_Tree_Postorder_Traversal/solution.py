#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:

	The number of nodes in the tree is in the range [0, 104].
	0 <= Node.val <= 104
	The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import sys
from collections import deque
from typing import List
import pytest


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self):
        if not self.children:
            return '%2s' % self.val
        children_reprs = [repr(child).split('\n') for child in self.children]
        max_lines = len(max(children_reprs, key=len))
        for children_repr in children_reprs:
            while len(children_repr) < max_lines:
                children_repr.append(' '*len(children_repr[0]))
        lines = ['|'.join(siblings) for siblings in zip(*children_reprs)]
        header =('{:^%s}' % len(lines[0])).format('%2s' % self.val)
        return '\n'.join([header, *lines])


def build_node(values):
    if not values:
        return None
    queue = deque([Node(v) if v is not None else None for v in values])
    head = queue.popleft()
    if not queue:
        return head
    else:
        queue.popleft()
    cur = [head]
    nxt = []
    i = 0
    while queue:
        children = []
        while queue and queue[0] is not None:
            children.append(queue.popleft())
        if queue:
            queue.popleft()
        cur[i].children = children
        i += 1
        nxt.extend(children)
        if i == len(cur):
            cur = nxt
            i = 0
            nxt = []
    return head


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ret = []
        for child in (root.children or []):
            ret.extend(self.postorder(child))
        ret.append(root.val)
        return ret


@pytest.mark.parametrize('values, expected', [
([1,None,3,2,4,None,5,6], [5,6,3,2,4,1]),
([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14], [2,6,14,11,7,3,12,8,4,13,9,10,5,1]),
])
def test(values, expected):
    node = build_node(values)
    print()
    print(node)
    assert expected == Solution().postorder(node)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
