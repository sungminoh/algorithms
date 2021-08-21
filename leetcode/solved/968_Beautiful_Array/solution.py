#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
An array nums of length n is beautiful if:

	nums is a permutation of the integers in the range [1, n].
	For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].

Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

Example 1:
Input: n = 4
Output: [2,1,4,3]
Example 2:
Input: n = 5
Output: [3,1,2,5,4]

Constraints:

	1 <= n <= 1000
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        @lru_cache(None)
        def rec(n):
            if n == 1:
                return [1]
            return [2*x-1 for x in rec((n+1)//2)] + [2*x for x in rec(n//2)]
        return rec(n)


@pytest.mark.parametrize('n, expected', [
    (4, [2,1,4,3]),
    (5, [3,1,2,5,4]),
])
def test(n, expected):
    arr = Solution().beautifulArray(n)
    for i in range(len(arr)):
        j = i+1
        k = i+2
        while k < len(arr):
            assert arr[i] + arr[k] != 2*arr[j]
            j += 1
            k += 2


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

