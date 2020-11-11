
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Constraints:
	1. The length of the array is in range [1, 20,000].
	2. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
from collections import defaultdict
from itertools import accumulate
from pathlib import Path
import json
import sys
from typing import List
import pytest


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        cnt = 0
        for s in accumulate(nums):
            if s - k in memo:
                cnt += memo[s - k]
            memo[s] += 1
        return cnt


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
    ([1], 0, 0),
    ([1], 1, 1),
    ([-1,-1,1], 0, 1),
    (json.load(open(Path(__file__).parent/'testcase.json')), -682, 4012)
])
def test(nums, k, expected):
    assert expected == Solution().subarraySum(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
