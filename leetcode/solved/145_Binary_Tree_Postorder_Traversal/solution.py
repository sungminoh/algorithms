#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

Constraints:

	The number of the nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from optparse import Option
from typing import List, Optional
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        stack = []
        visited = []
        done = set()
        while root:
            stack.append(root)
            visited.append(False)
            if root not in done:
                root = root.left
            else:
                root = None
            while not root and stack:
                if not visited[-1]:
                    root = stack[-1].right
                    visited[-1] = True
                else:
                    while visited and visited[-1]:
                        root = stack.pop()
                        ret.append(root.val)
                        visited.pop()
                        done.add(root)
                    root = None
        return ret

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Dec 05, 2024 12:42"""
        def rec(node):
            if not node:
                return
            yield from rec(node.left)
            yield from rec(node.right)
            yield node.val

        return list(rec(root))


@pytest.mark.parametrize('args', [
    (([1,None,2,3], [3,2,1])),
    (([1,2,3,4,5,None,8,None,None,6,7,9], [4,6,7,5,2,9,8,3,1])),
    (([], [])),
    (([1], [1])),
])
def test(args):
    assert args[-1] == Solution().postorderTraversal(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
