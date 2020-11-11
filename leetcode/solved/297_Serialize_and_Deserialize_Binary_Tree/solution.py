
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
from collections import deque
import sys
import pytest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque([root])
        ret = []
        while queue:
            n = queue.popleft()
            if n is not None:
                ret.append(str(n.val))
                queue.append(n.left)
                queue.append(n.right)
            else:
                ret.append('.')
        while ret[-1] == '.':
            ret.pop()
        return '_'.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split('_')
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        branches = ['left', 'right']
        i = 0
        for v in vals[1:]:
            n = None
            if v != '.':
                n = TreeNode(int(v))
                queue.append(n)
            setattr(queue[0], branches[i], n)
            if i == 1:
                queue.popleft()
            i ^= 1
        return root


def compare_tree(t1, t2):
    if t1 and t2:
        return t1.val == t2.val \
            and compare_tree(t1.left, t2.left) \
            and compare_tree(t1.right, t2.right)
    elif not t1 and not t2:
        return True
    else:
        return False


def build_tree(lst):
    root = TreeNode(lst[0])
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = TreeNode(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


@pytest.mark.parametrize('nodes', [
    ([1,2,3,None,None,4,5]),
    ([-1,0,1]),
])
def test(nodes):
    print()
    tree = build_tree(nodes)
    codec = Codec()
    data = codec.serialize(tree)
    print(data)
    assert compare_tree(tree, codec.deserialize(data))

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
