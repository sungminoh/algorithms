#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:

Input: arr = [10,11,12]
Output: 66

Constraints:

	1 <= arr.length <= 100
	1 <= arr[i] <= 1000
"""
import sys
from typing import List
import pytest


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)

        For an ith element,
        If the number of elements between start of a subarray and i is even,
        the number of elements between i+1 to end of the subarray must be odd
        and vice versa.

        Start index is in [1, i]
        End index is in [i, n]
        """
        s = 0
        for i, n in enumerate(arr, 1):
            n_start_odd_left = (i+1)//2
            n_start_even_left = i - n_start_odd_left
            n_end_even_right = (len(arr)-i+2)//2
            n_end_odd_right = len(arr)-i+1 - n_end_even_right
            s += n * ((n_start_odd_left * n_end_even_right) + (n_start_even_left * n_end_odd_right))

        return s


@pytest.mark.parametrize('arr, expected', [
    ([1,4,2,5,3], 58),
    ([1,2], 3),
    ([10,11,12], 66),
])
def test(arr, expected):
    assert expected == Solution().sumOddLengthSubarrays(arr)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
