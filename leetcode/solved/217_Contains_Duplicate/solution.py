#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List
import random


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def gen_case():
    n = random.randint(2, 50)
    nums = []
    for i in range(n//5):
        nums.append(random.randint(0, n))
    return nums, len(nums) != len(set(nums))


if __name__ == '__main__':
    cases = [
        ([1,3,4,2,2], 2),
        ([3,1,3,4,2], 3),
        ([4,3,1,4,2], 4),
        ([6,5,4,1,8,3,7,5,2], 5),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case()
    ]
    result = []
    for case, expected in cases:
        print(case, expected)
        actual = Solution().findDuplicate(case)
        ans = expected == actual
        result.append(ans)
        print(f'{ans}\texpected: {expected}\tactual: {actual}')
    if not all(result):
        raise Exception('Wrong')
