import math
import itertools
from functools import lru_cache
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

	Choose two elements, x and y.
	Receive a score of i * gcd(x, y).
	Remove x and y from nums.

Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

Constraints:

	1 <= n <= 7
	nums.length == 2 * n
	1 <= nums[i] <= 106
"""
import pytest
import sys


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """TLE"""
        @lru_cache(None)
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd((a-b)%b, b)

        def iter_cases(used=0):
            # i = 0
            # while i < len(nums) and used&(1<<i):
            #     i += 1
            if used == 2**(len(nums)-1)-1:
                return []
            i = int(math.log2(((used+1)^used)+1)-1)
            used |= (1<<i)
            for j in range(i+1, len(nums)):
                if used&(1<<j):
                    continue
                used |= (1<<j)
                for pairs in iter_cases(used):
                    yield itertools.chain([(i, j)], pairs)
                used ^= (1<<j)
            yield []

        ret = 0
        for pairs in iter_cases():
            gcds = sorted([gcd(nums[p], nums[q]) for p, q in pairs])
            ret = max(ret, sum(i*n for i, n in enumerate(gcds, 1)))
        return ret

    def maxScore(self, nums: List[int]) -> int:
        """Sep 22, 2023 13:48"""
        @lru_cache(None)
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd((a-b)%b, b)

        @lru_cache(None)
        def dp(i, used=0):
            if i > len(nums)//2:
                return 0
            ret = 0
            for x in range(len(nums)):
                if used&(1<<x):
                    continue
                for y in range(x+1, len(nums)):
                    if used&(1<<y):
                        continue
                    ret = max(ret, i*gcd(nums[x], nums[y]) + dp(i+1, used|(1<<x)|(1<<y)))
            return ret

        return dp(1)


@pytest.mark.parametrize('args', [
    (([1,2], 1)),
    (([3,4,6,8], 11)),
    (([1,2,3,4,5,6], 14)),
    (([773274,313112,131789,222437,918065,49745,321270,74163,900218,80160,325440,961730], 3032)),
    (([865,195,397,452,154,628,936,402,596,242,10,699,195,595], 1564)),
    (([896,72,970,78,753,457,729,417,903,431,50,969,688,948], 449)),
])
def test(args):
    assert args[-1] == Solution().maxScore(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
