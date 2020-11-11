
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Note:

	The tree will have between 1 and 100 nodes.
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


def height(n):
    l, r = 0, 0
    if n.left:
        l = height(n.left)
    if n.right:
        r = height(n.right)
    return min(l, r) + 1, max(l, r) + 1


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        min_height = float('inf')
        updated = False
        def traverse(n, height=0):
            nonlocal min_height, updated
            # print(n, height, min_height, updated)
            if n == None:
                if height < min_height:
                    if updated:
                        return False
                    else:
                        if min_height < float('inf'):
                            updated = True
                        min_height = height
                elif height > min_height:
                    return False
                return True
            else:
                left = traverse(n.left, height + 1)
                if not left:
                    return False
                right = traverse(n.right, height + 1)
                if not right:
                    return False
                return True

        return traverse(root, 0)


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,3,4,5,6], True),
    ([1,2,3,4,5,None,7], False),
    ([1,None,2], False),
])
def test(nodes, expected):
    print()
    root = build_tree(nodes)
    print_tree(root)
    assert expected == Solution().isCompleteTree(root)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


