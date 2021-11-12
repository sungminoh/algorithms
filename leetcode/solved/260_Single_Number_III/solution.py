#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]

Constraints:

	2 <= nums.length <= 3 * 104
	-231 <= nums[i] <= 231 - 1
	Each integer in nums will appear twice, only two integers will appear once.
"""
import math
import sys
from typing import List
import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """03/28/2020 17:10"""
        xor = 0
        for n in nums:
            xor ^= n
        if xor == 0:
            return []
        rightmost_positive_bid_index = math.log2(xor & -xor)
        m = int(math.pow(2, rightmost_positive_bid_index))
        xors = [0, 0]
        for n in nums:
            xors[min(1, n & m)] ^= n
        return sorted(xors)

    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)

    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n

        lsb = xor & -xor
        ret = [0, 0]
        for n in nums:
            ret[min(1, lsb & n)] ^= n
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([1,2,1,3,2,5], [3,5]),
    ([-1,0], [-1,0]),
    ([0,1], [1,0]),
])
def test(nums, expected):
    assert sorted(expected) == sorted(Solution().singleNumber(nums))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
