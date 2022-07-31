#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
	-1000 <= Node.val <= 1000
"""
from collections import deque
from collections import defaultdict
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
    def levelOrder(self, root):
        """05/06/2018 22:20"""
        memo = defaultdict(list)
        def tree2list(r, d=0):
            if d == 0:
                memo.clear()
            if not r:
                return
            memo[d].append(r.val)
            tree2list(r.left, d+1)
            tree2list(r.right, d+1)

        tree2list(root)
        return [v for k, v in sorted(memo.items(), key=lambda x: x[0])]

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """06/01/2021 14:48"""
        if not root:
            return []
        queue = deque([(0, root)])
        ret = []
        level = []
        cur = 0
        while queue:
            l, n = queue.popleft()
            if l != cur:
                ret.append(level)
                level = []
                cur = l
            level.append(n.val)
            if n.left:
                queue.append((l+1, n.left))
            if n.right:
                queue.append((l+1, n.right))
        ret.append(level)
        return ret

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """07/30/2022 18:30"""
        ret = []
        buf = []
        if root:
            buf.append(root)
        while buf:
            layer = []
            _buf = []
            for n in buf:
                layer.append(n.val)
                if n.left:
                    _buf.append(n.left)
                if n.right:
                    _buf.append(n.right)
            ret.append(layer)
            buf = _buf
        return ret


@pytest.mark.parametrize('values, expected', [
    ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
    ([1], [[1]]),
    ([], []),
])
def test(values, expected):
    assert expected == Solution().levelOrder(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
