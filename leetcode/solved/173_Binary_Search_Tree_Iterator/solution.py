#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
import sys
sys.path.append('../exercise')
from tree import TreeNode, build_bst, print_tree


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        n = self.stack.pop()
        cur = n.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return n.val


def main():
    root = build_bst([int(x) for x in input().split()])
    print_tree(root)
    # Your BSTIterator will be called like this:
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    print(v)


if __name__ == '__main__':
    main()
