#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        p = root
        while p:
            stack.append(p)
            p = p.left
            while not p and stack:
                p = stack.pop()
                ret.append(p.val)
                p = p.right
        return ret

    def inorderTraversalRec(self, root):
        if not root:
            return []
        return self.inorderTraversalRec(root.left)\
            + [root.val]\
            + self.inorderTraversalRec(root.right)


def main():
    vs = [int(x) for x in input().split()]
    root = None
    for v in vs:
        v = int(v)
        if not root:
            root = TreeNode(v)
        else:
            p = root
            while True:
                if v < p.val:
                    if not p.left:
                        p.left = TreeNode(v)
                        break
                    else:
                        p = p.left
                else:
                    if not p.right:
                        p.right = TreeNode(v)
                        break
                    else:
                        p = p.right
    print(Solution().inorderTraversal(root))
    print(Solution().inorderTraversalRec(root))


if __name__ == '__main__':
    main()
