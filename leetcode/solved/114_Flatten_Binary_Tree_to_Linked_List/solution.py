#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, flatten the tree into a "linked list":

	The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
	The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
	-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from typing import Tuple
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
    def flatten(self, root):
        """05/07/2018 14:19"""
        def flatten_(root):
            if not root:
                return None, None
            t = root
            hl, tl = flatten_(root.left)
            hr, tr = flatten_(root.right)
            if hl:
                root.right = hl
                t = tl
            if hr:
                t.right = hr
                t = tr
            root.left = None
            return root, t

        flatten_(root)
        return root

    def flatten(self, root: TreeNode) -> None:
        """05/27/2021 06:25"""
        def to_list(node: TreeNode):
            if node is None:
                return None, None
            left_head, left_tail = to_list(node.left)
            right_head, right_tail = to_list(node.right)
            if left_tail is None and right_head is None:
                return node, node
            node.left = None
            if left_tail is None:
                node.right, right_head.left = right_head, None
                return node, right_tail
            node.right, left_head.left = left_head, None
            if right_head is None:
                return node, left_tail
            left_tail.right, right_head.left = right_head, None
            return node, right_tail

        to_list(root)[0]

    def flatten(self, root: Optional[TreeNode]) -> None:
        """08/06/2022 22:42"""
        def flatten_head_tail(
            root: Optional[TreeNode]) -> Tuple[TreeNode, TreeNode]:
            if not root:
                return None, None
            lh, lt = flatten_head_tail(root.left)
            rh, rt = flatten_head_tail(root.right)
            if lh:
                root.right = lh
                lt.right = rh
            else:
                root.right = rh
            root.left = None
            return root, rt or lt or root

        flatten_head_tail(root)


@pytest.mark.parametrize('values, expected', [
    ([1,2,5,3,4,None,6], [1,None,2,None,3,None,4,None,5,None,6]),
    ([], []),
    ([0], [0]),
])
def test(values, expected):
    tree = build_tree(values)
    Solution().flatten(tree)
    assert build_tree(expected) == tree


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
