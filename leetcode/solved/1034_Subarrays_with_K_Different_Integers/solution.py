#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

	For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:

	1 <= nums.length <= 2 * 104
	1 <= nums[i], k <= nums.length
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """Apr 28, 2024 18:25"""
        N = len(nums)
        counter = Counter()
        cur = 0
        ret = 0
        j = 0
        for i in range(N):
            counter[nums[i]] += 1
            if len(counter) > k:
                counter[nums[j]] -= 1
                if counter[nums[j]] == 0:
                    counter.pop(nums[j])
                j += 1
                cur = 0
            if len(counter) == k:
                while counter[nums[j]] > 1:
                    counter[nums[j]] -= 1
                    j += 1
                    cur += 1
                ret += cur+1
        return ret


@pytest.mark.parametrize('args', [
    (([1,2,1,2,3], 2, 7)),
    (([1,2,1,3,4], 3, 3)),
])
def test(args):
    assert args[-1] == Solution().subarraysWithKDistinct(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
