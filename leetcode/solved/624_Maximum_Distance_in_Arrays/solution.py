#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:

Input: arrays = [[1],[1]]
Output: 0

Constraints:

	m == arrays.length
	2 <= m <= 105
	1 <= arrays[i].length <= 500
	-104 <= arrays[i][j] <= 104
	arrays[i] is sorted in ascending order.
	There will be at most 105 integers in all the arrays.
"""
from typing import List
import pytest
import sys


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        """Nov 06, 2024 15:56"""
        values = []
        for i, arr in enumerate(arrays):
            values.extend([(min(arr), i), (max(arr), i)])
        values.sort()

        def dp(i, j):
            if i >= j:
                return 0
            mn = values[i]
            mx = values[j]
            if mn[1] != mx[1]:
                return mx[0] - mn[0]
            return max(dp(i+1, j), dp(i, j-1))

        return dp(0, len(values)-1)

    def maxDistance(self, arrays: List[List[int]]) -> int:
        """Nov 06, 2024 15:59"""
        mn, mx = arrays[0][0], arrays[0][-1]
        ret = 0
        for i in range(1, len(arrays)):
            ret = max(
                ret,
                abs(mx - arrays[i][0]),
                abs(arrays[i][-1] - mn))
            mx = max(mx, arrays[i][-1])
            mn = min(mn, arrays[i][0])
        return ret


@pytest.mark.parametrize('args', [
    (([[1,2,3],[4,5],[1,2,3]], 4)),
    (([[1],[1]], 0)),
    (([[1,5],[3,4]], 3)),
])
def test(args):
    assert args[-1] == Solution().maxDistance(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
