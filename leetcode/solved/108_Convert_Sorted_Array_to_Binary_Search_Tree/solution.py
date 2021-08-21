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
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:

	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums is sorted in a strictly increasing order.
"""
from pathlib import Path
from typing import Optional
from typing import List
import pytest
import sys
sys.path.append(str(Path('__file__').absolute().parent.parent))
from exercise.tree import TreeNode, build_tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def to_tree(i, j):
            if j < i:
                return None
            m = i + (j-i)//2
            return TreeNode(nums[m], left=to_tree(i, m-1), right=to_tree(m+1, j))

        return to_tree(0, len(nums)-1)


def is_balanced(tree):
    def get_depth(root):
        if not root:
            return 0
        return max(get_depth(root.left), get_depth(root.right)) + 1
    return abs(get_depth(tree.left) - get_depth(tree.right)) <= 1


@pytest.mark.parametrize('nums, expected', [
    ([-10,-3,0,5,9], [0,-3,9,-10,None,5]),
    ([1,3], [3,1]),
])
def test(nums, expected):
    tree = Solution().sortedArrayToBST(nums)
    print()
    print(tree)
    assert is_balanced(tree)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
