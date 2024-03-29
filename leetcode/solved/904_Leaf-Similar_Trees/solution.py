import itertools
from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

	The number of nodes in each tree will be in the range [1, 200].
	Both of the given trees will have values in the range [0, 200].
"""
import pytest
import sys
sys.path.append('../')
from exercise.tree import TreeNode, build_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Dec 11, 2022 16:24"""
        def leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from leaves(node.left)
            if node.right:
                yield from leaves(node.right)

        return all(x==y for x, y in itertools.zip_longest(leaves(root1), leaves(root2)))

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Feb 18, 2023 19:41"""
        def leaf_seq(tree):
            if tree.left:
                yield from leaf_seq(tree.left)
            if tree.right:
                yield from leaf_seq(tree.right)
            if not tree.left and not tree.right:
                yield tree.val
        return all(x == y for x, y in itertools.zip_longest(leaf_seq(root1), leaf_seq(root2)))


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """Jan 22, 2024 22:15"""
        def traverse(node):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from traverse(node.left)
            if node.right:
                yield from traverse(node.right)

        return all(a == b for a, b in itertools.zip_longest(traverse(root1), traverse(root2)))


@pytest.mark.parametrize('args', [
    (([3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8], True)),
    (([1,2,3], [1,3,2], False)),
])
def test(args):
    assert args[-1] == Solution().leafSimilar(*[build_tree(x) for x in args[:-1]])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
