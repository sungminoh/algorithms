#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]

Constraints:

	The number of nodes in the given tree will be in the range [1, 100].
	0 <= Node.val <= 1000
"""
from typing import Tuple
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: TreeNode) -> Tuple[TreeNode, TreeNode]:
            if not node.left:
                root = node
            else:
                root, parent = inorder(node.left)
                parent.right = node
                node.left = None
            tail = node
            if node.right:
                node.right, tail = inorder(node.right)
            return root, tail

        return inorder(root)[0]


@pytest.mark.parametrize('values, expected', [
    ([5,3,6,2,4,None,8,1,None,None,None,7,9], [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9]),
    ([5,1,7], [1,None,5,None,7]),
])
def test(values, expected):
    assert build_tree(expected) == Solution().increasingBST(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
