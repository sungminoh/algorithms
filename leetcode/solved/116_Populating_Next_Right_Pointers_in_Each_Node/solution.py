#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return 'TreeLinkNode(%r, %r, %r, %r)' % (self.val, self.left, self.right, self.next)
        # return 'TreeLinkNode(%r)' % (self.val)


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = [[root], []]
        i = 0
        j = (i+1)%2
        while q[0] or q[1]:
            while q[i]:
                node = q[i].pop(0)
                node.next = q[i][0] if q[i] else None
                if node.left:
                    q[j].append(node.left)
                if node.right:
                    q[j].append(node.right)
            i = j
            j = (i+1)%2


def list2tree(arr):
    root = TreeLinkNode(arr[0])
    level = [root]
    i = 1
    while level:
        t = level.pop(0)
        if not t:
            continue
        if i >= len(arr):
            break
        t.left = TreeLinkNode(arr[i]) if arr[i] is not None else None; i += 1
        t.right = TreeLinkNode(arr[i]) if arr[i] is not None else None; i += 1
        level.extend([t.left, t.right])
    return root


def main():
    root = list2tree([eval(x) for x in input().split()])
    Solution().connect(root)
    while root:
        p = root
        while p:
            print(p.val, end=' ')
            p = p.next
        print()
        root = root.left


if __name__ == '__main__':
    main()
