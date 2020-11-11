#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode(%r, %r, %r)' % (self.val, self.left, self.right)


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        return [[root.val, *x]
                for x in self.pathSum(root.left, sum - root.val)\
                + self.pathSum(root.right, sum - root.val)]


def list2tree(arr):
    root = TreeNode(arr[0])
    level = [root]
    i = 1
    while level:
        t = level.pop(0)
        if not t:
            continue
        if i >= len(arr):
            break
        t.left = TreeNode(arr[i]) if arr[i] is not None else None; i += 1
        t.right = TreeNode(arr[i]) if arr[i] is not None else None; i += 1
        level.extend([t.left, t.right])
    return root


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
    root = list2tree([eval(x) for x in input().split()])
    print(Solution().pathSum(root, int(input())))


if __name__ == '__main__':
    main()
