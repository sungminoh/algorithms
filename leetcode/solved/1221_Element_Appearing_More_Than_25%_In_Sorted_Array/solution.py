from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

Constraints:

	1 <= arr.length <= 104
	0 <= arr[i] <= 105
"""
import pytest
import sys


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """Feb 03, 2024 18:07"""
        t = len(arr)/4
        i = 0
        while i < len(arr):
            j = i
            while j < len(arr) and arr[i] == arr[j]:
                j += 1
            if j-i > t:
                return arr[i]
            i = j


@pytest.mark.parametrize('args', [
    (([1,2,2,6,6,6,6,7,10], 6)),
    (([1,1], 1)),
])
def test(args):
    assert args[-1] == Solution().findSpecialInteger(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
