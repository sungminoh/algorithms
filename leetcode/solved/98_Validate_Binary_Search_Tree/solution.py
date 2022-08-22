#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-231 <= Node.val <= 231 - 1
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
    def isValidBST(self, root):
        """05/06/2018 06:10"""
        m = -float('inf')
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left
            while not p and stack:
                p = stack.pop()
                if p.val <= m:
                    return False
                else:
                    m = p.val
                p = p.right
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder
        cur = -float('inf')

        def insert(stack, node):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        insert(stack, root)

        while stack:
            n = stack.pop()
            if n.val <= cur:
                return False
            cur = n.val
            insert(stack, n.right)
        return True


@pytest.mark.parametrize('values, expected', [
    ([2,1,3], True),
    ([5,1,4,None,None,3,6], False),
    ([2,2,2], False),
    ([5,4,6,None,None,3,7], False),
])
def test(values, expected):
    root = build_tree(values)
    assert expected == Solution().isValidBST(root)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
