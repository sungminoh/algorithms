#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
from typing import List
import random


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev = nums[0]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] == prev:
                cnt += 1
            else:
                prev = nums[i]
                nums[i - cnt], nums[i] = nums[i], nums[i - cnt]
        return len(nums) - cnt


def gen_case():
    ret = []
    for i in range(random.randint(0, 10)):
        for _ in range(random.randint(1, 3)):
            ret.append(i)
    return ret, len(sorted(list(set(ret))))


if __name__ == '__main__':
    cases = [
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),
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
        print(case)
        actual = Solution().removeDuplicates(case)
        ans = expected == actual and case[:actual] == sorted(list(set(case)))
        result.append(ans)
        print(f'{ans}\texpected: {expected}\tactual: {actual}')
    if not all(result):
        raise Exception('Wrong')
