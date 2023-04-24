#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Apr 13, 2023 00:35"""
        ls = [root.left]
        rs = [root.right]
        while ls or rs:
            if ls and rs:
                l = ls.pop()
                r = rs.pop()
                if l and r:
                    if l.val != r.val:
                        return False
                    ls.append(l.left)
                    ls.append(l.right)
                    rs.append(r.right)
                    rs.append(r.left)
                    continue
                if not l and not r:
                    continue
                return False
        return not ls and not rs


@pytest.mark.parametrize('args', [
    (([1,2,2,3,4,4,3], True)),
    (([1,2,2,None,3,None,3], False)),
])
def test(args):
    assert args[-1] == Solution().isSymmetric(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
