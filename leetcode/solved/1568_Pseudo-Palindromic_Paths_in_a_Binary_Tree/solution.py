from typing import Optional

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

Constraints:

	The number of nodes in the tree is in the range [1, 105].
	1 <= Node.val <= 9
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
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        """04/18/2021 13:37"""
        def is_leaf(node):
            return node.left is None and node.right is None

        def toggle(s, v):
            if v in s:
                s.remove(v)
            else:
                s.add(v)

        def dfs(node, odd):
            if is_leaf(node):
                toggle(odd, node.val)
                ret = 1 if len(odd) <= 1 else 0
                toggle(odd, node.val)
                return ret
            cnt = 0
            toggle(odd, node.val)
            if node.left:
                cnt += dfs(node.left, odd)
            if node.right:
                cnt += dfs(node.right, odd)
            toggle(odd, node.val)
            return cnt

        return dfs(root, set())

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """10/03/2022 22:09"""
        def dfs(node, bit):
            bit ^= (1<<node.val)
            if not node.left and not node.right:  # leaf
                lsb = bit&(~(bit-1))
                if bit ^ lsb == 0:
                    return 1
            ret = 0
            if node.left:
                ret += dfs(node.left, bit)
            if node.right:
                ret += dfs(node.right, bit)
            bit ^= (1<<node.val)
            return ret

        return dfs(root, 0) if root else 0

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """Feb 01, 2024 19:27"""
        def traverse(node, counter):
            if not node:
                return 0
            counter ^= (1<<node.val)
            if not node.left and not node.right:
                counter -= ~(counter-1) & counter
                return 0 if counter else 1
            return traverse(node.left, counter) + traverse(node.right, counter)

        return traverse(root, 0)


@pytest.mark.parametrize('args', [
    (([2,3,1,3,1,None,1], 2)),
    (([2,1,1,1,3,None,None,None,None,None,1], 1)),
    (([9], 1)),
])
def test(args):
    assert args[-1] == Solution().pseudoPalindromicPaths(build_tree(*args[:-1]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
