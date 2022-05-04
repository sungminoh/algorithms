#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

	The number of nodes in the tree is n.
	1 <= k <= n <= 104
	0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """08/25/2019 16:16"""
        kth = None
        cnt = 0
        def find_kth_smallest(node):
            if not node:
                return False
            if find_kth_smallest(node.left):
                return True
            nonlocal cnt, kth
            cnt += 1
            if cnt == k:
                kth = node.val
                return True
            return find_kth_smallest(node.right)
        find_kth_smallest(root)
        return kth

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """05/01/2022 19:49"""
        def inorder(node, k) -> int:
            if not node:
                return 0, None
            left_cnt, target = inorder(node.left, k)
            if target is not None:
                return 0, target
            k -= left_cnt + 1
            if k == 0:
                return 0, node.val
            right_cnt, target = inorder(node.right, k)
            if target is not None:
                return 0, target
            return left_cnt + right_cnt + 1, None

        return inorder(root, k)[1]


@pytest.mark.parametrize('values, k, expected', [
    ([3,1,4,None,2], 1, 1),
    ([5,3,6,2,4,None,None,1], 3, 3),
    ([31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9], 1, 0)
])
def test(values, k, expected):
    root = build_tree(values)
    print()
    print(root)
    assert expected == Solution().kthSmallest(root, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
