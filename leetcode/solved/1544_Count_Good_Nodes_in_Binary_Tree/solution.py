#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

	The number of nodes in the binary tree is in the range [1, 10^5].
	Each node's value is between [-10^4, 10^4].
"""
from pathlib import Path
import pytest
import sys
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:
                return 0
            m = max(node.val, m)
            return (1 if node.val >= m else 0) + dfs(node.left, m) + dfs(node.right, m)

        return dfs(root, -float('inf'))


@pytest.mark.parametrize('nodes, expected', [
    ([3,1,4,3,None,1,5], 4),
    ([3,3,None,4,2], 3),
    ([1], 1),
])
def test(nodes, expected):
    assert expected == Solution().goodNodes(build_tree(nodes))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
