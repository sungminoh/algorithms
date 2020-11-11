#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
"""
import pytest

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        cnt = 1
        for n in nodes:
            if cnt <= 0:
                return False
            if n != '#':
                cnt += 1
            elif n == '#':
                cnt -= 1
        return cnt == 0


    def _isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        return self.max_tree_size(nodes) == len(nodes)


    def max_tree_size(self, s):
        if not s:
            return 0
        if s[0] == '#':
            return 1
        left_size = self.max_tree_size(s[1:])
        right_size = self.max_tree_size(s[1 + left_size:])
        if not right_size:
            return 0
        else:
            return 1 + left_size + right_size


@pytest.mark.parametrize('preorder, ans', [
    ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
    ("1,#", False),
    ("9,#,#,1", False),
    ("1,#,#", True),
    ("1,2,3,4,5,#,#,#,#,#,#", True),
    ("1", False),
    ("#,7,6,9,#,#,#", False)
])
def test(preorder, ans):
    assert ans == Solution().isValidSerialization(preorder)


