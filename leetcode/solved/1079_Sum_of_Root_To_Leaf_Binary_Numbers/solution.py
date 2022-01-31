#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

	For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Example 1:

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:

Input: root = [0]
Output: 0

Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	Node.val is 0 or 1.
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.tree import build_tree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traverse(node, n):
            if not node:
                return 0
            n = (n<<1) + node.val
            if not node.left and not node.right:
                return n
            return traverse(node.left, n) + traverse(node.right, n)

        return traverse(root, 0)


@pytest.mark.parametrize('values, expected', [
    ([1,0,1,0,1,0,1], 22),
    ([0], 0),
])
def test(values, expected):
    tree = build_tree(values)
    assert expected == Solution().sumRootToLeaf(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
