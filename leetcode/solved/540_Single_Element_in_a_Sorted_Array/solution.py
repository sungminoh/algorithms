#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 105
"""
import random
import sys
from typing import List
import pytest


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """06/03/2020 21:59"""
        i, j = 0, len(nums) - 1
        while i < j:
            m = i + (j-i)//2  # 2k or 2k+1
            e = 2 * (m // 2)
            o = e + 1
            if nums[e] == nums[o]:
                i = o + 1
            else:
                j = e - 1
        return nums[i]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        s, e = 0, (len(nums)+1)//2 - 1
        while s <= e:
            m = s + (e-s)//2
            if 2*m == len(nums)-1:
                return nums[2*m]
            elif nums[2*m] == nums[2*m+1]:
                s = m+1
            elif nums[2*m] != nums[2*m-1]:
                return nums[2*m]
            else:
                e = m-1
        return nums[s]

    def singleNonDuplicate(self, nums: List[int]) -> int:
        s, e = 0, (len(nums)+1)//2 - 1
        while s < e:
            m = s + (e-s)//2
            if nums[2*m] == nums[2*m+1]:
                s = m+1
            else:
                e = m
        return nums[2*s]



def gen_case():
    n = random.randint(1, 10)
    m = random.randrange(0, n)
    ret = []
    for i in range(n):
        ret.append(i)
        if i != m:
            ret.append(i)
    return ret, m


@pytest.mark.parametrize('nums, expected', [
    ([1,1,2,3,3,4,4,8,8], 2),
    ([3,3,7,7,10,11,11], 10),
    ([0, 0, 1], 1),
    ([0, 0, 1, 2, 2], 1),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
])
def test(nums, expected):
    print(nums, expected)
    assert expected == Solution().singleNonDuplicate(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
