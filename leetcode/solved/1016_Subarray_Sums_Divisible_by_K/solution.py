#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:

Input: nums = [5], k = 9
Output: 0

Constraints:

	1 <= nums.length <= 3 * 104
	-104 <= nums[i] <= 104
	2 <= k <= 104
"""
from pathlib import Path
import json
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """Mar 05, 2023 22:16
        TLE
        """
        ret = 0
        sums = defaultdict(int)
        sums[0] += 1
        acc = 0
        for n in nums:
            acc += n
            for s in sums:
                if (acc - s) % k == 0:
                    ret += sums[s]
            sums[acc] += 1
        return ret

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """Mar 05, 2023 22:20"""
        ret = 0
        cnt = [0]*k
        cnt[0] = 1
        acc = 0
        for n in nums:
            acc += n
            ret += cnt[acc % k]
            cnt[acc % k] += 1
        return ret


@pytest.mark.parametrize('args', [
    (([4,5,0,-2,-3,1], 5, 7)),
    (([5], 9, 0)),
    ((*json.load(open(Path(__file__).parent/'testcase.json')), 767481)),
])
def test(args):
    assert args[-1] == Solution().subarraysDivByK(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
