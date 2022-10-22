#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

	Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
	cur's original left subtree should be the left subtree of the new left subtree root.
	cur's original right subtree should be the right subtree of the new right subtree root.
	If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	The depth of the tree is in the range [1, 104].
	-100 <= Node.val <= 100
	-105 <= val <= 105
	1 <= depth <= the depth of tree + 1
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """06/20/2020 17:37"""
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

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """10/21/2022 20:39"""
        def add_row(root, depth, direction):
            if depth == 1:
                ret = TreeNode(val)
                setattr(ret, direction, root)
                return ret
            if not root:
                return None
            root.left = add_row(root.left, depth-1, 'left')
            root.right = add_row(root.right, depth-1, 'right')
            return root

        return add_row(root, depth, 'left')


@pytest.mark.parametrize('values, val, depth, expected', [
    ([4,2,6,3,1,5], 1, 2, [4,1,1,2,None,None,6,3,1,5]),
    ([4,2,None,3,1], 1, 3, [4,2,None,1,1,3,None,None,1]),
])
def test(values, val, depth, expected):
    actual = Solution().addOneRow(build_tree(values), val, depth)
    assert build_tree(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
