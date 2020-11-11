#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
81. Search in Rotated Sorted Array II
DescriptionHintsSubmissionsDiscussSolution
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def bisearch(ns, t):
            i, j = 0, len(nums)-1
            while i <= j:
                m = (i+j)//2
                if ns[m] > t:
                    j = m-1
                elif ns[m] < t:
                    i = m+1
                else:
                    return True
            return False

        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        p = len(nums)-1
        while p >= 0 and nums[p-1] <= nums[p]:
            p -= 1
        return bisearch(nums[p:] + nums[:p], target)


def main():
    nums = [int(x) for x in input()]
    print(Solution().search(nums, int(input())))


if __name__ == '__main__':
    main()
