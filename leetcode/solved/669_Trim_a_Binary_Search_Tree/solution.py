#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

Example 1:

Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Example 3:

Input: root = [1], low = 1, high = 2
Output: [1]

Example 4:

Input: root = [1,null,2], low = 1, high = 3
Output: [1,null,2]

Example 5:

Input: root = [1,null,2], low = 2, high = 4
Output: [2]

Constraints:

	The number of nodes in the tree in the range [1, 104].
	0 <= Node.val <= 104
	The value of each node in the tree is unique.
	root is guaranteed to be a valid binary search tree.
	0 <= low <= high <= 104
"""
import sys
import pytest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        from itertools import zip_longest
        left_lines = repr(self.left).split('\n') if self.left else []
        right_lines = repr(self.right).split('\n') if self.right else []
        node_padding = len(repr(self.val)) + 2
        left_padding = len(left_lines[0]) if left_lines else 0
        right_padding = len(right_lines[0]) if right_lines else 0
        lines = [' '*left_padding + rf'({self.val})' + ' '*right_padding]
        for ll, rl in zip_longest(left_lines, right_lines):
            if ll is not None:
                lines.append(ll + ' '*node_padding + (rl or ''))
            else:
                lines.append(' '*(node_padding + left_padding) + (rl or ''))
        return '\n'.join(lines)

    def __eq__(self, other):
        return other.val == self.val \
            and other.left == self.left \
            and other.right == self.right


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


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def remove_smaller(node, val):
            if not node:
                return None
            if node.val < val:
                return remove_smaller(node.right, val)
            node.left = remove_smaller(node.left, val)
            return node

        def remove_larger(node, val):
            if not node:
                return None
            if val < node.val:
                return remove_larger(node.left, val)
            node.right = remove_larger(node.right, val)
            return node

        root = remove_smaller(root, low)
        root = remove_larger(root, high)
        return root


@pytest.mark.parametrize('root, low, high, expected', [
    ([1,0,2], 1, 2, [1,None,2]),
    ([3,0,4,None,2,None,None,1], 1, 3, [3,2,None,1]),
    ([1], 1, 2, [1]),
    ([1,None,2], 1, 3, [1,None,2]),
    ([1,None,2], 2, 4, [2]),
    ([3,1,4,None,2], 3, 4, [3,None,4])
])
def test(root, low, high, expected):
    print()
    tree = build_tree(root)
    print(tree)
    print('------------------')
    actual = Solution().trimBST(tree, low, high)
    print(actual)
    assert build_tree(expected) == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
