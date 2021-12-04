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

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []

Constraints:

	The number of nodes in the tree is in the range [0, 104].
	-105 <= Node.val <= 105
	Each node has a unique value.
	root is a valid binary search tree.
	-105 <= key <= 105

Follow up: Could you solve it with time complexity O(height of tree)?
"""
import sys
from typing import Optional
import pytest
sys.path.append('../')
from exercise.tree import TreeNode, build_tree, serialize_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """05/02/2020 18:36"""
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

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # if root.left is None:
                # return root.right
            if root.right is None:
                return root.left
            # find successor
            p, n = None, root.right
            while n.left:
                p = n
                n = n.left
            if p is None:
                n.left = root.left
                return n
            else:
                n.left, root.left = root.left, None
                n.right, root.right = root.right, n.right
                p.left = root
                p.left = self.deleteNode(p.left, key)
                return n


@pytest.mark.parametrize('nodes, key, expected', [
    ([3,2,4], 3, [4,2]),
    ([5,3,6,2,4,None,7], 3, [5,4,6,2,None,None,7]),
    ([5,3,6,2,4,None,7], 0, [5,3,6,2,4,None,7]),
    ([], 0, []),
    ([2,1,5,None,None,3,6], 5, [2,1,6,None,None,3]),
    ([2,0,33,None,1,25,40,None,None,11,31,34,45,10,18,29,32,None,36,43,46,4,None,12,24,26,30,None,None,35,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None,None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6],
     33,
     [2,0,34,None,1,25,40,None,None,11,31,35,45,10,18,29,32,None,36,43,46,4,None,12,24,26,30,None,None,None,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None,None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6]),
])
def test(nodes, key, expected):
    print()
    tree = build_tree(nodes)
    print(tree)
    print(key)
    expected_tree = build_tree(expected)
    actual_tree = Solution().deleteNode(tree, key)
    print(actual_tree)
    print('--------------------------------')
    print(expected_tree)
    assert expected == serialize_tree(actual_tree)
    assert expected_tree == actual_tree

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
