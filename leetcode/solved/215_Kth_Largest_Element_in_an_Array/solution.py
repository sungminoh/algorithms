#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.<Paste>
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        n = nums[-1]
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] < n < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] >= n:
                i += 1
            if nums[j] <= n:
                j -= 1
        nums[j + 1], nums[-1] = n, nums[j + 1]
        if k - 1 < j + 1:
            return self.findKthLargest(nums[:j + 1], k)
        elif k - 1 > j + 1:
            return self.findKthLargest(nums[j + 2:], k - j - 2)
        else:
            return nums[k - 1]


# exercise
def quick_sort(nums):
    def __quick_sort(s, e):
        if e >= len(nums) or s > e:
            return
        n = nums[e]
        i, j = s, e - 1
        while i <= j:
            if nums[i] > n > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] <= n:
                i += 1
            if nums[j] >= n:
                j -= 1
        nums[j + 1], nums[e] = n, nums[j + 1]
        __quick_sort(s, j)
        __quick_sort(j + 2, e)
    __quick_sort(0, len(nums) - 1)
    return nums


if __name__ == '__main__':
    cases = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4),
        ([1,2,3,4,5,6,7], 4)
    ]
    expecteds = [
        5,
        4,
        4
    ]
    for (nums, k), expected in zip(cases, expecteds):
        actual = Solution().findKthLargest(nums, k)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
