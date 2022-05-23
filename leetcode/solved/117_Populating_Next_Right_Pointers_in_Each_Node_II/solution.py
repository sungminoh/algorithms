#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 6000].
	-100 <= Node.val <= 100

Follow-up:

	You may only use constant extra space.
	The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
import itertools
from typing import Tuple
from typing import List
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a Node.
class Node(TreeNode):
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not root:
            return None

        queue = [root]
        while queue:
            next_queue = []
            for i, n in enumerate(queue):
                if i > 0:
                    queue[i-1].next = queue[i]
                if n.left is not None:
                    next_queue.append(n.left)
                if n.right is not None:
                    next_queue.append(n.right)
            queue = next_queue

        return root

    def connect(self, root: 'Node') -> 'Node':
        """
        Recursive
        Time complexity: O(n)
        Space complexity: O(logn)  # height
        """
        def ziptree(root) -> Tuple[List[Node], List[Node]]:
            if not root:
                return [], []
            ll, lr = ziptree(root.left)
            rl, rr = ziptree(root.right)
            for l, r in itertools.zip_longest(lr, rl):
                if l is not None:
                    l.next = r
            left = [root]
            right = [root]
            for l1, l2, r1, r2 in itertools.zip_longest(ll, lr, rl, rr):
                left.append(l1 or l2 or r1 or r2)
                right.append(r2 or r1 or l2 or l1)
            return left, right

        lst = ziptree(root)
        return root

    def connect(self, root: 'Node') -> 'Node':
        """
        Use next pointer to iterate each level like a queue
        Time complexity: O(n)
        Space complexity: O(1)
        """
        head = root
        while head:  # iterate vertically
            next_head = None
            node = head
            cur = Node()  # dummy
            while node:  # iterate horizontally
                if next_head is None:
                    next_head = node.left or node.right
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                node = node.next
            head = next_head

        return root


def serialize(root):
    ret = []
    while root:
        node = root
        while node:
            ret.append(node.val)
            node = node.next
        else:
            ret.append('#')
        root = root.left
    return ret


@pytest.mark.parametrize('values, expected', [
    ([1,2,3,4,5,6,7], [1,'#',2,3,'#',4,5,6,7,'#']),
    ([1,2,3,4,5,None,7], [1,'#',2,3,'#',4,5,7,'#']),
    ([], []),
    ([1,2,3,4,5,None,6,7,None,None,None,None,8], [1,'#',2,3,'#',4,5,6,'#',7,8,'#']),
])
def test(values, expected):
    tree = build_tree(values, Node)
    print('\n------------')
    print(tree)
    assert expected == serialize(Solution().connect(tree))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
