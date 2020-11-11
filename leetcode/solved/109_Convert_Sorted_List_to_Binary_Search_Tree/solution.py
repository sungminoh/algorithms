#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, arr):
        if not arr:
            return None
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrayToBST(arr[:mid])
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.sortedArrayToBST(arr)


from collections import defaultdict
for_print = defaultdict(list)
def tree2list(root, depth=0):
    if depth == 0:
        for_print.clear()
    if not root:
        return for_print[depth].append(None)
    for_print[depth].append(root.val)
    tree2list(root.left, depth+1)
    tree2list(root.right, depth+1)
    ret = []
    for d in sorted(for_print.keys()):
        l = for_print[d]
        for i, v in enumerate(l):
            if v is not None:
                ret.extend(l[max(0, i-1):])
                break
    while ret and not ret[-1]:
        ret.pop()
    return ret


def get_list():
    nodes = [ListNode(x) for x in sorted(int(x) for x in input().split())]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    return head


def main():
    head = get_list()
    print(tree2list(Solution().sortedListToBST(head)))


if __name__ == '__main__':
    main()
