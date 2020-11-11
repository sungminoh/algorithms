#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
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


if __name__ == '__main__':
    cases = [
        (([3,1,4,None,2], 1), 1),
        (([5,3,6,2,4,None,None,1], 3), 3),
    ]
    for case, expected in cases:
        actual = Solution().kthSmallest(build_tree(case[0]), case[1])
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
