#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

	For i <= k < j:

		arr[k] > arr[k + 1] when k is odd, and
		arr[k] < arr[k + 1] when k is even.

	Or, for i <= k < j:

		arr[k] > arr[k + 1] when k is even, and
		arr[k] < arr[k + 1] when k is odd.

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2]  arr[4] < arr[5]

Example 2:

Input: arr = [4,8,12,16]
Output: 2

Example 3:

Input: arr = [100]
Output: 1

Constraints:

	1 <= arr.length <= 4 * 104
	0 <= arr[i] <= 109
"""
import sys
from typing import List
import pytest


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return 1

        ret = 1
        cnt = 1
        grad = 0
        for i in range(1, len(arr)):
            new_grad = 1 if arr[i-1] < arr[i] else -1 if arr[i-1] > arr[i] else 0
            if new_grad == 0:
                cnt = 0
            else:
                if grad == 0:
                    cnt = 2
                else:
                    if new_grad != grad:
                        cnt += 1
                    else:
                        cnt = 2
            ret = max(ret, cnt)
            grad = new_grad

        return ret


@pytest.mark.parametrize('arr, expected', [
    ([9,4,2,10,7,8,8,1,9], 5),
    ([4,8,12,16], 2),
    ([100], 1),
    ([9, 9], 1),
    ([100,100,100], 1),
])
def test(arr, expected):
    assert expected == Solution().maxTurbulenceSize(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
