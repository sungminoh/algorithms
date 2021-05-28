#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, flatten the tree into a "linked list":

	The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
	The "linked list" should be in the same order as a pre-order traversal of the binary tree.

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

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

Constraints:

	The number of nodes in the tree is in the range [0, 2000].
	-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from pathlib import Path
import pytest
import sys
sys.path.append(f'{Path(__file__).parent.parent.parent.parent}/exercise')


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
    if not lst:
        return None
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
    def flatten(self, root):
        """
        05/07/2018 14:19
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

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def to_list(node: TreeNode):
            if node is None:
                return None, None
            left_head, left_tail = to_list(node.left)
            right_head, right_tail = to_list(node.right)
            if left_tail is None and right_head is None:
                return node, node
            node.left = None
            if left_tail is None:
                node.right, right_head.left = right_head, None
                return node, right_tail
            node.right, left_head.left = left_head, None
            if right_head is None:
                return node, left_tail
            left_tail.right, right_head.left = right_head, None
            return node, right_tail

        to_list(root)[0]


def to_array(root: TreeNode):
    elements = []
    node = root
    while node:
        elements.append(node.val)
        # if node.right:
            # assert(id(node.right.left) == id(node))
        node = node.right
    return elements


@pytest.mark.parametrize('nodes, expected', [
    ([1,2,5,3,4,None,6], [1,None,2,None,3,None,4,None,5,None,6]),
    ([], []),
    ([0], [0]),
])
def test(nodes, expected):
    print()
    root = build_tree(nodes)
    print(root)
    Solution().flatten(root)
    print(root)
    array = to_array(root)
    print(array)
    assert [x for x in expected if x is not None] == array



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
