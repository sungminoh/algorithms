
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

	The length of the given array will not exceed 15.
	The range of integer in the given array is [-100,100].
	The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""
import sys
from typing import List
import pytest


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
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


@pytest.mark.parametrize('nums, expected', [
    ([4,6,7,7], [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]])
])
def test(nums, expected):
    assert set(tuple(x) for x in expected) == set(tuple(x) for x in Solution().findSubsequences(nums))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
