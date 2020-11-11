#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        count1, count2 = 0, 0
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1 = n
                count1 = 1
            elif count2 == 0:
                num2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1

        ret = []
        if count1 > len(nums) // 3:
            ret.append(num1)
        if count2 > len(nums) // 3:
            ret.append(num2)
        return ret


if __name__ == '__main__':
    cases = [
        ([3,2,3], [3]),
        ([1,1,1,3,3,2,2,2], [1,2]),
        ([1,2,2,3,2,1,1,3], [2,1]),
        ([1,2], [1,2])
    ]
    for case, expected in cases:
        actual = Solution().majorityElement(case)
        print(f'{expected == actual}\texpected: {expected}\tactual: {actual}')
