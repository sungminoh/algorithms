#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums is sorted in a strictly increasing order.
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """08/19/2021 12:17"""
        def to_tree(i, j):
            if j < i:
                return None
            m = i + (j-i)//2
            return TreeNode(nums[m], left=to_tree(i, m-1), right=to_tree(m+1, j))

        return to_tree(0, len(nums)-1)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """08/21/2022 15:11"""
        def build(i, j):
            if j < i:
                return None
            m = i + (j-i)//2
            root = TreeNode(nums[m])
            root.left = build(i, m-1)
            root.right = build(m+1, j)
            return root

        return build(0, len(nums)-1)


def validate(root: Optional[TreeNode]):
    if not root:
        return True, 0
    l, ld = validate(root.left)
    r, rd = validate(root.right)
    return l and r, max(ld, rd)+1


@pytest.mark.parametrize('nums, expected', [
    ([-10,-3,0,5,9], [0,-3,9,-10,None,5]),
    ([1,3], [3,1]),
])
def test(nums, expected):
    root = Solution().sortedArrayToBST(nums)
    assert validate(root)[0]


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
