#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        q = [[root], []]
        i = 0
        while q[0] or q[1]:
            level = []
            j = (i+1)%2
            while q[i]:
                n = q[i].pop(0)
                level.append(n.val)
                if n.left:
                    q[j].append(n.left)
                if n.right:
                    q[j].append(n.right)
            if i % 2 == 0:
                ret.append(level)
            else:
                ret.append(list(reversed(level)))
            i = j
        return ret


def get_tree():
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
    return root


def main():
    print(Solution().zigzagLevelOrder(get_tree()))


if __name__ == '__main__':
    main()
