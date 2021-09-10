#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

	For example, it could never contain two consecutive commas, such as "1,,3".

Note: You are not allowed to reconstruct the tree.

Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:
Input: preorder = "1,#"
Output: false
Example 3:
Input: preorder = "9,#,#,1"
Output: false

Constraints:

	1 <= preorder.length <= 104
	preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
"""
import sys
import pytest


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """04/07/2020 03:14"""
        def max_tree_size(s):
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

        nodes = preorder.split(',')
        return max_tree_size(nodes) == len(nodes)

    def isValidSerialization(self, preorder: str) -> bool:
        """04/07/2020 03:28"""
        nodes = preorder.split(',')
        cnt = 1
        for n in nodes[:-1]:
            if n != '#':
                cnt += 1
            elif n == '#':
                cnt -= 1
            if cnt <= 0:
                return False
        return cnt == 1 and nodes[-1] == '#'

    def isValidSerialization(self, preorder: str) -> bool:
        s = preorder.split(',')
        def consume(i):
            if i >= len(s):
                return float('inf')
            if s[i] == '#':
                return i+1
            return consume(consume(i+1))

        return consume(0) == len(s)


@pytest.mark.parametrize('preorder, expected', [
    ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
    ("1,#", False),
    ("9,#,#,1", False),
    ("1,#,#", True),
    ("1,2,3,4,5,#,#,#,#,#,#", True),
    ("1", False),
    ("#,7,6,9,#,#,#", False)
])
def test(preorder, expected):
    assert expected == Solution().isValidSerialization(preorder)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
