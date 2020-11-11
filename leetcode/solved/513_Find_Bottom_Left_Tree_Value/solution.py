
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

  Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Note:
You may assume the tree (i.e., the given root node) is not NULL.
"""
import sys
import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '(%r)' % self.val


def build_tree(lst):
    root = TreeNode(lst[0])
    queue = [root]
    att = ['left', 'right']
    cur = 0
    for x in lst[1:]:
        node = TreeNode(x) if x is not None else None
        setattr(queue[0], att[cur], node)
        if cur:
            queue.pop(0)
        if node:
            queue.append(node)
        cur += 1
        cur %= 2
    return root


def print_tree(root):
    from itertools import zip_longest
    def build_lines(root):
        if not root:
            return [''], 0
        left, lw = build_lines(root.left)
        lp = ' '*lw
        right, rw = build_lines(root.right)
        rp = ' '*rw
        s = str(root)
        subs = [(l if l else lp) + ' '*len(s) + (r if r else rp) for l, r in zip_longest(left, right)]
        first_line = lp + s + rp
        return [first_line] + subs, len(first_line)
    lines, _ = build_lines(root)
    print('\n'.join(lines))


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        max_height = -float('inf')
        left_most = None

        def dfs(n, height=0):
            nonlocal max_height, left_most
            if not n:
                return
            if height > max_height:
                max_height = height
                left_most = n
            dfs(n.left, height+1)
            dfs(n.right, height+1)

        dfs(root)
        return left_most.val


@pytest.mark.parametrize('nodes, expected', [
    ([2,1,3], 1),
    ([1,2,3,4,5,6,None,None,7], 7),
])
def test(nodes, expected):
    print()
    tree = build_tree(nodes)
    print_tree(tree)
    assert expected == Solution().findBottomLeftValue(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
