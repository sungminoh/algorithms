from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

	The node is currently uninfected.
	The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

Example 1:

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:

Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.

Constraints:

	The number of nodes in the tree is in the range [1, 105].
	1 <= Node.val <= 105
	Each node has a unique value.
	A node with a value of start exists in the tree.
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """Jan 22, 2024 23:41"""
        ret = 0
        def dfs(node, depth=0):
            """dist_to_bottom, depth_to_target, answer"""
            if not node:
                return 0, -1, -1

            lbottom, lfound, lanswer = dfs(node.left, depth+1)
            rbottom, rfound, ranswer = dfs(node.right, depth+1)
            bottom = max(lbottom, rbottom)+1
            if node.val == start:
                return bottom, 1, max(lbottom, rbottom, depth)

            if lfound >= 0:
                return bottom, lfound+1, max(lanswer, lfound+rbottom)
            elif rfound >= 0:
                return bottom, rfound+1, max(ranswer, rfound+lbottom)
            return bottom, -1, -1

        return dfs(root, 0)[-1]


@pytest.mark.parametrize('args', [
    (([1,5,3,None,4,10,6,9,2], 3, 4)),
    (([1], 1, 0)),
    (([1,2,None,3,None,4,None,5], 3, 2)),
])
def test(args):
    assert args[-1] == Solution().amountOfTime(build_tree(args[0]), *args[1:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
