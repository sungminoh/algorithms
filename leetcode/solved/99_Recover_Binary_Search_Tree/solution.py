#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

"""

import sys
sys.path.append('../../exercise')
from tree import TreeNode, build_tree, print_tree


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.cur = self.first = self.second = None
        self.recover(root)
        self.swap(self.first, self.second)

    def recover(self, node):
        if not node:
            return
        self.recover(node.left)
        if self.cur and self.cur.val > node.val:
            if not self.first:
                self.first = self.cur
            self.second = node
        self.cur = node
        self.recover(node.right)


    def swap(self, n, m):
        n.val, m.val = m.val, n.val

    def __recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        lmin, lmax = self.minmax(root.left)
        rmin, rmax = self.minmax(root.right)
        if lmax is not None and rmin is not None and lmax.val > rmin.val:
            lmax.val, rmin.val = rmin.val, lmax.val
        elif lmax is not None and lmax.val > root.val:
            lmax.val, root.val = root.val, lmax.val
        elif rmin is not None and rmin.val < root.val:
            rmin.val, root.val = root.val, rmin.val
        else:
            self.recoverTree(root.left)
            self.recoverTree(root.right)

    def minmax(self, node):
        if node is None:
            return None, None
        lmin, lmax = self.minmax(node.left)
        rmin, rmax = self.minmax(node.right)
        return min(lmin, rmin, node, key=lambda x: x.val if x is not None else float('inf')),\
            max(lmax, rmax, node, key=lambda x: x.val if x is not None else -float('inf'))

    def _recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        current = self.inorder(root)
        actual = sorted(current, key=lambda x: x.val)
        swaped = []
        for i, (a, b) in enumerate(zip(current, actual)):
            if a != b:
                a.val, b.val = b.val, a.val
                break

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node] + self.inorder(node.right)



def main():
    root = build_tree(eval(input()))
    print("input:")
    print_tree(root)
    print("output:")
    Solution().recoverTree(root)
    print_tree(root)


if __name__ == '__main__':
    main()
