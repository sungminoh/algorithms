#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

	The number of nodes in the tree is in the range [2, 105].
	-109 <= Node.val <= 109
	All Node.val are unique.
	p != q
	p and q will exist in the tree.
"""
from typing import Tuple
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """08/25/2019 19:40"""
        ancestor = None
        def find_nodes(node) -> int:
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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """08/21/2021 16:57"""
        def find(node) -> Tuple[TreeNode, bool, bool]:
            """
            Returns [Common Ancestor, Found p, Found q]
            """
            if not node:
                return None, False, False
            la, lp, lq = find(node.left)
            if la:
                return la, True, True
            ra, rp, rq = find(node.right)
            if ra:
                return ra, True, True
            if (lp or node == p) and (rq or node == q):
                return node, True, True
            if (lq or node == q) and (rp or node == p):
                return node, True, True
            return None, lp or rp or node == p, lq or rq or node == q

        return find(root)[0]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """08/06/2022 22:28"""
        lca = None
        def dfs(root, nodes):
            """
            Return an integer whose binary representation represents existence
            of i'th node in nodes if i'th digit is 1.
            If all nodes are found, update a non-local variable and stop
            recursion.
            """
            nonlocal lca
            if not root:
                return 0
            found = 0
            for i, node in enumerate(nodes):
                if root.val == node.val:
                    found |= (1<<i)
            found |= dfs(root.left, nodes)
            if lca is None and found == (1<<len(nodes))-1:
                lca = root
                return found
            found |= dfs(root.right, nodes)
            if lca is None and found == (1<<len(nodes))-1:
                lca = root
                return found
            return found

        dfs(root, [p, q])
        return lca


@pytest.mark.parametrize('values, p, q, expected', [
    ([3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3),
    ([3,5,1,6,2,0,8,None,None,7,4], 5, 4, 5),
    ([1,2], 1, 2, 1),
])
def test(values, p, q, expected):
    def find(root, x):
        if not root:
            return None
        if root.val == x:
            return root
        return find(root.left, x) or find(root.right, x)

    root = build_tree(values)
    p = find(root, p)
    q = find(root, q)
    assert expected == Solution().lowestCommonAncestor(root, p, q).val


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
