#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List
import random


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k == len(nums):
            return nums

        def swap_circle(nums, i, k):
            m = 0
            tmp = None
            while nums[i] is not None:
                if m == 0 or i < m:
                    m = i
                tmp, nums[i] = nums[i], tmp
                i = (i + k) % len(nums)
            else:
                nums[i] = tmp
            return m

        k = k % len(nums)
        times = swap_circle(nums, 0, k)
        for i in range(1, times):
            swap_circle(nums, i, k)


def gen_case():
    size = random.randint(0, 20)
    nums = list(range(size))
    random.shuffle(nums)
    k = random.randint(0, 20)
    fivot = k % len(nums)
    answer = nums[-fivot:] + nums[:-fivot]
    return (nums, k), answer


if __name__ == '__main__':
    cases = [
        (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4]),
        (([-1,-100,3,99], 2), [3,99,-1,-100]),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case()
    ]
    result = []
    for case, expected in cases:
        print(case, expected)
        Solution().rotate(*case)
        ans = expected == case
        result.append(ans)
        print(f'{ans}\texpected: {expected}\tactual: {case}')
    if not all(result):
        raise Exception('Wrong')
