#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

"""

import sys
sys.path.append('../exercise/')
from tree import build_tree, print_tree


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.mps(root))

    def mps(self, root):
        if not root:
            return -float('inf'), -float('inf')
        ll, l = self.mps(root.left)
        rr, r = self.mps(root.right)
        connected = root.val + max(0, l, r)
        unconnected = max(ll, rr, l, r, l + r + root.val)
        return unconnected, connected

    def maxSpanSum(self, root):
        if not root:
            return -float('inf'), -float('inf')
        ll, l = self.maxSpanSum(root.left)
        rr, r = self.maxSpanSum(root.right)
        connected = root.val + max(0, l, r, l+r)
        unconnected = max(ll, l, rr, r)
        print(root, connected, unconnected)
        return unconnected, connected


def main():
    # nodes = eval(input())
    # nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]  # 48
    nodes = [-2,1]
    root = build_tree(nodes)
    print_tree(root)
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    main()
