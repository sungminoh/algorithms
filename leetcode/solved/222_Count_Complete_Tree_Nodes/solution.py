#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""
import sys
sys.path.append('../../')
from exercise.tree import TreeNode, build_tree


class Solution:
    def height(self, root):
        return 0 if not root else (1 + self.height(root.left))

    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        h = self.height(root)
        while root:
            if self.height(root.right) == h - 1:
                cnt += 2 ** (h - 1)
                root = root.right
            else:
                cnt += 2 ** (h - 2)
                root = root.left
            h -= 1
        return cnt

    def __countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def find_diff(node: TreeNode, d: int):
            if node.left and node.right:
                in_right, rd = find_diff(node.right, d + 1)
                if in_right:
                    return in_right, rd
                in_left, ld = find_diff(node.left, d + 1)
                if in_left:
                    return in_left + 2 ** (rd - d), ld
                if ld != rd:
                    return 2 ** (rd - d), ld
                return 0, ld
            elif not node.left and not node.right:
                return 0, d
            else:
                return 1, d + 1
        missing, depth = find_diff(root, 1)
        return 2 ** depth - 1 - missing


if __name__ == '__main__':
    cases = [
        build_tree([1]),
        build_tree([1,2]),
        build_tree([1,2,3]),
        build_tree([1,2,3,4]),
        build_tree([1,2,3,4,5]),
        build_tree([1,2,3,4,5,6]),
        build_tree([1,2,3,4,5,6,7]),
        build_tree([1,2,3,4,5,6,7,8]),
        build_tree([1,2,3,4,5,6,7,8,9]),
        build_tree([1,2,3,4,5,6,7,8,9,10]),
        build_tree([1,2,3,4,5,6,7,8,9,10,11]),
        build_tree([1,2,3,4,5,6,7,8,9,10,11,12]),
        build_tree([1,2,3,4,5,6,7,8,9,10,11,12,13]),
    ]
    expecteds = [
        1,2,3,4,5,6,7,8,9,10,11,12,13
    ]
    for tree, expected in zip(cases, expecteds):
        actual = Solution().countNodes(tree)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
