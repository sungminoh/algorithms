#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

	1 <= nums.length <= 200
	1 <= nums[i] <= 1000
	All the elements of nums are unique.
	1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """04/12/2020 22:17"""
        @lru_cache(None)
        def _rec(target):
            if target <= 0:
                return 1 if target == 0 else 0
            return sum(_rec(target - n) for n in nums)

        return _rec(target)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """08/15/2022 10:05"""
        @lru_cache(None)
        def dfs(t):
            if t == 0:
                return 1
            return sum(dfs(t-n) for n in nums if n <= t)

        return dfs(target)


@pytest.mark.parametrize('nums, target, expected', [
    ([1,2,3], 4, 7),
    ([9], 3, 0),
    ([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111], 999, 1)
])
def test(nums, target, expected):
    assert expected == Solution().combinationSum4(nums, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
