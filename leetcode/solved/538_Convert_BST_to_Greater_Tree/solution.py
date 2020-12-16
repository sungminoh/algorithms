#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:

Input: root = [0,null,1]
Output: [1,null,1]

Example 3:

Input: root = [1,0,2]
Output: [3,3,2]

Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]

Constraints:

	The number of nodes in the tree is in the range [0, 104].
	-104 <= Node.val <= 104
	All the values in the tree are unique.
	root is guaranteed to be a valid binary search tree.
"""
import sys
import pytest


# Definition for a binary tree node.
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def conv(node: TreeNode, val=0) -> TreeNode:
            if node.right:
                node.val += conv(node.right, val)
            else:
                node.val += val
            ret = node.val
            if node.left:
                ret = conv(node.left, node.val)
            return ret

        conv(root)
        return root


@pytest.mark.parametrize('tree, expected', [
    ([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8], [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]),
    ([0,None,1], [1,None,1]),
    ([1,0,2], [3,3,2]),
    ([3,2,4,1], [7,9,4,10]),
    ([-3,-4,0,None,None,-2,1], [-4,-8,1,None,None,-1,1])
])
def test(tree, expected):
    print()
    exp = build_tree(expected)
    root = build_tree(tree)
    print('------------------ input -------------------')
    print(root)
    print('----------------- expected -----------------')
    print(exp)
    print('------------------ actual ------------------')
    act = Solution().convertBST(root)
    print(act)
    assert exp == act


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
