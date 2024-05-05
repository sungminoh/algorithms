#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

	arr.length >= 3
	There exists some i with 0 < i < arr.length - 1 such that:

		arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
		arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

	MountainArray.get(k) returns the element of the array at index k (0-indexed).
	MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:

	3 <= mountain_arr.length() <= 104
	0 <= target <= 109
	0 <= mountain_arr.get(index) <= 109
"""
import pytest
import sys


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """May 04, 2024 14:33"""
        def bisearch(i, j, key):
            while i <= j:
                m = i + (j-i)//2
                if key(m):
                    i = m+1
                else:
                    j = m-1
            return j+1

        N = mountain_arr.length()
        def is_increasing(i):
            return (i == 0 or mountain_arr.get(i-1) < mountain_arr.get(i)) \
                and (i == N-1 or mountain_arr.get(i) < mountain_arr.get(i+1))

        peak = bisearch(0, N-1, key=is_increasing)

        i = bisearch(0, peak, key=lambda i: mountain_arr.get(i) < target)
        if i < N and mountain_arr.get(i) == target:
            return i
        i = bisearch(peak, N-1, key=lambda i: mountain_arr.get(i) > target)
        if i < N and mountain_arr.get(i) == target:
            return i
        return -1


@pytest.mark.parametrize('args', [
    (([1,2,3,4,5,3,1], 3, 2)),
    (([0,1,2,4,2,1], 3, -1)),
])
def test(args):
    assert args[-1] == Solution().findInMountainArray(args[1], MountainArray(args[0]))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
