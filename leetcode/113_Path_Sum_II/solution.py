#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 5000].
	-1000 <= Node.val <= 1000
	-1000 <= targetSum <= 1000
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
    def pathSum(self, root, sum):
        """05/06/2018 21:21"""
        if root is None:
            return []
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        return [[root.val, *x]
                for x in self.pathSum(root.left, sum - root.val)\
                + self.pathSum(root.right, sum - root.val)]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """08/22/2021 22:30"""
        def dfs(node, backtrack, summation):
            if node is None:
                return []
            if node.left is None and node.right is None:
                if summation + node.val == targetSum:
                    return [backtrack + [node.val]]
                return []
            backtrack.append(node.val)
            left = dfs(node.left, backtrack, summation + node.val)
            right = dfs(node.right, backtrack, summation + node.val)
            backtrack.pop()
            return left + right

        return dfs(root, [], 0)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """10/22/2022 00:27"""
        def dfs(node, target):
            if node is None:
                return []
            if node.left is None and node.right is None:
                if node.val == target:
                    return [[node.val]]
            ret = [[node.val] + path for path in dfs(node.left, target - node.val)]
            ret.extend([[node.val] + path for path in dfs(node.right, target - node.val)])
            return ret

        return dfs(root, targetSum)


@pytest.mark.parametrize('values, targetSum, expected', [
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, [[5,4,11,2],[5,8,4,5]]),
    ([1,2,3], 5, []),
    ([1,2], 0, []),
])
def test(values, targetSum, expected):
    assert expected == Solution().pathSum(build_tree(values), targetSum)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
