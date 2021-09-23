#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

	The first element in s[k] starts with the selection of the element nums[k] of index = k.
	The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
	We stop adding right before a duplicate element occurs in s[k].

Return the longest length of a set s[k].

Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation:
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

Example 2:

Input: nums = [0,1,2]
Output: 1

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] < nums.length
	All the values of nums are unique.
"""
import sys
from typing import List
import pytest


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """06/12/2020 00:17"""
        pool = set(nums)

        def iterate(n):
            cnt = 0
            while n in pool:
                pool.remove(n)
                cnt += 1
                n = nums[n]
            return cnt

        m = 1
        for n in nums:
            m = max(m, iterate(n))
        return m

    def arrayNesting(self, nums: List[int]) -> int:
        used = set()

        def loop(n):
            used.add(n)
            if nums[n] not in used:
                return 1 + loop(nums[n])
            return 1

        ret = 0
        for i in range(len(nums)):
            if i not in used:
                ret = max(ret, loop(i))
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([5,4,0,3,1,6,2], 4),
    ([0,1,2], 1),
])
def test(nums, expected):
    assert expected == Solution().arrayNesting(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
