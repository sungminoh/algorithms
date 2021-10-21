#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Example 1:

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:

Input: preorder = [1,3]
Output: [1,null,3]

Constraints:

	1 <= preorder.length <= 100
	1 <= preorder[i] <= 1000
	All the values of preorder are unique.
"""
from typing import Optional
from typing import List
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """Recursion"""
        if not preorder:
            return None

        def build(i, lb, ub):
            if i >= len(preorder) or preorder[i] >= ub or preorder[i] <= lb:
                return i, None
            root = TreeNode(preorder[i])
            i, root.left = build(i+1, lb, root.val)
            i, root.right = build(i, root.val, ub)
            return i, root

        return build(0, 0, float('inf'))[1]

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """Stack"""
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        for p in preorder[1:]:
            node = TreeNode(p)
            if p < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                parent = stack[-1]
                while stack and stack[-1].val < p:
                    parent = stack.pop()
                parent.right = node
                stack.append(node)

        return root




@pytest.mark.parametrize('preorder, expected', [
    ([8,5,1,7,10,12], [8,5,10,1,7,None,12]),
    ([1,3], [1,None,3]),
])
def test(preorder, expected):
    actual = Solution().bstFromPreorder(preorder)
    print()
    print(actual)
    assert build_tree(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
