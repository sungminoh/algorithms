#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
import sys
sys.path.append('../exercise')
from tree import TreeNode, build_tree, print_tree


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        stack = []
        visited = []
        done = set()
        while root:
            stack.append(root)
            visited.append(False)
            if root not in done:
                root = root.left
            else:
                root = None
            while not root and stack:
                if not visited[-1]:
                    root = stack[-1].right
                    visited[-1] = True
                else:
                    while visited and visited[-1]:
                        root = stack.pop()
                        ret.append(root.val)
                        visited.pop()
                        done.add(root)
                    root = None
        return ret


def main():
    root = build_tree([eval(x) for x in input().split()])
    print_tree(root)
    print(Solution().postorderTraversal(root))


if __name__ == '__main__':
    main()
