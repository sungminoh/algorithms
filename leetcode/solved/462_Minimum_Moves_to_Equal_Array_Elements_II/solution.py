
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
import sys
from typing import List
import pytest


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        m = nums[len(nums) // 2]
        return sum(abs(n - m) for n in nums)


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], 2),
    ([1,0,0,8,6], 14)
])
def test(nums, expected):
    assert expected == Solution().minMoves2(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
