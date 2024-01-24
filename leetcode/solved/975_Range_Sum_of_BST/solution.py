#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:

	The number of nodes in the tree is in the range [1, 2 * 104].
	1 <= Node.val <= 105
	1 <= low <= high <= 105
	All Node.val are unique.
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Dec 23, 2021 13:06"""
        def dfs(node):
            if not node:
                return 0

            ret = 0
            if low <= node.val <= high:
                ret += node.val

            if node.val < low:
                ret += dfs(node.right)
            elif node.val > high:
                ret += dfs(node.left)
            else:
                ret += dfs(node.left) + dfs(node.right)

            return ret

        return dfs(root)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Dec 11, 2022 16:13"""
        def summation(node):
            if not node:
                return 0
            if node.val < low:
                return summation(node.right)
            if node.val > high:
                return summation(node.left)
            return summation(node.left) + summation(node.right) + node.val

        return summation(root)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Feb 18, 2023 19:27"""
        ret = 0
        stack = [root]
        while stack:
            n = stack.pop()
            if not n:
                continue
            if low <= n.val <= high:
                ret += n.val
            stack.append(n.left)
            stack.append(n.right)
        return ret

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Jan 22, 2024 22:02"""
        if root is None:
            return 0
        return self.rangeSumBST(root.left, low, high) \
            + self.rangeSumBST(root.right, low, high) \
            + (root.val if low <= root.val <= high else 0)


@pytest.mark.parametrize('args', [
    (([10,5,15,3,7,None,18], 7, 15, 32)),
    (([10,5,15,3,7,13,18,1,None,6], 6, 10, 23)),
])
def test(args):
    assert args[-1] == Solution().rangeSumBST(build_tree(args[0]), args[1], args[2])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
