#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flatten_(root):
            if not root:
                return None, None
            t = root
            hl, tl = flatten_(root.left)
            hr, tr = flatten_(root.right)
            if hl:
                root.right = hl
                t = tl
            if hr:
                t.right = hr
                t = tr
            root.left = None
            return root, t

        flatten_(root)
        return root



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
    print(Solution().flatten(root))

if __name__ == '__main__':
    main()
