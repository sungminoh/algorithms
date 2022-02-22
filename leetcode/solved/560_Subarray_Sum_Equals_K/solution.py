#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

	1 <= nums.length <= 2 * 104
	-1000 <= nums[i] <= 1000
	-107 <= k <= 107
"""
from itertools import accumulate
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """06/12/2020 00:04"""
        memo = defaultdict(int)
        memo[0] = 1
        cnt = 0
        for s in accumulate(nums):
            if s - k in memo:
                cnt += memo[s - k]
            memo[s] += 1
        return cnt

    def subarraySum(self, nums: List[int], k: int) -> int:
        acc_cnt = defaultdict(int)
        acc_cnt[0] = 1
        acc = 0
        ret = 0
        for n in nums:
            acc += n
            if acc-k in acc_cnt:
                ret += acc_cnt[acc-k]
            acc_cnt[acc] += 1
        return ret


@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,1], 2, 2),
    ([1,2,3], 3, 2),
])
def test(nums, k, expected):
    assert expected == Solution().subarraySum(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
