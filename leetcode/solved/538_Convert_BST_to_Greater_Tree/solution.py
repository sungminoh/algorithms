#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:

Input: root = [0,null,1]
Output: [1,null,1]

Constraints:

	The number of nodes in the tree is in the range [0, 104].
	-104 <= Node.val <= 104
	All the values in the tree are unique.
	root is guaranteed to be a valid binary search tree.

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        """12/15/2020 17:21"""
        if not root:
            return root

        def conv(node: TreeNode, val=0) -> TreeNode:
            if node.right:
                node.val += conv(node.right, val)
            else:
                node.val += val
            ret = node.val
            if node.left:
                ret = conv(node.left, node.val)
            return ret

        conv(root)
        return root

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node, carry=0):
            if not node:
                return 0
            val = node.val
            right = traverse(node.right, carry)
            left = traverse(node.left, carry=right+val+carry)
            node.val += right + carry
            return val + left + right

        traverse(root)
        return root


@pytest.mark.parametrize('values, expected', [
    ([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8], [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]),
    ([0,None,1], [1,None,1]),
    ([1,0,2], [3,3,2]),
    ([3,2,4,1], [7,9,4,10]),
    ([-3,-4,0,None,None,-2,1], [-4,-8,1,None,None,-1,1])
])
def test(values, expected):
    assert build_tree(expected) == Solution().convertBST(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
