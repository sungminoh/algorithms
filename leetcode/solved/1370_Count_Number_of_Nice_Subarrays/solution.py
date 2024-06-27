#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

	1 <= nums.length <= 50000
	1 <= nums[i] <= 10^5
	1 <= k <= nums.length
"""
from typing import List
import pytest
import sys


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """Jun 26, 2024 23:50"""
        odd_pos = [-1]
        for i, n in enumerate(nums):
            if n%2 != 0:
                odd_pos.append(i)
        odd_pos.append(len(nums))
        ret = 0
        for j in range(k, len(odd_pos)-1):
            i = j-k+1
            l = odd_pos[i] - odd_pos[i-1]
            r = odd_pos[j+1] - odd_pos[j]
            ret += l*r
        return ret


@pytest.mark.parametrize('args', [
    (([1,1,2,1,1], 3, 2)),
    (([2,4,6], 1, 0)),
    (([2,2,2,1,2,2,1,2,2,2], 2, 16)),
])
def test(args):
    assert args[-1] == Solution().numberOfSubarrays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
