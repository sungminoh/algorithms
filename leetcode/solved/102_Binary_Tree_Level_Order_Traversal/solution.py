#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    memo = defaultdict(list)

    def tree2list(self, r, d=0):
        if d == 0:
            self.memo.clear()
        if not r:
            return
        self.memo[d].append(r.val)
        self.tree2list(r.left, d+1)
        self.tree2list(r.right, d+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.tree2list(root)
        return [v for k, v in sorted(self.memo.items(), key=lambda x: x[0])]


def main():
    pass


if __name__ == '__main__':
    main()
