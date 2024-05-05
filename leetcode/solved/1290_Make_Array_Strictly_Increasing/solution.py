#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.

Constraints:

	1 <= arr1.length, arr2.length <= 2000
	0 <= arr1[i], arr2[i] <= 10^9
"""
from functools import lru_cache
import bisect
from typing import List
import pytest
import sys


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """May 04, 2024 20:18"""
        arr2.sort()

        @lru_cache(None)
        def dp(i, p):
            if i == len(arr1):
                return 0
            ret = float('inf')
            if p < arr1[i]:
                ret = min(ret, dp(i+1, arr1[i]))
            j = bisect.bisect_right(arr2, p)
            if 0<=j<len(arr2):
                ret = min(ret, 1 + dp(i+1, arr2[j]))
            return ret

        ret = dp(0, -1)
        return ret if ret < float('inf') else -1


@pytest.mark.parametrize('args', [
    (([1,5,3,6,7], [1,3,2,4], 1)),
    (([1,5,3,6,7], [4,3,1], 2)),
    (([1,5,3,6,7], [1,6,3,3], -1)),
])
def test(args):
    assert args[-1] == Solution().makeArrayIncreasing(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
