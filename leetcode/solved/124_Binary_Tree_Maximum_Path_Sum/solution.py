#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:

	The number of nodes in the tree is in the range [1, 3 * 104].
	-1000 <= Node.val <= 1000
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
    def maxPathSum(self, root):
        """Aug 16, 2018 06:35"""
        def mps(root):
            if not root:
                return -float('inf'), -float('inf')
            ll, l = mps(root.left)
            rr, r = mps(root.right)
            connected = root.val + max(0, l, r)
            unconnected = max(ll, rr, l, r, l + r + root.val)
            return unconnected, connected

        return max(mps(root))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Feb 19, 2023 15:03"""
        m = -float('inf')
        def max_path_from(node):
            if not node:
                return 0
            lp = max_path_from(node.left)
            rp = max_path_from(node.right)
            ret = max(node.val, node.val+lp, node.val+rp)
            nonlocal m
            m = max(m, ret, node.val+lp+rp)
            return ret
        max_path_from(root)
        return m


@pytest.mark.parametrize('values, expected', [
    ([1,2,3], 6),
    ([-10,9,20,None,None,15,7], 42),
    ([-3], -3),
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 48),
])
def test(values, expected):
    assert expected == Solution().maxPathSum(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
