#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for n in nums:
            if n > 0 and (s % pow(2, n+1)) // pow(2, n) == 0:
                s += pow(2, n)
        cnt = 0
        s //= 2
        r = 1
        while s and r:
            s, r = divmod(s, 2)
            cnt += 1
        if not s:
            return cnt+1
        return cnt


def main():
    nums = [int(x) for x in input().split()]
    print(Solution().firstMissingPositive(nums))


if __name__ == '__main__':
    main()
