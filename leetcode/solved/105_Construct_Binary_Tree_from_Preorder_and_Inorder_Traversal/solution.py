#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,None,None,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

	1 <= preorder.length <= 3000
	inorder.length == preorder.length
	-3000 <= preorder[i], inorder[i] <= 3000
	preorder and inorder consist of unique values.
	Each value of inorder also appears in preorder.
	preorder is guaranteed to be the preorder traversal of the tree.
	inorder is guaranteed to be the inorder traversal of the tree.
"""
from pathlib import Path
from typing import List
import pytest
import sys
sys.path.append(str(Path('__file__').absolute().parent.parent))
from exercise.tree import TreeNode, build_tree


class Solution:
    def buildTree(self, preorder, inorder):
        """
        05/07/2018 10:44
        Time complexity: O(n)
        """
        def build(v):
            if not preorder or inorder[0] == v:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(v)
            return root
        return build(None)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Time complexity; O(n^2)
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1 or len(inorder) == 1:
            return root
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(i, j, v):
            if i == len(preorder) or inorder[j] == v:
                return None, i, j+1
            root = TreeNode(preorder[i])
            root.left, i, j = build(i+1, j, root.val)
            root.right, i, j = build(i, j, v)
            return root, i, j
        return build(0, 0, None)[0]



@pytest.mark.parametrize('preorder, inorder, expected', [
([3,9,20,15,7], [9,3,15,20,7], [3,9,20,None,None,15,7]),
([20,15,7], [15,20,7], [20,15,7]),
([-1], [-1], [-1]),
])
def test(preorder, inorder, expected):
    actual = Solution().buildTree(preorder, inorder)
    print()
    print(actual)
    assert build_tree(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
