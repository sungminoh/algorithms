from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

Constraints:

	2 <= nums.length <= 105
	1 <= nums[i] <= nums[i + 1] <= 104
"""
import pytest
import sys


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """Feb 07, 2024 22:30"""
        N = len(nums)
        past = 0
        acc = sum(nums)
        ret = []
        for i, n in enumerate(nums):
            right = acc - n*(N-i)
            left = (n*i) - past
            ret.append(right+left)
            past += n
            acc -= n
        return ret


@pytest.mark.parametrize('args', [
    (([2,3,5], [4,3,5])),
    (([1,4,6,8,10], [24,15,13,15,21])),
])
def test(args):
    assert args[-1] == Solution().getSumAbsoluteDifferences(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
