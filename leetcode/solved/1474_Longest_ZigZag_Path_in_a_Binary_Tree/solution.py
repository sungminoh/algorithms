from typing import Tuple
from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

	Choose any node in the binary tree and a direction (right or left).
	If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
	Change the direction from right to left or from left to right.
	Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:

Input: root = [1]
Output: 0

Constraints:

	The number of nodes in the tree is in the range [1, 5 * 104].
	1 <= Node.val <= 100
"""
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """Sep 03, 2023 21:16"""
        ret = 0

        def dfs(node) -> Tuple[int, int]:
            if not node:
                return 0, 0

            ll, lr = dfs(node.left)
            rl, rr = dfs(node.right)
            l, r = lr + 1, rl + 1
            nonlocal ret
            ret = max(ret, l-1, r-1)
            return l, r

        dfs(root)

        return ret


@pytest.mark.parametrize('args', [
    (([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1], 3)),
    (([1,1,1,None,1,None,None,1,1,None,1], 4)),
    (([1], 0)),
])
def test(args):
    assert args[-1] == Solution().longestZigZag(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
