#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:

	1 <= nums.length <= 15
	-100 <= nums[i] <= 100
"""
from typing import List
import pytest
import sys


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """May 21, 2020 19:36"""
        ret = set()
        def _rec(i, track):
            if i == len(nums):
                if len(track) >= 2:
                    ret.add(tuple(track))
            else:
                _rec(i + 1, track)
                if not track or nums[i] >= track[-1]:
                    _rec(i + 1, track + [nums[i]])

        _rec(0, [])
        return [list(x) for x in ret]

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """Mar 05, 2023 22:45"""
        def dfs(i):
            if i == -1:
                return set()
            ret = dfs(i-1)
            new = set()
            for arr in ret:
                if arr and arr[-1] <= nums[i]:
                    new.add((*arr, nums[i]))
            new.add((nums[i],))
            ret |= new
            return ret

        return [list(x) for x in dfs(len(nums)-1) if len(x) > 1]


@pytest.mark.parametrize('args', [
    (([4,6,7,7], [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]])),
    (([4,4,3,2,1], [[4,4]])),
])
def test(args):
    actual = Solution().findSubsequences(*args[:-1])
    assert sorted(args[-1]) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
