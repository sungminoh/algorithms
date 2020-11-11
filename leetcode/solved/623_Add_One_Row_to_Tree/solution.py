#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:

Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1

Note:

The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""
from jedi import debug
import sys
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def dfs(node, depth):
            if not node:
                return
            if depth == d-1:
                left = node.left if node.left else None
                node.left = TreeNode(v)
                node.left.left = left
                right = node.right if node.right else None
                node.right = TreeNode(v)
                node.right.right = right
                return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            return
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        else:
            dfs(root, 1)
            return root


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


def compare_tree(t1, t2):
    if t1 and t2:
        return t1.val == t2.val \
            and compare_tree(t1.left, t2.left) \
            and compare_tree(t1.right, t2.right)
    elif not t1 and not t2:
        return True
    else:
        return False


@pytest.mark.parametrize('nodes, v, d, expected', [
    ([4,2,6,3,1,5], 1, 2, [4,1,1,2,None,None,6,3,1,5]),
    ([4,2,None,3,1], 1, 3, [4,2,None,1,1,3,None,None,1])
])
def test(nodes, v, d, expected):
    root = build_tree(nodes)
    assert compare_tree(build_tree(expected), Solution().addOneRow(root, v, d))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
