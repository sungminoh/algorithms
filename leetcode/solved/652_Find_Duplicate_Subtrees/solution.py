#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
"""
from collections import defaultdict
import sys
from IPython.utils.process import abbrev_cwd
from typing import List
import pytest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return '(%r)' % self.val

    def __eq__(self, other):
        return other and self.val == other.val


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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        ret = dict()
        id_map = defaultdict()
        def get_id(node):
            if not node:
                return
            left = get_id(node.left)
            right = get_id(node.right)
            key = (node.val, left, right)
            if key not in id_map:
                id_map[key] = len(id_map)
            else:
                ret[key] = node
            return id_map[key]
        get_id(root)
        return list(ret.values())


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,None,2,4,None,None,4], [[2,4], [4]]),
    ([0,0,0,0,None,None,0,None,None,0,0], [[0,0,0],[0]]),
])
def test(nodes, expected):
    print()
    tree = build_tree(nodes)
    print_tree(tree)
    print('---------------------------------------')
    actuals = Solution().findDuplicateSubtrees(tree)
    for t in actuals:
        print_tree(t)
        print('---------------------------------------')

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
