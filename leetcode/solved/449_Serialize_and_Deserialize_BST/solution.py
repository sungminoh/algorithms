
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
from collections import deque
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        arr = []
        queue = deque([root])
        while queue:
            n = queue.popleft()
            if n == '!':
                arr[-1] += '!'
            elif n is None:
                arr[-1] += '.'
            else:
                arr.append(str(n.val))
                if not n.left and not n.right:
                    queue.append('!')
                else:
                    queue.append(n.left)
                    queue.append(n.right)
        return '-'.join(arr).rstrip('!')

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.replace('!', '-!').replace('.', '-.')
        arr = deque(data.split('-'))
        nodes = [TreeNode(int(arr.popleft()))]
        i = 0
        while arr:
            if arr[0] == '!':
                arr.popleft()
                i += 1
            else:
                l, r = arr.popleft(), arr.popleft()
                if l != '.':
                    left_node = TreeNode(int(l))
                    nodes[i].left = left_node
                    nodes.append(left_node)
                if r != '.':
                    right_node = TreeNode(int(r))
                    nodes[i].right = right_node
                    nodes.append(right_node)
                i += 1
        return nodes[0]
