#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [2, 100].
	0 <= Node.val <= 105

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """Mar 20, 2023 23:38"""
        def inorder(node):
            if not node:
                return float('inf'), -float('inf'), float('inf')
            lmn, lmx, ld = inorder(node.left)
            rmn, rmx, rd = inorder(node.right)
            return min(lmn, node.val), max(node.val, rmx), min(ld, rd, node.val-lmx, rmn-node.val)

        return inorder(root)[-1]


@pytest.mark.parametrize('args', [
    (([4,2,6,1,3], 1)),
    (([1,0,48,None,None,12,49], 1)),
    (([27,None,34,None,58,50,None,44], 6)),
])
def test(args):
    assert args[-1] == Solution().minDiffInBST(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
