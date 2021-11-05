#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100
"""
from typing import Optional
import sys
import pytest
sys.path.append('../')
from exercise.tree import TreeNode, build_tree, print_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root


@pytest.mark.parametrize('nodes, expected', [
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
    ([], []),
])
def test(nodes, expected):
    tree = build_tree(nodes)
    print('\n----------------------')
    print(tree)
    actual = Solution().invertTree(tree)
    print()
    print(actual)
    assert build_tree(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
