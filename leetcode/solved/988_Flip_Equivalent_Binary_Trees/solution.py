
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Note:
	1. Each tree will have at most 100 nodes.
	2. Each value in each tree will be a unique integer in the range [0, 99].
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


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return root1.val == root2.val \
            and ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
                 or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))


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


@pytest.mark.parametrize('a, b, expected', [
    ([0,3,1,None,None,None,2], [0,3,1,2], False)
])
def test(a, b, expected):
    print()
    r1, r2 = build_tree(a), build_tree(b)
    print_tree(r1)
    print('---')
    print_tree(r2)
    assert expected == Solution().flipEquiv(r1, r2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
