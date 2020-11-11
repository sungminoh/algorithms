#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
from typing import List
import random
import math


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        if xor == 0:
            return []
        rightmost_positive_bid_index = math.log2(xor & -xor)
        m = int(math.pow(2, rightmost_positive_bid_index))
        xors = [0, 0]
        for n in nums:
            xors[min(1, n & m)] ^= n
        return sorted(xors)


def gen_case():
    n = 10
    pool = list(range(1, n + 1))  # [1,2,3,4,...,n]
    duplicates = []
    # num_duplicates = random.randint(0, n)  # [0...n]
    # num_uniques = n - num_duplicates
    num_duplicates = n - 2
    num_uniques = 2
    for i in range(num_duplicates):
        idx = random.randint(0, len(pool) - 1 - i)  # [0... last_index - i]
        duplicates.append(pool[idx])
        pool[idx], pool[-i - 1] = pool[-i - 1], pool[idx]
    duplicates *= 2
    nums = duplicates + pool[:num_uniques]
    random.shuffle(nums)
    return nums, sorted(pool[:num_uniques])


if __name__ == '__main__':
    cases = [
        ([1,2,1,3,2,5], [3,5]),
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
