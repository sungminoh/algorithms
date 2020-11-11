#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) == 1:
            return 0
        self.nums = nums
        return self.find_peak_index(0, len(nums)-1)

    def find_peak_index(self, i, j):
        if i == j:
            return i
        m = (i+j)//2
        if self.is_peak(m):
            return m
        elif self.is_asc(m):
            return self.find_peak_index(m+1, j)
        else:
            return self.find_peak_index(i, m)

    def is_peak(self, i):
        return (-float('inf') if i == 0 else self.nums[i-1]) \
            < self.nums[i] \
            > (-float('inf') if i == len(self.nums) else self.nums[i+1])

    def is_asc(self, i):
        return self.nums[i] < self.nums[i+1]


def main():
    nums = [int(x) for x in input().split()]
    print(Solution().findPeakElement(nums))


if __name__ == '__main__':
    main()
