#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree_(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        from collections import defaultdict
        memo = defaultdict(list)
        for i, v in enumerate(inorder):
            memo[v].append(i)

        def build(in_s, in_e, post_s, post_e):
            if in_e < in_s or post_e < post_s:
                return None
            root = TreeNode(postorder[post_e])
            i = memo[root.val].pop()
            root.left = build(in_s, i-1, post_s, post_s+(i-1-in_s))
            root.right = build(i+1, in_e, post_s+(i-1-in_s)+1, post_e-1)
            return root

        return build(0, len(inorder)-1, 0, len(postorder)-1)

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def build(v):
            if not postorder or inorder[-1] == v:
                return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(v)
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
