#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:

	The number of nodes in the tree is in the range [1, 100].
	1 <= Node.val <= 1000
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        """May 30, 2020 18:23"""
        min_height = float('inf')
        updated = False
        def traverse(n, height=0):
            nonlocal min_height, updated
            # print(n, height, min_height, updated)
            if n == None:
                if height < min_height:
                    if updated:
                        return False
                    else:
                        if min_height < float('inf'):
                            updated = True
                        min_height = height
                elif height > min_height:
                    return False
                return True
            else:
                left = traverse(n.left, height + 1)
                if not left:
                    return False
                right = traverse(n.right, height + 1)
                if not right:
                    return False
                return True

        return traverse(root, 0)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """Apr 23, 2023 17:45"""
        if not root:
            return True
        queue = [root]
        stopped = False
        while queue:
            _queue = []
            should_be_last_parent = False
            for i, n in enumerate(queue):
                if n.left:
                    if stopped:
                        return False
                    _queue.append(n.left)
                else:
                    stopped = True
                if n.right:
                    if stopped:
                        return False
                    _queue.append(n.right)
                else:
                    stopped = True
            queue = _queue
        return True


@pytest.mark.parametrize('args', [
    (([1,2,3,4,5,6], True)),
    (([1,2,3,4,5,None,7], False)),
    ([1,None,2], False),
])
def test(args):
    assert args[-1] == Solution().isCompleteTree(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
