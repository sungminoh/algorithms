#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100
"""
from typing import List
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
    def rightSideView(self, root):
        """12/21/2018 18:06"""
        def look_at_nth_from_right(tree, depth):
            if not tree:
                return
            if len(right_side) <= depth:
                right_side.append(tree.val)
            look_at_nth_from_right(tree.right, depth + 1)
            look_at_nth_from_right(tree.left, depth + 1)

        right_side = []
        look_at_nth_from_right(root, 0)
        return right_side

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(ret):
                ret.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return ret


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,None,5,None,4], [1,3,4]),
    ([1,None,3], [1,3]),
    ([], []),
])
def test(values, expected):
    assert expected == Solution().rightSideView(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
