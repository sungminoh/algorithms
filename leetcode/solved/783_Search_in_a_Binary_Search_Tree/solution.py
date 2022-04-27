#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:

	The number of nodes in the tree is in the range [1, 5000].
	1 <= Node.val <= 107
	root is a binary search tree.
	1 <= val <= 107
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        return root


@pytest.mark.parametrize('values, val, expected', [
    ([4,2,7,1,3], 2, [2,1,3]),
    ([4,2,7,1,3], 5, []),
])
def test(values, val, expected):
    assert build_tree(expected) == Solution().searchBST(build_tree(values), val)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
