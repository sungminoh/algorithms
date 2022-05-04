#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:

	The number of nodes in the tree is in the range [2, 1000].
	-231 <= Node.val <= 231 - 1

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""
from typing import Tuple
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
    def recoverTree(self, root):
        """08/15/2018 00:23
        Space complexity: O(n)
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node] + inorder(node.right)

        current = inorder(root)
        actual = sorted(current, key=lambda x: x.val)
        swaped = []
        for i, (a, b) in enumerate(zip(current, actual)):
            if a != b:
                a.val, b.val = b.val, a.val
                break

    def recoverTree(self, root):
        """08/15/2018 00:55
        Space complexity: O(1)
        """
        if not root:
            return

        def minmax(node):
            if node is None:
                return None, None
            lmin, lmax = minmax(node.left)
            rmin, rmax = minmax(node.right)
            return min(lmin, rmin, node, key=lambda x: x.val if x is not None else float('inf')),\
                max(lmax, rmax, node, key=lambda x: x.val if x is not None else -float('inf'))

        lmin, lmax = minmax(root.left)
        rmin, rmax = minmax(root.right)
        if lmax is not None and rmin is not None and lmax.val > rmin.val:
            lmax.val, rmin.val = rmin.val, lmax.val
        elif lmax is not None and lmax.val > root.val:
            lmax.val, root.val = root.val, lmax.val
        elif rmin is not None and rmin.val < root.val:
            rmin.val, root.val = root.val, rmin.val
        else:
            self.recoverTree(root.left)
            self.recoverTree(root.right)

    def recoverTree(self, root):
        """08/15/2018 03:31"""
        cur = first = second = None

        def recover(node):
            nonlocal cur, first, second
            if not node:
                return
            recover(node.left)
            if cur and cur.val > node.val:
                if not first:
                    first = cur
                second = node
            cur = node
            recover(node.right)

        def swap(n, m):
            n.val, m.val = m.val, n.val

        recover(root)
        swap(first, second)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """05/02/2022 11:14
        Do not return anything, modify root in-place instead.
        """
        targets = [None, None]
        def inorder(node) -> Tuple[TreeNode, TreeNode, bool]:
            if node.left:
                left_min, left_max = inorder(node.left)
            else:
                left_min = left_max = node

            if node.right:
                right_min, right_max = inorder(node.right)
            else:
                right_min = right_max = node

            nonlocal targets
            # Swap one from left and one from right
            if left_max.val > node.val and right_min.val < node.val:
                targets = [left_max, right_min]
            # Swap with the node
            elif left_max.val > node.val:
                targets = [left_max, node]
            elif right_min.val < node.val:
                targets = [right_min, node]

            if left_max.val > right_max.val:
                right_max = left_max
            if right_min.val < left_min.val:
                left_min = right_min

            return (min([left_min, right_min, node], key=lambda x: x.val),
                    max([left_max, right_max, node], key=lambda x: x.val))

        inorder(root)
        targets[0].val, targets[1].val = targets[1].val, targets[0].val


@pytest.mark.parametrize('values, expected', [
    ([1,3,None,None,2], [3,1,None,None,2]),
    ([3,1,4,None,None,2], [2,1,4,None,None,3]),
    ([146,71,-13,55,None,231,399,321,None,None,None,None,None,-33], [146,71,321,55,None,231,399,-13,None,None,None,None,None,-33]),
])
def test(values, expected):
    root = build_tree(values)
    print()
    print(root)
    Solution().recoverTree(root)
    print()
    print(root)
    assert build_tree(expected) == root


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
