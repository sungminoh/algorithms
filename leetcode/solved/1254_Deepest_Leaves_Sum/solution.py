#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	1 <= Node.val <= 100
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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """04/29/2021 09:49
        BFS and keep only the deepest sum
        """
        if not root:
            return 0

        ret = 0
        depth = 0
        queue = deque([(1, root)])
        while queue:
            d, n = queue.popleft()
            if d > depth:
                depth = d
                ret = 0
            if d == depth:
                ret += n.val
            if n.left:
                queue.append((d+1, n.left))
            if n.right:
                queue.append((d+1, n.right))
        return ret

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """06/02/2022 15:28
        Recursion
        """
        def rec(node: TreeNode):
            """return depth and sum of leaves at that depth"""
            if not node:
                return 0, 0
            ld, ls = rec(node.left)
            rd, rs = rec(node.right)
            if ld > rd:
                return ld+1, ls
            if ld < rd:
                return rd+1, rs
            if ld == 0:
                return 1, node.val
            return ld+1, ls+rs

        return rec(root)[1]


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5,None,6,7,None,None,None,None,8], 15),
    ([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5], 19),
])
def test(values, expected):
    assert expected == Solution().deepestLeavesSum(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
