#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

	BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
	boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
	int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

Constraints:

	The number of nodes in the tree is in the range [1, 105].
	0 <= Node.val <= 106
	At most 105 calls will be made to hasNext, and next.

Follow up:

	Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
from typing import Optional
import pytest
import sys
sys.path.append('../')
from exercise.tree import build_tree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    """07/28/2018 19:22"""
    def __init__(self, root):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def hasNext(self):
        if self.stack:
            return True
        else:
            return False

    def next(self):
        n = self.stack.pop()
        cur = n.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return n.val


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.insert_all_left(root)

    def insert_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.insert_all_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
     [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []],
     [None, 3, 7, True, 9, True, 15, True, 20, False],),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands.pop(0)](build_tree(*arguments.pop(0)))
    expecteds.pop(0)
    for cmd, arg, exp in zip(commands, arguments, expecteds):
        assert exp == getattr(obj, cmd)(*arg)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

