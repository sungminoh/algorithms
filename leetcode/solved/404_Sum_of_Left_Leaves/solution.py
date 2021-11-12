#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the sum of all left leaves.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0

Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	-1000 <= Node.val <= 1000
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        return left + self.sumOfLeftLeaves(root.right)


@pytest.mark.parametrize('nodes, expected', [
    ([3,9,20,None,None,15,7], 24),
    ([1], 0),
])
def test(nodes, expected):
    assert expected == Solution().sumOfLeftLeaves(build_tree(nodes))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
