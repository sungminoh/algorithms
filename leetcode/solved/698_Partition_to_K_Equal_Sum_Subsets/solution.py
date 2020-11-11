#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

	1 <= k <= len(nums) <= 16.
	0 < nums[i] < 10000.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)
        if r > 0 or q == 0:
            return False

        @lru_cache(None)
        def fill(i, remainders):
            remainders = list(remainders)
            if i == -1:
                return True
            for j in range(len(remainders)):
                if remainders[j] < nums[i]:
                    break
                remainders[j] -= nums[i]
                if fill(i-1, tuple(sorted(remainders, key=lambda x: -x))):
                    return True
                remainders[j] += nums[i]
                if remainders[j] == 0:
                    break
            return False

        nums.sort()
        if nums[-1] > q:
            return False

        while nums and nums[-1] == q:
            nums.pop()
            k -= 1

        return fill(len(nums)-1, tuple([q] * k))


@pytest.mark.parametrize('nums, k, expected', [
    ([4, 3, 2, 3, 5, 2, 1], 4, True),
    ([18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037], 4, True),
    ([2,2,2,2,3,4,5], 4, False)
])
def test(nums, k, expected):
    assert expected == Solution().canPartitionKSubsets(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
