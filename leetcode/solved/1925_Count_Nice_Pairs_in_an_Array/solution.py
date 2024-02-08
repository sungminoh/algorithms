from collections import defaultdict
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

	0 <= i < j < nums.length
	nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 109
"""
import pytest
import sys


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """Feb 07, 2024 21:45"""
        def rev(n):
            ret = 0
            while n:
                ret *= 10
                n, r = divmod(n, 10)
                ret += r
            return ret

        group = defaultdict(set)
        for i, (r, n) in enumerate(zip([rev(n) for n in nums], nums)):
            group[n-r].add(i)

        return sum(len(g)*(len(g)-1)//2 for g in group.values()) % int(1e9+7)


@pytest.mark.parametrize('args', [
    (([42,11,1,97], 2)),
    (([13,10,35,24,76], 4)),
])
def test(args):
    assert args[-1] == Solution().countNicePairs(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
