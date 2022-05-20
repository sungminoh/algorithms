#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 109
	1 <= k <= 109
"""
import sys
from collections import defaultdict
from typing import List
import pytest


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ret = 0
        cnt = {}
        for n in nums:
            if cnt.get(k-n, 0) > 0:
                cnt[k-n] -= 1
                ret += 1
            else:
                cnt.setdefault(n, 0)
                cnt[n] += 1
        return ret


@pytest.mark.parametrize('nums, k, expected', [
    ([1,2,3,4], 5, 2),
    ([3,1,3,4,3], 6, 1),
])
def test(nums, k, expected):
    assert expected == Solution().maxOperations(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
