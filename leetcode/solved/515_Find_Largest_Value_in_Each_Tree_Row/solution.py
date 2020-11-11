
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You need to find the largest value in each row of a binary tree.

Example:

Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""
import sys
from collections import defaultdict
from typing import List
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
    def largestValues(self, root: TreeNode) -> List[int]:
        mvh = defaultdict(lambda: -float('inf'))

        def dfs(n, height=0):
            if not n:
                return
            mvh[height] = max(mvh[height], n.val)
            dfs(n.left, height+1)
            dfs(n.right, height+1)

        dfs(root)
        return list(mvh.values())


@pytest.mark.parametrize('nodes, expected', [
    ([1,3,2,5,3,None,9], [1,3,9]),
    ([0,-1], [0,-1])
])
def test(nodes, expected):
    print()
    tree = build_tree(nodes)
    print_tree(tree)
    assert expected == Solution().largestValues(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
