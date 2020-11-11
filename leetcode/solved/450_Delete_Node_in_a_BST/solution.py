
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
import sys
import pytest


def format_tree(root):
    from itertools import zip_longest
    def build_lines(root):
        if not root:
            return [''], 0
        left, lw = build_lines(root.left)
        lp = ' '*lw
        right, rw = build_lines(root.right)
        rp = ' '*rw
        s = str(root.val)
        subs = [(l if l else lp) + ' '*len(s) + (r if r else rp) for l, r in zip_longest(left, right)]
        first_line = lp + s + rp
        return [first_line] + subs, len(first_line)
    lines, _ = build_lines(root)
    return '\n'.join(lines)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '(%r)' % self.val

    def __str__(self):
        return format_tree(self)

    def __eq__(self, other):
        return other and self.val == other.val


def build_bst(lst):
    def insert(root, node):
        if node.val < root.val:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
    if not lst:
        return None
    nodes = [TreeNode(x) for x in lst]
    root = nodes[0]
    for node in nodes[1:]:
        insert(root, node)
    return root


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


def find(root, key, parent=None):
    if not root:
        return None, parent
    if key < root.val:
        return find(root.left, key, root)
    elif root.val < key:
        return find(root.right, key, root)
    else:
        return root, parent


def get_max_and_parent(root, parent=None):
    if not root.right:
        return root, parent
    else:
        return get_max_and_parent(root.right, root)


def predecessor_and_parent(root, parent=None):
    if not root.left:
        return None, root
    else:
        return get_max_and_parent(root.left, root)


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def delete(root):
            if not root.left:
                return root.right
            if not root.left.right:
                root.left.right = root.right
                return root.left
            else:
                parent = root.left
                pred = root.left.right
                while pred.right:
                    parent = pred
                    pred = pred.right
                pred.left, pred.right, root.left, root.right \
                    = root.left, root.right, pred.left, pred.right
                parent.right = delete(root)
                return pred
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val == key:
            return delete(root)
        else:
            return root


@pytest.mark.parametrize('tree, k', [
    ([5,3,6,2,4,None,7], 3),
    ([5,3,6,2,4,None,7], 6),
    ([5,3,6,2,4,None,7], 2),
    ([5,3,6,2,4,None,7], 4),
    ([5,3,6,2,4,None,7], 7),
    ([5,3,6,2,4,None,7], 5),
    ([5,3,6,2,4,None,7], 0),
])
def test(tree, k):
    print()
    t = build_tree(tree)
    print(t)
    print(Solution().deleteNode(t, k))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
