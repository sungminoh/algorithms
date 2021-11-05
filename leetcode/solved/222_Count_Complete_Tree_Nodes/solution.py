#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [0, 5 * 104].
	0 <= Node.val <= 5 * 104
	The tree is guaranteed to be complete.
"""
import sys
from typing import Optional
import pytest
sys.path.append('../')
from exercise.tree import TreeNode, build_tree, print_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """05/12/2019 22:01"""
        if not root:
            return 0

        def find_diff(node: TreeNode, d: int):
            if node.left and node.right:
                in_right, rd = find_diff(node.right, d + 1)
                if in_right:
                    return in_right, rd
                in_left, ld = find_diff(node.left, d + 1)
                if in_left:
                    return in_left + 2 ** (rd - d), ld
                if ld != rd:
                    return 2 ** (rd - d), ld
                return 0, ld
            elif not node.left and not node.right:
                return 0, d
            else:
                return 1, d + 1
        missing, depth = find_diff(root, 1)
        return 2 ** depth - 1 - missing

    def countNodes(self, root: TreeNode) -> int:
        """05/12/2019 22:09"""
        def height(root):
            return 0 if not root else (1 + height(root.left))

        cnt = 0
        h = height(root)
        while root:
            if height(root.right) == h - 1:
                cnt += 2 ** (h - 1)
                root = root.right
            else:
                cnt += 2 ** (h - 2)
                root = root.left
            h -= 1
        return cnt

    def countNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def dfs(node):
            if not node:
                return True, 0
            nonlocal cnt
            cnt += 1
            is_right_full, right_depth = dfs(node.right)
            if not is_right_full:
                cnt += 2**(right_depth) - 1  # for left
                return False, right_depth+1
            else:
                is_left_full, left_depth = dfs(node.left)
                if is_left_full:
                    if left_depth != right_depth:
                        return False, left_depth+1
                    else:
                        return True, left_depth+1
                else:
                    return False, left_depth+1

        dfs(root)
        return cnt


def build_complete_tree(nodes):
    if not nodes:
        return None
    nodes = [TreeNode(x) for x in nodes]
    for i, n in enumerate(nodes):
        l = 2*i+1
        if l < len(nodes):
            n.left = nodes[l]
        r = 2*i+2
        if r < len(nodes):
            n.right = nodes[r]
    return nodes[0]


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,5,6], 6),
    ([], 0),
    ([1], 1),
])
def test(nodes, expected):
    tree = build_complete_tree(nodes)
    assert expected == Solution().countNodes(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
