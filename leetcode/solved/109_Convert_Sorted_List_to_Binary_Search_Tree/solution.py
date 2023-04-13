#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:

Input: head = []
Output: []

Constraints:

	The number of nodes in head is in the range [0, 2 * 104].
	-105 <= Node.val <= 105
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.list import build_list, ListNode
from exercise.tree import TreeNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        """May 06, 2018 19:50"""
        def sortedArrayToBST(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = sortedArrayToBST(arr[:mid])
            root.right = sortedArrayToBST(arr[mid+1:])
            return root

        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return sortedArrayToBST(arr)

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Apr 13, 2023 00:08"""
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        def build(i, j):
            if i > j:
                return None
            if i == j:
                return TreeNode(vals[i])
            m = i + (j-i)//2
            return TreeNode(vals[m], build(i, m-1), build(m+1, j))

        return build(0, len(vals)-1)


@pytest.mark.parametrize('args', [
    (([-10,-3,0,5,9], [0,-3,9,-10,None,5])),
    (([], [])),
])
def test(args):
    def check(root):
        if not root:
            return 0, True
        ld, lr = check(root.left)
        rd, rr = check(root.right)
        return max(ld, rd)+1, lr and rr and ld <= rd+1 and ld+1 >= rd

    root = Solution().sortedListToBST(build_list(*args[:-1]))
    print()
    print(root)
    depth, balanced = check(root)
    assert balanced


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
