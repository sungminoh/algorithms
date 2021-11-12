#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

	For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:

	The number of nodes in the tree is in the range [1, 1000].
	0 <= Node.val <= 9
	The depth of the tree will not exceed 10.
"""
import sys
from typing import Optional
import pytest
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root):
        """05/12/2018 04:56"""
        def sum_numbers(root):
            if not root.left and not root.right:
                return [(root.val, 1)]
            ret = []
            if root.left:
                left = sum_numbers(root.left)
                ret.extend([(root.val * (10 ** ll) + ls, ll + 1) for ls, ll in left])
            if root.right:
                right = sum_numbers(root.right)
                ret.extend([(root.val * (10 ** rl) + rs, rl + 1) for rs, rl in right])
            return ret

        if not root:
            return 0
        return sum(x[0] for x in sum_numbers(root))

    def sumNumbers(self, root):
        """05/12/2018 05:02"""
        def dfs(root, val):
            if not root:
                return 0
            val = val*10 + root.val
            if not root.left and not root.right:
                return val
            return dfs(root.left, val) + dfs(root.right, val)

        return self.dfs(root, 0)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, acc):
            if not node:
                return acc
            if not node.left and not node.right:
                return 10*acc + node.val
            ret = 0
            if node.left:
                ret += dfs(node.left, 10*acc + node.val)
            if node.right:
                ret += dfs(node.right, 10*acc + node.val)
            return ret

        return dfs(root, 0)


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3], 25),
    ([4,9,0,5,1], 1026),
])
def test(nodes, expected):
    assert expected == Solution().sumNumbers(build_tree(nodes))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
