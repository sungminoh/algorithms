#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '(%r)' % self.val


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        stack = []
        cur = root
        while cur:
            ret.append(cur.val)
            stack.append(cur)
            cur = cur.left
            while not cur and stack:
                cur = stack.pop().right
        return ret


def main():
    import os, sys, importlib.util
    cfd = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(cfd, '../../exercise/tree.py')
    spec = importlib.util.spec_from_file_location('tree', module_path)
    tree = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tree)
    root = tree.build_tree([eval(x) for x in input().split()])
    tree.print_tree(root)
    print(Solution().preorderTraversal(root))


if __name__ == '__main__':
    main()
