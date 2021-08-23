#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:

	1 <= nums.length <= 10
	-10 <= nums[i] <= 10
"""
import sys
from typing import List
import pytest


class Solution:
    def subsetsWithDup(self, nums):
        """05/04/2018 22:44"""
        if not nums:
            return [[]]
        nums.sort()
        nums.append(None)
        ret = []
        n = 0
        for i in range(0, len(nums)-1):
            n += 1
            if nums[i] != nums[i+1]:
                tmp = [[nums[i]] * j for j in range(1, n+1)]
                add = [s + t for s in ret for t in tmp] + tmp
                ret.extend(add)
                n = 0
        ret.append([])
        return ret

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set([tuple()])
        for n in sorted(nums):
            new = []
            for arr in ret:
                new.append((*arr, n))
            ret.update(new)
        return [list(x) for x in ret]


@pytest.mark.parametrize('nums, expected', [
    ([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
    ([0], [[],[0]]),
    ([4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])
])
def test(nums, expected):
    actual = Solution().subsetsWithDup(nums)
    print()
    print(sorted(expected))
    print(sorted(actual))
    assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
