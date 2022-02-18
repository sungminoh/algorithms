#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:

	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
"""
from pathlib import Path
import json
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """TLE 05/31/2020 19:58"""
        counts = [[0], [0]]
        for i, n in enumerate(nums):
            if i == 0:
                counts[n].append(1)
                counts[(n+1)%2].append(0)
            else:
                counts[n].append(counts[n][-1] + 1)
                counts[(n+1)%2].append(counts[(n+1)%2][-1])
        m = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if counts[1][j+1] - counts[1][i] == counts[0][j+1] - counts[0][i]:
                    m = max(m, j - i + 1)
                    break
        return m

    def findMaxLength(self, nums: List[int]) -> int:
        sign = [-1, 1]
        memo = {0: -1}
        water_mark = 0
        m = 0
        for i, n in enumerate(nums):
            water_mark = water_mark + sign[n]
            if water_mark in memo:
                m = max(m, i - memo[water_mark])
            else:
                memo[water_mark] = i
        return m

    def findMaxLength(self, nums: List[int]) -> int:
        memo = {0: -1}
        s = 0
        ret = 0
        for i, n in enumerate(nums):
            s += (-1, 1)[n]
            if s in memo:
                ret = max(ret, i-memo[s])
            else:
                memo[s] = i
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([0,1], 2),
    ([0,1,0], 2),
    (json.load(open(f'{Path(__file__).parent}/testcase.json', 'r')), 44578),
])
def test(nums, expected):
    assert expected == Solution().findMaxLength(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
