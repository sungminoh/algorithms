#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Constraints:

	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left
            while not p and stack:
                p = stack.pop()
                ret.append(p.val)
                p = p.right
        return ret

    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left)\
            + [root.val]\
            + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        return list(inorder(root))


@pytest.mark.parametrize('values, expected', [
    ([1,None,2,3], [1,3,2]),
    ([], []),
    ([1], [1]),
])
def test(values, expected):
    assert expected == Solution().inorderTraversal(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
