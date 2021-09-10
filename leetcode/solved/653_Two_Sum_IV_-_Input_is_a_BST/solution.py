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

Example 3:

Input: root = [2,1,3], k = 4
Output: true

Example 4:

Input: root = [2,1,3], k = 1
Output: false

Example 5:

Input: root = [2,1,3], k = 3
Output: true

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-104 <= Node.val <= 104
	root is guaranteed to be a valid binary search tree.
	-105 <= k <= 105
"""
from pathlib import Path
import sys
from typing import Optional
import pytest
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))
from exercise.tree import TreeNode, build_tree


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        def dfs(node):
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


@pytest.mark.parametrize('nodes, k, expected', [
    ([5,3,6,2,4,None,7], 9, True),
    ([5,3,6,2,4,None,7], 28, False),
    ([2,1,3], 4, True),
    ([2,1,3], 1, False),
    ([2,1,3], 3, True),
])
def test(nodes, k, expected):
    assert expected == Solution().findTarget(build_tree(nodes), k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
