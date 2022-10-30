#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-104 <= Node.val <= 104
	root is guaranteed to be a valid binary search tree.
	-105 <= k <= 105
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """09/03/2021 23:20"""
        visited = set()
        def dfs(node):
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """10/29/2022 14:12"""
        s = set()
        def traverse(node):
            if not node:
                return False
            if k - node.val in s:
                return True
            s.add(node.val)
            return traverse(node.left) or traverse(node.right)

        return traverse(root)


@pytest.mark.parametrize('values, k, expected', [
    ([5,3,6,2,4,None,7], 9, True),
    ([5,3,6,2,4,None,7], 28, False),
    ([2,1,3], 4, True),
    ([2,1,3], 1, False),
    ([2,1,3], 3, True),
])
def test(values, k, expected):
    assert expected == Solution().findTarget(build_tree(values), k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
