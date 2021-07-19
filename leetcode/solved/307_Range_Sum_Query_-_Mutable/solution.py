#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, handle multiple queries of the following types:

	Update the value of an element in nums.
	Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

	NumArray(int[] nums) Initializes the object with the integer array nums.
	void update(int index, int val) Updates the value of nums[index] to be val.
	int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:

	1 <= nums.length <= 3 * 104
	-100 <= nums[i] <= 100
	0 <= index < nums.length
	-100 <= val <= 100
	0 <= left <= right < nums.length
	At most 3 * 104 calls will be made to update and sumRange.
"""
import sys
import math
from typing import List
import pytest


class NumArray:
    """Segment tree"""
    def __init__(self, nums: List[int]):
        self.size = len(nums)

        def build(l, r):
            if l == r:
                return [nums[l], None, None]
            m = l + (r-l)//2
            left = build(l, m)
            right = build(m+1, r)
            return [left[0] + right[0], left, right]

        self.tree = build(0, self.size-1)

    def update(self, index: int, val: int) -> None:
        def change_val(l, r, node):
            nval, lnode, rnode = node
            if l == r == index:
                diff = val - nval
            else:
                m = l + (r-l)//2
                if index <= m:
                    diff = change_val(l, m, lnode)
                else:
                    diff = change_val(m+1, r, rnode)
            node[0] += diff
            return diff

        change_val(0, self.size-1, self.tree)

    def sumRange(self, left: int, right: int) -> int:
        def query(l, r, left, right, node):
            nval, lnode, rnode = node
            if l == left and r == right:
                return nval
            m = l + (r-l)//2
            if right <= m:
                return query(l, m, left, right, lnode)
            if left > m:
                return query(m+1, r, left, right, rnode)
            return query(l, m, left, m, lnode) + query(m+1, r, m+1, right, rnode)

        return query(0, self.size-1, left, right, self.tree)



@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["NumArray", "sumRange", "update", "sumRange"],
     [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
     [None, 9, None, 8]),
])
def test(commands, arguments, expecteds):
    obj = globals()[commands[0]](*arguments[0])
    for cmd, args, exps in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exps == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
