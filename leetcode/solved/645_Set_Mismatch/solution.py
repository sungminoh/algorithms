#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:

	2 <= nums.length <= 104
	1 <= nums[i] <= 104
"""
import math
from typing import List
import pytest
import sys


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """11/06/2022 14:11"""
        exists = 0
        appeared = 0
        for n in nums:
            exists ^= 1<<(n-1)
            appeared |= 1<<(n-1)
        ret = [None, None]
        for i in range(len(nums)):
            if exists % 2 == 0:
                ret[0 if appeared&(1<<i) else 1] = i+1
            exists >>= 1
            i += 1
        return ret

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Feb 01, 2024 19:04"""
        bit = 0
        ret = []
        for n in nums:
            if 1<<(n-1) & bit:
                ret.append(n)
            bit |= 1<<(n-1)
        # not get the index of zero
        bit += 1
        ret.append(int(math.log2(~(bit-1) & bit))+1)
        return sorted(ret)


@pytest.mark.parametrize('args', [
    (([1,2,2,4], [2,3])),
    (([1,1], [1,2])),
    (([2,2], [2,1])),
])
def test(args):
    assert args[-1] == Solution().findErrorNums(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
