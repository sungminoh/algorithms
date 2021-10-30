#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:

	The number of nodes in the tree is in the range [2, 100].
	1 <= Node.val <= 100
	Each node has a unique value.
	x != y
	x and y are exist in the tree.
"""
import sys
from typing import Optional
import pytest
sys.path.append('../exercise')
from tree import TreeNode, build_tree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find_depth_and_parent(root, val):
            if not root:
                return -1, None
            if root.val == val:
                return 0, None
            dl, pl = find_depth_and_parent(root.left, val)
            if dl >= 0:
                return dl+1, pl or root.val
            # Assume that val is always in the tree
            dr, pr = find_depth_and_parent(root.right, val)
            if dr >= 0:
                return dr+1, pr or root.val
            return -1, None

        dx, px = find_depth_and_parent(root, x)
        dy, py = find_depth_and_parent(root, y)
        return px != py and dx == dy


@pytest.mark.parametrize('nodes, x, y, expected', [
    ([1,2,3,4], 4, 3, False),
    ([1,2,3,None,4,None,5], 5, 4, True),
    ([1,2,3,None,4], 2, 3, False),
    ([1,None,2,3,None,None,4,None,5], 1, 3, False),
])
def test(nodes, x, y, expected):
    tree = build_tree(nodes)
    print()
    print(tree)
    assert expected == Solution().isCousins(tree, x, y)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


