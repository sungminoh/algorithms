#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List
import random


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            ret ^= n
        return ret


def gen_case():
    n = 10
    pool = list(range(1, n + 1))  # [1,2,3,4,...,n]
    duplicates = []
    # num_duplicates = random.randint(0, n)  # [0...n]
    # num_uniques = n - num_duplicates
    num_duplicates = n - 1
    num_uniques = 1
    for i in range(num_duplicates):
        idx = random.randint(0, len(pool) - 1 - i)  # [0... last_index - i]
        duplicates.append(pool[idx])
        pool[idx], pool[-i - 1] = pool[-i - 1], pool[idx]
    duplicates *= 2
    nums = duplicates + pool[:num_uniques]
    random.shuffle(nums)
    return nums, pool[:num_uniques][0]


if __name__ == '__main__':
    cases = [
        ([2,2,1], 1),
        ([4,1,2,1,2], 4),
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
        actual = Solution().singleNumber(case)
        ans = expected == actual
        result.append(ans)
        print(f'{ans}\texpected: {expected}\tactual: {actual}')
    if not all(result):
        raise Exception('Wrong')
