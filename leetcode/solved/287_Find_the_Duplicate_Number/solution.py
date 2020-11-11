#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
import random
from typing import List


class Solution:
    def _findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l <= r:
            k = l + (r - l) // 2
            smaller = 0
            larger = 0
            found = False
            for n in nums:
                if n > r or n < l:
                    continue
                if n < k:
                    smaller += 1
                elif n > k:
                    larger += 1
                elif found:
                    return k
                else:
                    found = True
            if smaller < larger:
                l = k + 1
            else:
                r = k - 1
        return -1

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


def gen_case():
    n = random.randint(2, 10)
    nums = list(range(1, n + 1))
    duplicate = random.randint(1, n - 1)
    nums[-1] = duplicate
    random.shuffle(nums)
    return nums, duplicate


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
