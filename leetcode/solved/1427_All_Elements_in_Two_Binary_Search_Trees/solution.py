#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

	The number of nodes in each tree is in the range [0, 5000].
	-105 <= Node.val <= 105
"""
from typing import List
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


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        v1 = list(inorder(root1))
        v2 = list(inorder(root2))
        i, j = 0, 0
        ret = []
        while i < len(v1) or j < len(v2):
            if j >= len(v2):
                ret.append(v1[i])
                i += 1
            elif i >= len(v1):
                ret.append(v2[j])
                j += 1
            else:
                if v1[i] <= v2[j]:
                    ret.append(v1[i])
                    i += 1
                else:
                    ret.append(v2[j])
                    j += 1
        return ret

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        class Inorder:
            def __init__(self, root):
                self.root = root
                self.stack = []
                self.__insert_all_left(root)

            def __insert_all_left(self, node):
                while node:
                    self.stack.append(node)
                    node = node.left

            def has_next(self):
                return len(self.stack) > 0

            def next(self):
                node = self.stack.pop()
                self.__insert_all_left(node.right)
                return node.val

            def peak(self):
                return self.stack[-1].val

        traverse1 = Inorder(root1)
        traverse2 = Inorder(root2)
        ret = []
        while traverse1.has_next() or traverse2.has_next():
            if not traverse1.has_next():
                ret.append(traverse2.next())
            elif not traverse2.has_next():
                ret.append(traverse1.next())
            else:
                if traverse1.peak() <= traverse2.peak():
                    ret.append(traverse1.next())
                else:
                    ret.append(traverse2.next())
        return ret


@pytest.mark.parametrize('values1, values2, expected', [
    ([2,1,4], [1,0,3], [0,1,1,2,3,4]),
    ([1,None,8], [8,1], [1,1,8,8]),
])
def test(values1, values2, expected):
    root1 = build_tree(values1)
    root2 = build_tree(values2)
    assert expected == Solution().getAllElements(root1, root2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
