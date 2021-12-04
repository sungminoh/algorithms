#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:

	1 <= inorder.length <= 3000
	postorder.length == inorder.length
	-3000 <= inorder[i], postorder[i] <= 3000
	inorder and postorder consist of unique values.
	Each value of postorder also appears in inorder.
	inorder is guaranteed to be the inorder traversal of the tree.
	postorder is guaranteed to be the postorder traversal of the tree.
"""
from collections import defaultdict
from typing import Optional
from typing import List
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree, serialize_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree_(self, inorder, postorder):
        """05/06/2018 19:12"""
        memo = defaultdict(list)
        for i, v in enumerate(inorder):
            memo[v].append(i)

        def build(in_s, in_e, post_s, post_e):
            if in_e < in_s or post_e < post_s:
                return None
            root = TreeNode(postorder[post_e])
            i = memo[root.val].pop()
            root.left = build(in_s, i-1, post_s, post_s+(i-1-in_s))
            root.right = build(i+1, in_e, post_s+(i-1-in_s)+1, post_e-1)
            return root

        return build(0, len(inorder)-1, 0, len(postorder)-1)

    def buildTree(self, inorder, postorder):
        """05/06/2018 19:18"""
        def build(v):
            if not postorder or inorder[-1] == v:
                return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(v)
            return root
        return build(None)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {x: i for i, x in enumerate(inorder)}
        def reconstruct(i, j, x, y):
            root = TreeNode(postorder[y])
            inorder_pivot = inorder_map[postorder[y]]
            left_tree_size = inorder_pivot - i
            right_tree_size = j - inorder_pivot
            if left_tree_size:
                root.left = reconstruct(i, inorder_pivot-1, x, x+left_tree_size-1)
            if right_tree_size:
                root.right = reconstruct(inorder_pivot+1, j, x+left_tree_size, y-1)
            return root

        return reconstruct(0, len(inorder)-1, 0, len(postorder)-1)


@pytest.mark.parametrize('inorder, postorder, expected', [
    ([9,3,15,20,7], [9,15,7,20,3], [3,9,20,None,None,15,7]),
    ([-1], [-1], [-1]),
])
def test(inorder, postorder, expected):
    tree = Solution().buildTree(inorder, postorder)
    print()
    print(tree)
    assert expected == serialize_tree(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
