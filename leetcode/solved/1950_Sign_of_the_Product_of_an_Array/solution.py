import functools
import itertools
import operator
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a function signFunc(x) that returns:

	1 if x is positive.
	-1 if x is negative.
	0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:

	1 <= nums.length <= 1000
	-100 <= nums[i] <= 100
"""
import pytest
import sys


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """Sep 09, 2023 21:27"""
        signfunc = lambda x: max(min(1, x), -1)
        return functools.reduce(operator.mul, (signfunc(x) for x in nums))


@pytest.mark.parametrize('args', [
    (([-1,-2,-3,-4,3,2,1], 1)),
    (([1,5,0,2,-3], 0)),
    (([-1,1,-1,1,-1], -1)),
    (([-5], -1)),
])
def test(args):
    assert args[-1] == Solution().arraySign(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
