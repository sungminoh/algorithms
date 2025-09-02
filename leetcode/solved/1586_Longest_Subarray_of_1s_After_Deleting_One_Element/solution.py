#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:

	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
"""
from typing import List
import pytest
import sys


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ret = 0
        pre = 0
        cur = 0
        zero_found = False
        for i, n in enumerate(nums):
            if n == 1:
                cur += 1
            else:
                ret = max(ret, pre + cur)
                pre = cur
                cur = 0
                zero_found = True
        ret = max(ret, cur+pre)
        return ret if zero_found else ret-1


@pytest.mark.parametrize('args', [
    (([1,1,0,1], 3)),
    (([0,1,1,1,0,1,1,0,1], 5)),
    (([1,1,1], 2)),
])
def test(args):
    assert args[-1] == Solution().longestSubarray(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
