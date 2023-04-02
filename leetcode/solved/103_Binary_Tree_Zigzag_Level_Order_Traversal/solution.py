#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
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
    def zigzagLevelOrder(self, root):
        """May 06, 2018 06:44
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        q = [[root], []]
        i = 0
        while q[0] or q[1]:
            level = []
            j = (i+1)%2
            while q[i]:
                n = q[i].pop(0)
                level.append(n.val)
                if n.left:
                    q[j].append(n.left)
                if n.right:
                    q[j].append(n.right)
            if i % 2 == 0:
                ret.append(level)
            else:
                ret.append(list(reversed(level)))
            i = j
        return ret

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Mar 22, 2023 00:13"""
        if not root:
            return []
        ret = []
        l = [root]
        while l:
            layer = []
            _l = []
            for n in reversed(l):
                layer.append(n.val)
                if len(ret)%2:
                    if n.right:
                        _l.append(n.right)
                    if n.left:
                        _l.append(n.left)
                else:
                    if n.left:
                        _l.append(n.left)
                    if n.right:
                        _l.append(n.right)
            ret.append(layer)
            l = _l
        return ret


@pytest.mark.parametrize('args', [
    (([3,9,20,None,None,15,7], [[3],[20,9],[15,7]])),
    (([1], [[1]])),
    (([], [])),
    (([1,2,3,4,None,None,5] , [[1],[3,2],[4,5]])),
])
def test(args):
    assert args[-1] == Solution().zigzagLevelOrder(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
