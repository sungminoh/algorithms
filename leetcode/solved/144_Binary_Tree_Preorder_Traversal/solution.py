#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

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
    def preorderTraversal(self, root):
        """Jul 26, 2018 06:43"""
        if not root:
            return []
        ret = []
        stack = []
        cur = root
        while cur:
            ret.append(cur.val)
            stack.append(cur)
            cur = cur.left
            while not cur and stack:
                cur = stack.pop().right
        return ret

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Mar 05, 2023 14:14"""
        def traverse(n):
            if not n:
                return
            yield n.val
            yield from traverse(n.left)
            yield from traverse(n.right)
        return list(traverse(root))


@pytest.mark.parametrize('args', [
    (([1,None,2,3], [1,2,3])),
    (([], [])),
    (([1], [1])),
])
def test(args):
    assert args[-1] == Solution().preorderTraversal(build_tree(args[0]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
