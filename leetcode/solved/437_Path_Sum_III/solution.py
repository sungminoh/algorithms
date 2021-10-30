#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

	The number of nodes in the tree is in the range [0, 1000].
	-109 <= Node.val <= 109
	-1000 <= targetSum <= 1000
"""
import itertools
from typing import Optional
import sys
import pytest
sys.path.append('../exercise')
from tree import TreeNode, build_tree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """07/28/2020 00:27"""
        cnt = 0
        def rec(node, acc):
            nonlocal cnt
            if not node:
                return
            if 0 not in acc:
                acc[0] = 0
            acc[0] += 1
            cnt += acc.get(targetSum-node.val, 0)
            rec(node.left, {k+node.val: v for k, v in acc.items()})
            rec(node.right, {k+node.val: v for k, v in acc.items()})

        rec(root, {})
        return cnt

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """07/28/2020 00:34
        Time complexity: O(n)
        Space complexity: O(n)
        """
        cnt = 0
        memo = {0: 1}
        def dfs(node, acc):
            nonlocal cnt
            if not node:
                return
            acc += node.val
            cnt += memo.get(acc-targetSum, 0)
            if acc not in memo:
                memo[acc] = 0
            memo[acc] += 1
            dfs(node.left, acc)
            dfs(node.right, acc)
            memo[acc] -= 1

        dfs(root, 0)
        return cnt

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Time complexity: O(n*d)
        Space complexity: O(d)
        """
        stack = []

        def dfs(root):
            ret = 0
            if not root:
                return ret
            stack.append(root.val)
            acc = 0
            for x in reversed(stack):
                acc += x
                if acc == targetSum:
                    ret += 1
            ret += dfs(root.left)
            ret += dfs(root.right)
            stack.pop()
            return ret

        return dfs(root)


@pytest.mark.parametrize('nodes, targetSum, expected', [
    ([10,5,-3,3,2,None,11,3,-2,None,1], 8, 3),
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, 3),
    ([1], 1, 1),
    ([-2,None,-3], -5, 1),
])
def test(nodes, targetSum, expected):
    tree = build_tree(nodes)
    assert expected == Solution().pathSum(tree, targetSum)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
