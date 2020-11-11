#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
import sys
sys.path.append('../exercise')
from tree import build_tree


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.right_side = []
        self.look_at_nth_from_right(root, 0)
        return self.right_side

    def look_at_nth_from_right(self, tree, depth):
        if not tree:
            return
        if len(self.right_side) <= depth:
            self.right_side.append(tree.val)
        self.look_at_nth_from_right(tree.right, depth + 1)
        self.look_at_nth_from_right(tree.left, depth + 1)


def main():
    inputs = []
    inputs.append(([1,2,3,None,5,None,4], [1,3,4]))

    for tlist, expected in inputs:
        tree = build_tree(tlist)
        actual = Solution().rightSideView(tree)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')


if __name__ == '__main__':
    main()
