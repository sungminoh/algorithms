#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree_(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        left_size = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:left_size+1], inorder[:left_size])
        root.right= self.buildTree(preorder[1+left_size:], inorder[1+left_size:])
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(v):
            if not preorder or inorder[0] == v:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(v)
            return root
        return build(None)


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



def main():
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    print(tree2list(Solution().buildTree(preorder, inorder)))


if __name__ == '__main__':
    main()
