#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	Node.val == 0
"""
from pathlib import Path
from typing import Tuple
import pytest
import sys
sys.path.append(str(Path('__file__').absolute().parent.parent.parent))
from exercise.tree import TreeNode, build_tree


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        Top down
        Time complexity: O(3*n)
        Space complexity: O(3*n)
        """
        memo = {}
        def rec(node: TreeNode, parent_covered: bool, covered: bool) -> int:
            key = (id(node), parent_covered, covered)
            if key in memo:
                return memo[key]
            if not node:
                return 0
            if not node.left and not node.right and not covered:
                return 1
            ret = 1 + rec(node.left, True, True) + rec(node.right, True, True)
            if parent_covered:
                if covered:
                    ret = min(ret, rec(node.left, True, False) + rec(node.right, True, False))
                else:
                    if node.right:
                        ret = min(ret, rec(node.left, True, False) + rec(node.right, False, False))
                    if node.left:
                        ret = min(ret, rec(node.left, False, False) + rec(node.right, True, False))
            memo[key] = ret
            return ret
        return rec(root, True, False)

    def minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy bottom up
        Time complexity: O(n)
        Space complexity: O(logn)  (call stack)
        """
        cnt = 0
        def rec(node: TreeNode) -> Tuple[int, int]:
            """
            0: camera, 1: covered, 2: not covered
            """
            nonlocal cnt
            if not node:
                return 1
            l = rec(node.left)
            r = rec(node.right)
            if l == 2 or r == 2:
                cnt += 1
                return 0
            if l*r == 0:
                return 1
            return 2
        if rec(root) == 2:
            cnt += 1
        return cnt


@pytest.mark.parametrize('nodes, expected', [
    ([0,0,None,0,0], 1),
    ([0,0,None,0,None,None,0], 2),
    ([0,0,None,0,None,0,None,None,0], 2),
    ([0,0,0,None,None,None,0], 2),
    ([1,2,3,None,None,None,4], 2),
    ([0,0,0,0,0,0,0,0,0,0,None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,None,0,0,0,None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,None,None,0,0,0,0,0,0,0,0,None,None,0,None,0,0,0,0,0,0,0,0,0,0,0,0,None,None,0,None,0,0,None,0,None,0,0,0,0,0,None,None,None,None,0,0,0,0,None,None,0,0,0,0,0,0,None,None,None,None,0,None,None,0,None,None,None,None,0,0,0,0,0,None,0,0,None,None,0,0,0,0,0,None,0,None,0,0,0,0,0,0,None,None,0,0,0,0,0,None,None,0,0,None,0,None,0,None,0,0,0,None,0,0,None,0,0,None,0,0,0,0,0,0,0,0,0,0,None,0,0,0,None,0,0,0,0,0,None,0,0,0,None,None,0,0,0,0,0,0,None,0,0,None,None,0,None,0,0,None,0,0,None,0,0,0,0,0,None,0,None,0,None,None,None,0,0,0,0,0,0,None,None,None,0,0,0,0,0,None,None,None,0,None,None,0,None,None,None,None,0,None,0,None,0,0,0,None,None,0,None,None,None,0,0,0,None,None,0,0,0,0,None,None,0,0,None,0,0,0,None,0,0,None,0,None,0,0,0,0,None,0,0,0,0,0,0,0,None,0,None,None,None,0,0,0,0,0,None,0,0,0,0,0,0,0,0,0,None,None,None,None,0,None,None,None,None,0,0,None,None,0,None,0,0,0,0,0,None,0,0,0,0,None,0,None,None,None,None,None,None,None,0,0,0,0,None,0,0,None,0,0,0,0,0,0,0,None,0,None,None,0,None,None,None,None,None,None,0,0,None,None,0,None,None,None,None,None,0,None,0,0,0,None,0,0,0,0,0,0,0,0,None,0,0,0,0,0,None,None,None,0,0,None,0,0,None,0,None,None,0,0,None,None,None,0,0,None,None,None,None,0,0,0,0,0,None,0,0,None,0,0,0,None,0,0,0,0,None,0,None,0,0,0,0,0,None,None,None,0,0,0,0,0,0,0,None,None,None,None,0,None,0,None,None,None,0,0,0,None,0,None,None,None,0,None,0,0,None,None,None,0,None,None,0,None,None,0,0,0,None,0,None,None,None,None,0,0,0,0,0,0,0,0,0,0,None,0,0,0,0,None,0,None,None,0,None,None,0,0,None,None,0,0,None,0,0,0,0,0,0,0,0,0,0,0,None,0,0,0,0,0,0,0,0,None,0,0,0,0,0,0,0,None,None,0,None,None,0,None,0,None,0,None,0,0,0,0,0,None,None,None,None,None,None,0,0,None,0,0,None,0,0,0,0,None,None,None,None,None,0,None,None,0,None,0,None,None,None,0,None,None,None,None,0,0,0,0,None,None,0,None,None,None,0,0,0,None,0,0,0,0,0,0,None,0,None,None,0,0,None,None,None,None,0,None,None,None,None,None,None,None,None,0,None,None,None,None,0,None,0,None,0,None,0,0,None,0,None,None,0,None,0,None,0,None,None,0,0,None,0,None,0,0,0,0,0,0,None,0,0,0,0,None,None,None,None,None,0,0,0,0,0,0,None,0,0,0,None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,None,0,0,0,0,0,None,0,None,0,0,0,0,0,0,None,0,0,0,None,None,None,None,None,None,None,None,0,None,0,None,0,None,None,None,0,None,None,None,0,0,None,None,None,0,0,0,0,0,0,None,None,None,None,None,0,0,None,0,0,None,None,None,None,None,None,0,None,0,None,None,None,0,0,0,None,0,0,None,0,0,None,None,None,None,None,None,0,0,0,0,0,None,None,0,None,None,0,0,0,0,0,0,0,None,None,None,0,0,None,None,None,None,None,None,None,None,None,None,0,None,None,None,None,0,None,None,None,None,None,None,None,0,None,None,0,None,0,0,None,None,0,None,None,None,0,None,None,None,None,None,None,None,None,None,None,None,None,0,None,None,None,None,0,0,None,0,0,0,None,None,None,None,0,0,None,None,None,None,0,0,0,0,None,None,0,0,None,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,None,None,None,None,None,0,0,None,None,None,None,None,None,None,None,None,None,None,None,None,0,0,0,0,None,None,0,None,None,None,None,None,0,None,None,None,None,None,None,0,0,None,0,None,0,0,0,0,None,None,None,None,None,None,0,0,0,0,0,0,0,0,0,None,None,None,None,0,0,None,None,None,None,0,0,None,None,0,None,0,None,0,None,None,0,None,None,None,None,0,None,0,None,None,None,None,0,0,None,0,0,0,None,0,0,0,None,0,None,None,None,None,0,None,None,None,None,None,None,None,None,0,0,0,0,None,0,None,0,None,0,None,0,0,0,0,0,None,0,0,0,None,None,None,None,0,0,0,0,None,0,0,None,None,0,None,None,0,None,0,0,None,0,0,0,None,0,0,None,None,None,0,0,None,None,None,None,None,0,0,0,None,0,0,0,0,0,0,0,0,None,None,0,0,None,0,None,None,None,0,0,None,None,None,0,0,None,0,None,None,0,None,None,0,0,None,None,None,0,0,None,None,0,None,0,None,0,0,None,None,None,0,0,None,None,None,None,0,0,None,0,None,None,None,None,0,0,0,0,0,0,None,None,None,0,0,None,0,None,None,None,None,0,None,0,None,None,0,0,None,None,0,0,0,0,None,0,None,None,None,None,None,None,None,None,None,0,0,0,None,0,None,None,0,0,None,0,0,0,None,0,None,None,None,0,None,0,None,None,0,None,0,0,0,0,0,0,0,0,0,None,None,0,0,0,None,None,None,None,None,0,0,None,None,None,None,0,0,0,0,0,None,0,0,0,None,None,None,None,None,0,None,None,0,0,0,0,0,None,None,0,0,0,0,None,None,None,0,0,None,None,0,None,None,0,0,0,None,0,None,0,None,0,None,None,0,0,None,None,None,None,None,None,None,None,None,None,None,None,0,None,None,0,0,None,None,None,None,None,0,None,0,0,0,0,None,0,0,0,None,None,0,None,None,0,None,None,0,None,None,None,None,None,None,0,0,0,0,0,0,0,None,None,None,None,None,None,0,0,None,0,None,0,None,None,None,None,None,0,None,None,None,None,None,0,0,0,0,None,None,None,None,None,None,None,None,0,0,0,0,0,None,0,0,None,0,0,0,0,0,0,0,None,0,0,0,None,None,0,None,None,None,None,None,None,None,None,0,None,None,None,0,None,0,None,0,0,None,None,0,0,None,0,0,0,None,0,0,0,None,0,None,None,None,None,0,None,0,None,0,None,None,None,None,None,None,0,0,0,None,None,0,None,None,None,0,0,None,None,None,None,0,None,0,None,None,None,0,None,0,0,0,0,0,0,None,0,0,None,None,None,0,None,0,None,None,0,None,None,None,None,None,None,None,None,None,None,0,None,0,0,None,None,None,None,0,None,0,None,None,None,None,0,0,None,None,0,None,None,0,0,0,0,None,0,None,None,0,None,None,None,0,None,0,0,0,None,0,0,0,0,0,None,None,None,None,None,0,None,0,None,0,None,None,0,None,None,None,None,None,None,None,None,None,0,None,0,0,0,None,None,None,None,0,None,None,None,0,None,None,None,None,0,None,None,None,None,None,None,None,None,0,None,0,None,None,None,0,None,None,None,None,None,0,None,0,0,0,0,None,None,None,0,0,0,None,0,0,0,None,0,None,None,None,None,None,None,None,None,None,None,None,None,0,0,0,None,None,None,None,None,None,None,0,0,0,0,0,0,None,None,None,0,0,None,None,None,0,0,None,0,0,0,0,None,None,None,0,None,None,None,None,None,None,None,None,None,0,None,None,None,None,None,None,None,0,0,0,0,0,None,0,0,None,None,None,0,0,0,0,0,None,None,None,None,None,0,0,0,None,0,None,None,None,None,0,0,0,None,None,None,0,None,None,0,0,None,None,0,0,None,None,None,None,None,None,None,0,None,0,None,None,None,None,0,0,None,None,0,0,0,0,0,None,None,0,None,None,0,0,0,0,0,0,None,None,None,0,None,None,None,0,0,None,None,None,None,None,None,None,None,None,None,0,0,None,0,None,None,0,None,0,None,None,None,None,None,None,None,0,None,None,None,None,None,None,None,0,None,0,None,None,0,None,None,0,0,None,None,None,0,None,None,0,0,None,None,0,0,0,0,0,0,0,0,None,None,0,0,None,None,None,None,None,None,None,None,0,0,0,None,None,None,None,0,None,0,None,0,None,None,None,None,0,0,None,None,None,None,None,0,0,0,None,0,None,None,None,0,None,None,0,0,None,None,None,None,0,None,None,None,None,None,0,0,None,None,None,None,None,None,0,0,None,None,None,0,None,None,None,None,None,None,None,None,None,None,0,None,None,None,None,None,0,0,None,None,None,None,None,None,0,0,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0], 360)
])
def test(nodes, expected):
    root = build_tree(nodes)
    print()
    print(root)
    actual = Solution().minCameraCover(root)
    print(actual)
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
