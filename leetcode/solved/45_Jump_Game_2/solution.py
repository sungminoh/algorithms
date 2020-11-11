#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""


class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        farthest = 0
        previous = 0
        i = 0
        cnt = 0
        while i < len(nums):
            while i <= previous:
                farthest = max(farthest, i + nums[i])
                i += 1
            if farthest <= previous:
                break
            previous = farthest
            cnt += 1
            if farthest >= len(nums)-1:
                return cnt
        return -1

    def _jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        if nums[0]+1 >= len(nums):
            return 1
        memo = [float('inf') for _ in range(len(nums))]
        memo[0] = 0
        m = 1
        for i, n in enumerate(nums):
            for j in range(m, min(len(nums), i+n+1)):
                memo[j] = min(memo[j], memo[i]+1)
            m = max(m, i+n)
        return memo[-1]


def main():
    nums = [int(x) for x in input().split()]
    # nums = eval(open('./test.txt').read())
    print(Solution().jump(nums))


if __name__ == '__main__':
    main()
