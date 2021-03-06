#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]




Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
import sys
sys.path.append('../../')
from exercise.tree import TreeNode, build_tree, print_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None
        def find_nodes(node) -> bool:
            nonlocal ancestor
            if not node:
                return 0
            # find from left
            found_from_left = find_nodes(node.left)
            if found_from_left == 2:
                return 2
            if found_from_left == 1 and node.val in {p.val, q.val}:
                ancestor = node
                return 2
            found_from_right = find_nodes(node.right)
            if found_from_right == 2:
                return 2
            if found_from_right == 1 and node.val in {p.val, q.val}:
                ancestor = node
                return 2
            if found_from_left == found_from_right == 1:
                ancestor = node
                return 2
            return found_from_left + found_from_right + (1 if node.val in {p.val, q.val} else 0)

        find_nodes(root)
        return ancestor


if __name__ == '__main__':
    cases = [
        ((build_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(1)), TreeNode(3)),
        ((build_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(4)), TreeNode(5)),
        ((build_tree([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(0), TreeNode(8)), TreeNode(1))
    ]
    for case, expected in cases:
        actual = Solution().lowestCommonAncestor(*case)
        print_tree(case[0])
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
