#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

# Definition for a binary tree node.
import pytest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.max_in_ex_root(root))

    def max_in_ex_root(self, root: TreeNode) -> int:
        if not root:
            return 0, 0
        left_in, left_ex = self.max_in_ex_root(root.left)
        right_in, right_ex = self.max_in_ex_root(root.right)
        root_in = root.val + left_ex + right_ex
        root_ex = max(left_in, left_ex) + max(right_in, right_ex)
        return root_in, root_ex


def arr_to_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    left_or_right = 0
    for v in arr[1:]:
        if v is None:
            if left_or_right == 1:
                queue.pop(0)
        else:
            node = TreeNode(v)
            if left_or_right == 0:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.pop(0)
            queue.append(node)
        left_or_right ^= 1
    return root


def print_tree(root: TreeNode, depth=0):
    print(root.val)
    if not root.left and not root.right:
        return
    if root.left:
        print(' ' * depth + '└', end='')
        print_tree(root.left, depth + 1)
    else:
        print()
    if root.right:
        print(' ' * depth + '└', end='')
        print_tree(root.right, depth + 1)
    else:
        print()


@pytest.mark.parametrize('arr', [
    [3,2,3,None,3,None,1],
    [3,4,5,1,3,None,1],
])
def test_build(arr):
    print()
    print_tree(arr_to_tree(arr))



@pytest.mark.parametrize('arr, ans', [
    ([3,2,3,None,3,None,1], 7),
    ([3,4,5,1,3,None,1], 9),
    ([1,9,9], 18),
    ([9,100,1], 101),
    ([100,0,0,0,0,0,0,100,0,0,0,100,0,0,0], 300)
])
def test_sol(arr, ans):
    root = arr_to_tree(arr)
    assert ans == Solution().rob(root)
