#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

	arr.length >= 3
	There exists some i with 0 < i < arr.length - 1 such that:

		arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
		arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false
Example 2:
Input: arr = [3,5,5]
Output: false
Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:

	1 <= arr.length <= 104
	0 <= arr[i] <= 104
"""
import sys
from typing import List
import pytest


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        pass_peak = False
        for i in range(1, len(arr)-1):
            is_peak = not pass_peak and (arr[i-1] < arr[i] > arr[i+1])
            if is_peak:
                pass_peak = True
            else:
                up = arr[i-1] < arr[i] < arr[i+1]
                down = arr[i-1] > arr[i] > arr[i+1]
                if (not pass_peak and not up)\
                        or (pass_peak and not down):
                    return False
        return pass_peak


@pytest.mark.parametrize('arr, expected', [
    ([2,1], False),
    ([3,5,5], False),
    ([0,3,2,1], True),
    ([0,1,2,3,4,5,6,7,8,9], False),
    ([9,8,7,6,5,4,3,2,1,0], False),
])
def test(arr, expected):
    assert expected == Solution().validMountainArray(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
