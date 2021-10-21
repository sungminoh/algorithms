#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-100 <= Node.val <= 100
"""
from heapq import heappop
from heapq import heappush
from typing import Optional
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0

        def dfs(node):
            nonlocal m
            if not node:
                return 0
            if not node.left and not node.right:
                m = max(m, 1)
                return 1
            elif not node.left:
                depth = 1+dfs(node.right)
                m = max(m, depth)
                return depth
            elif not node.right:
                depth = 1+dfs(node.left)
                m = max(m, depth)
                return depth
            else:
                left = 1+dfs(node.left)
                right = 1+dfs(node.right)
                m = max(m, left+right-1)
                return max(left, right)

        dfs(root)
        return m-1


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,5], 3),
    ([1,2], 1),
    ([4,2,None,1,3], 2),
])
def test(nodes, expected):
    tree = build_tree(nodes)
    print()
    print(tree)
    assert expected == Solution().diameterOfBinaryTree(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
