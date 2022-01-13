#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 212 - 1].
	-1000 <= Node.val <= 1000

Follow-up:

	You may only use constant extra space.
	The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
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
    def connect(self, root):
        """05/06/2018 23:03"""
        if not root:
            return
        q = [[root], []]
        i = 0
        j = (i+1)%2
        while q[0] or q[1]:
            while q[i]:
                node = q[i].pop(0)
                node.next = q[i][0] if q[i] else None
                if node.left:
                    q[j].append(node.left)
                if node.right:
                    q[j].append(node.right)
            i = j
            j = (i+1)%2

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n)
        Space complexity: O(n/2)  # the number of leaf nodes
        """
        row = [root]
        while row:
            next_row = []
            for i in range(len(row)):
                if i+1 < len(row):
                    row[i].next = row[i+1]
                if row[i].left:
                    next_row.append(row[i].left)
                if row[i].right:
                    next_row.append(row[i].right)
            row = next_row
        return root

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time complexity: O(n*h)
        Space complexity: O(h)  # height
        """
        if not root:
            return
        self.connect(root.left)
        self.connect(root.right)
        l = root.left
        r = root.right
        while l and r:
            l.next = r
            l = l.right
            r = r.left
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
    ([], []),
])
def test(values, expected):
    tree = build_tree(values, Node)
    print('\n------------')
    print(tree)
    assert expected == serialize(Solution().connect(tree))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
