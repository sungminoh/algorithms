#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.

Example 1:

Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:

Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Constraints:

	The number of nodes in the original tree is in the range [1, 1000].
	1 <= Node.val <= 109
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """May 04, 2024 12:08"""
        def parse(i):
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            ret = ''
            while i < len(traversal) and traversal[i] != '-':
                ret += traversal[i]
                i += 1
            return i, depth, int(ret)

        stack = []
        i = 0
        while i < len(traversal):
            i, d, v = parse(i)
            while stack and stack[-1][0] >= d:
                stack.pop()
            n = TreeNode(v)
            if stack and stack[-1][0] == d-1:
                p = stack[-1][1]
                if p.left is None:
                    p.left = n
                elif p.right is None:
                    p.right = n
            stack.append((d, n))

        return stack[0][1] if stack else None


@pytest.mark.parametrize('args', [
    (("1-2--3--4-5--6--7", [1,2,5,3,4,6,7])),
    (("1-2--3---4-5--6---7", [1,2,5,3,None,6,None,4,None,7])),
    (("1-401--349---90--88", [1,401,None,349,88,90])),
])
def test(args):
    assert build_tree(args[-1]) == Solution().recoverFromPreorder(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
