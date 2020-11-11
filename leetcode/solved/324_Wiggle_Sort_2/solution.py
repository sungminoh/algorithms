#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from typing import List
import pytest


def swap(arr, i, j):
    arr[i], arr[j]= arr[j], arr[i]


class Solution:
    cnt = 0
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, e = 0, len(nums) - 1
        k = s + (e - s) // 2
        m = self.find_kth_smallest(nums, 0, e, k)
        # -> 1,3,5,..0,2,4...
        next_idx = lambda i: (2 * i + 1) % (len(nums) | 1)
        i = 0
        while i <= e:
            _i = next_idx(i)
            if nums[_i] > m:
                swap(nums, _i, next_idx(s))
                i += 1
                s += 1
            elif nums[_i] < m:
                swap(nums, _i, next_idx(e))
                e -= 1
            else:
                i += 1
        return nums

    def find_kth_smallest(self, nums, s, e, k):
        self.cnt += 1
        l, r = s, e
        m = nums[k]
        while l < r:
            while l < r and nums[l] < m:
                l += 1
            while l < r and m < nums[r]:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if k > r:
            return self.find_kth_smallest(nums, r + 1, e, k)
        if k < l:
            return self.find_kth_smallest(nums, s, l - 1, k)
        return m


@pytest.mark.parametrize(
    'nums', [
        [1,5,1,1,6,4],
        [1,3,2,2,3,1],
        [1,1,1,2,2,2],
        [1,2,3,9,8,7],
        [1,1,1,1,1,2,2,2,2,2],
        [2,1],
        [4,5,5,6],
        [1,1,2,1,2,2,1],
        [1,1,2,2,2,1],
        [5,3,1,2,6,7,8,5,5]
    ])
def test(nums):
    Solution().wiggleSort(nums)
    wiggled = True
    for i in range(1, len(nums)):
        if i % 2 == 1:
            wiggled &= nums[i-1] < nums[i]
        else:
            wiggled &= nums[i-1] > nums[i]
    print(nums)
    assert wiggled
