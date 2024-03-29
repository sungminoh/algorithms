#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

	For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

	For example, the next permutation of arr = [1,2,3] is [1,3,2].
	Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
	While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:

	1 <= nums.length <= 100
	0 <= nums[i] <= 100
"""
import sys
import random
from typing import List
import pytest


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quick_sort(arr, i, j):
            if i >= j:
                return
            m = random.randint(i, j)
            arr[j], arr[m] = arr[m], arr[j]
            l, r = i, j-1
            while l <= r:
                if arr[l] > arr[j]:
                    arr[l], arr[r] = arr[r], arr[l]
                    r -= 1
                else:
                    l += 1
            arr[l], arr[j] = arr[j], arr[l]
            quick_sort(arr, i, l-1)
            quick_sort(arr, l+1, j)

        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def bisearch(arr, l, r, x):
            while l <= r:
                m = l + (r-l)//2
                if arr[m] > x:
                    l = m+1
                else:
                    r = m-1
            return r

        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                j = bisearch(nums, i, len(nums)-1, nums[i-1])
                nums[i-1], nums[j] = nums[j], nums[i-1]
                # quick_sort(nums, i, len(nums)-1)
                reverse(nums, i, len(nums)-1)
                return
        nums.sort()
        return


@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [1,3,2]),
    ([3,2,1], [1,2,3]),
    ([1,1,5], [1,5,1]),
    ([1,3,2], [2,1,3]),
    ([1,5,1], [5,1,1]),
    ([5,4,7,5,3,2], [5,5,2,3,4,7])
])
def test(nums, expected):
    Solution().nextPermutation(nums)
    assert expected == nums


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
