#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, return the number of AND triples.

An AND triple is a triple of indices (i, j, k) such that:

	0 <= i < nums.length
	0 <= j < nums.length
	0 <= k < nums.length
	nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.

Example 1:

Input: nums = [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

Example 2:

Input: nums = [0,0,0]
Output: 27

Constraints:

	1 <= nums.length <= 1000
	0 <= nums[i] < 216
"""
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """Apr 28, 2024 17:54"""
        N = len(nums)
        two_and = Counter([nums[i] & nums[j] for i in range(N) for j in range(N)])
        ret = 0
        for i in range(N):
            for k, v in two_and.items():
                if k & nums[i] == 0:
                    ret += v
        return ret


@pytest.mark.parametrize('args', [
    (([2,1,3], 12)),
    (([0,0,0], 27)),
])
def test(args):
    assert args[-1] == Solution().countTriplets(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
