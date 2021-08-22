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
from pathlib import Path
import sys
import pytest
sys.path.append(str(Path('__file__').absolute().parent.parent))
from exercise.tree import TreeNode


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
        def find(node) -> Tuple[TreeNode, bool, bool]:
            """
            Returns [Common Ancestor, Found p, Found q]
            """
            if not node:
                return None, False, False
            la, lp, lq= find(node.left)
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


def build_tree(lst, values=None):
    if not lst:
        return None
    values = values or []
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    value_nodes = {node.val: node for node in nodes if node and node.val in values}
    root = nodes[0]
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for node in nodes[1:]:
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root, value_nodes


@pytest.mark.parametrize('nodes, p, q, expected', [
    ([3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3),
    ([3,5,1,6,2,0,8,None,None,7,4], 5, 4, 5),
    ([1,2], 1, 2, 1),
])
def test(nodes, p, q, expected):
    root, value_nodes = build_tree(nodes, [p, q])
    p = value_nodes[p]
    q = value_nodes[q]
    actual = Solution().lowestCommonAncestor(root, p, q)
    print()
    print(actual)
    assert expected == actual.val


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
