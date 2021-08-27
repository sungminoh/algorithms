#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, handle multiple queries of the following type:

	Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

	NumArray(int[] nums) Initializes the object with the integer array nums.
	int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:

	1 <= nums.length <= 104
	-105 <= nums[i] <= 105
	0 <= left <= right < nums.length
	At most 104 calls will be made to sumRange.
"""
import sys
import itertools
from typing import List
import pytest


class NumArray:
    def __init__(self, nums: List[int]):
        self.cumsum = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right+1] - self.cumsum[left]


@pytest.mark.parametrize('commands, arguments, expecteds', [
    (["NumArray", "sumRange", "sumRange", "sumRange"],
     [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]],
     [None, 1, -1, -3])
])
def test(commands, arguments, expecteds):
    obj = globals()[commands[0]](*arguments[0])
    for cmd, args, exp in zip(commands[1:], arguments[1:], expecteds[1:]):
        assert exp == getattr(obj, cmd)(*args)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
