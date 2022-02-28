#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
	All the numbers of nums are unique.
"""
import sys
from typing import List
import pytest


class Solution:
    def subsets(self, nums):
        """04/28/2018 06:23"""
        ret = [[]]
        for n in nums:
            new = []
            for s in ret:
                new.append(s + [n])
            ret.extend(new)
        return ret

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            for i in range(len(ret)):
                ret.append(ret[i] + [n])
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[],[0]]),
])
def test(nums, expected):
    assert sorted(expected) == sorted(Solution().subsets(nums))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
