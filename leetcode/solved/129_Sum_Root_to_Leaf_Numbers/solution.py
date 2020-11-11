#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum_numbers(self, root):
        if not root.left and not root.right:
            return [(root.val, 1)]
        ret = []
        if root.left:
            left = self.sum_numbers(root.left)
            ret.extend([(root.val * (10 ** ll) + ls, ll + 1) for ls, ll in left])
        if root.right:
            right = self.sum_numbers(root.right)
            ret.extend([(root.val * (10 ** rl) + rs, rl + 1) for rs, rl in right])
        return ret

    def dfs(self, root, val):
        if not root:
            return 0
        val = val*10 + root.val
        if not root.left and not root.right:
            return val
        return self.dfs(root.left, val) + self.dfs(root.right, val)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)


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
        if i < len(arr):
            t.left = TreeNode(arr[i]) if arr[i] is not None else None; i += 1
        if i < len(arr):
            t.right = TreeNode(arr[i]) if arr[i] is not None else None; i += 1
        level.extend([t.left, t.right])
    return root


def main():
    tree = list2tree([eval(x) for x in input().split()])
    print(Solution().sumNumbers(tree))


if __name__ == '__main__':
    main()
