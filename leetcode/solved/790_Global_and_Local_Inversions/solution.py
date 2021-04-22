#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

	0 <= i < j < n
	nums[i] > nums[j]

The number of local inversions is the number of indices i where:

	0 <= i < n - 1
	nums[i] > nums[i + 1]

Return true if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.

Example 2:

Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.

Constraints:

	n == nums.length
	1 <= n <= 5000
	0 <= nums[i] < n
	All the integers of nums are unique.
	nums is a permutation of all the numbers in the range [0, n - 1].
"""
import sys
from typing import List
import pytest


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        There shouldn't be any non-local inversion
        When the maximum so far is larger than num[i+2],
        it geneartes non-local inversion.
        """
        m = -float('inf')
        for i in range(len(nums)-2):
            m = max(m, nums[i])
            if nums[i+2] < m:
                return False
        return True

    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        There shouldn't be any non-local inversion
        When the current value is not index-1 or index+1,
        there must be a non-local inversion
        """
        return all(abs(n-i) <= 1 for i, n in enumerate(nums))


@pytest.mark.parametrize('nums, expected', [
    ([1,0,2], True),
    ([1,2,0], False),
    ([2,1,0], False),
])
def test(nums, expected):
    assert expected == Solution().isIdealPermutation(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
