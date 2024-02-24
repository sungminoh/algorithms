from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

	For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

	Each element of nums is in exactly one pair, and
	The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.

Example 1:

Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

Example 2:

Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

Constraints:

	n == nums.length
	2 <= n <= 105
	n is even.
	1 <= nums[i] <= 105
"""
import pytest
import sys


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """Feb 24, 2024 13:47"""
        nums.sort()
        return max(nums[len(nums)-1-i] + nums[i] for i in range(len(nums)//2))


@pytest.mark.parametrize('args', [
    (([3,5,2,3], 7)),
    (([3,5,4,2,4,6], 8)),
])
def test(args):
    assert args[-1] == Solution().minPairSum(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
