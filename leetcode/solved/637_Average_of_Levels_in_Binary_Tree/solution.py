#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:

	The number of nodes in the tree is in the range [1, 104].
	-231 <= Node.val <= 231 - 1
"""
from typing import List
from typing import Optional
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        q = []
        if root is not None:
            q.append(root)
        while q:
            _q = []
            s = 0
            for n in q:
                s += n.val
                if n.left is not None:
                    _q.append(n.left)
                if n.right is not None:
                    _q.append(n.right)
            ret.append(s/len(q))
            q = _q
        return ret


@pytest.mark.parametrize('values, expected', [
    ([3,9,20,None,None,15,7], [3.00000,14.50000,11.00000]),
    ([3,9,20,15,7], [3.00000,14.50000,11.00000]),
])
def test(values, expected):
    assert expected == Solution().averageOfLevels(build_tree(values))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
