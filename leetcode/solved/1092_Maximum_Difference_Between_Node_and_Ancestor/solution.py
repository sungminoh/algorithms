#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:

Input: root = [1,null,2,null,0,3]
Output: 3

Constraints:

	The number of nodes in the tree is in the range [2, 5000].
	0 <= Node.val <= 105
"""
from typing import Tuple
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.tree import build_tree, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def minmax(node: TreeNode) -> Tuple:
            nonlocal ret
            vals = []
            if node.left:
                vals.extend(minmax(node.left))
            if node.right:
                vals.extend(minmax(node.right))
            if vals:
                ret = max(ret, abs(node.val-min(vals)), abs(node.val-max(vals)))
            vals.append(node.val)
            return min(vals), max(vals)

        minmax(root)
        return ret


@pytest.mark.parametrize('values, expected', [
    ([8,3,10,1,6,None,14,None,None,4,7,13], 7),
    ([1,None,2,None,0,3], 3),
])
def test(values, expected):
    root = build_tree(values)
    assert expected == Solution().maxAncestorDiff(root)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
