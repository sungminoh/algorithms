#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""
import math


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])

        max_n = max(nums)
        min_n = min(nums)
        size = math.ceil((max_n - min_n + 1) / (len(nums) - 1))

        if size == 0:
            return 0

        buckets = [[] for _ in range(len(nums)-1)]
        for num in nums:
            n = num - min_n
            buckets[n // size].append(n)

        ret = 0
        e = 0
        for bucket in buckets:
            if not bucket:
                continue
            s = min(bucket)
            ret = max(ret, s-e)
            e = max(bucket)
        return ret


def main():
    inputs = []
    inputs.append(([3, 6, 9, 1], 3))
    inputs.append(([10], 0))

    from random import randint
    for i in range(10):
        length = randint(1, 100)
        nums = [randint(0, length * 100) for _ in range(length)]
        snums = sorted(nums)
        sol = max([snums[i + 1] - snums[i] for i in range(len(nums) - 1)]) if len(nums) > 1 else 0
        inputs.append((nums, sol))

    for nums, sol in inputs:
        ans = Solution().maximumGap(nums)
        print('%s\tAnswer:%s\tExpected:%s' % (ans == sol, ans, sol))
        if ans != sol:
            print(nums)
            print(sorted(nums))



if __name__ == '__main__':
    main()
