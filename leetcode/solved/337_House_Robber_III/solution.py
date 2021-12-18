#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	0 <= Node.val <= 104
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
    def rob(self, root: TreeNode) -> int:
        def max_in_ex_node(node: TreeNode) -> int:
            if not node:
                return 0, 0
            left_in, left_ex = max_in_ex_node(node.left)
            right_in, right_ex = max_in_ex_node(node.right)
            node_in = node.val + left_ex + right_ex
            node_ex = max(left_in, left_ex) + max(right_in, right_ex)
            return node_in, node_ex

        return max(max_in_ex_node(root))

    def rob(self, root: Optional[TreeNode]) -> int:
        """12/16/2021 23:15"""
        memo = {}

        def rec(node, is_parent_used):
            if node is None:
                return 0
            key = (id(node), is_parent_used)
            if key not in memo:
                if is_parent_used:
                    memo[key] = rec(node.left, False) + rec(node.right, False)
                else:
                    memo[key] = max(
                        node.val + rec(node.left, True) + rec(node.right, True),
                        rec(node.left, False) + rec(node.right, False))
            return memo[key]

        return rec(root, False)


@pytest.mark.parametrize('nodes, expected', [
    ([3,2,3,None,3,None,1], 7),
    ([3,4,5,1,3,None,1], 9),
])
def test(nodes, expected):
    assert expected == Solution().rob(build_tree(nodes))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
