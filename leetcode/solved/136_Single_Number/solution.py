#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:
Input: nums = [1]
Output: 1

Constraints:

	1 <= nums.length <= 3 * 104
	-3 * 104 <= nums[i] <= 3 * 104
	Each element in the array appears twice except for one element which appears only once.
"""
import random
import sys
from typing import List
import pytest


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


@pytest.mark.parametrize('nums, expected', [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case(),
    gen_case()
])
def test(nums, expected):
    assert expected == Solution().singleNumber(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
