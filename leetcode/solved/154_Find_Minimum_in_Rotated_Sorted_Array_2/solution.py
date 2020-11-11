#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
"""


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return min(nums)
        m = len(nums)//2
        if nums[m] > nums[-1]:
            return self.findMin(nums[m+1:])
        elif nums[m] < nums[-1]:
            return self.findMin(nums[:m+1])
        else:
            if nums[0] < nums[m]:
                return nums[0]
            elif nums[0] > nums[m]:
                return self.findMin(nums[:m+1])
            else:
                if len(set(nums[m:])) == 1:
                    return self.findMin(nums[:m+1])
                else:
                    return self.findMin(nums[m+1:])


def main():
    inputs = []
    inputs.append(([1,3,5], 1))
    inputs.append(([2,2,2,0,1], 0))
    for nums, sol in inputs:
        ans = Solution().findMin(nums)
        print('%s\tActual:%s\tExpected:%s' % (ans == sol, ans, sol))


if __name__ == '__main__':
    main()
