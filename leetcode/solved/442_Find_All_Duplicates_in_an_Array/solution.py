
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
import sys
from typing import List
import pytest


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            if n - 1 == i:
                continue
            while True:
                if n - 1 == i or nums[n - 1] == n:
                    nums[i] = n
                    break
                else:
                    tmp = nums[n - 1]
                    nums[n - 1] = n
                    n = tmp
        return [n for i, n in enumerate(nums) if n - 1 != i]


@pytest.mark.parametrize('nums, expected', [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([2, 1], [])
])
def test(nums, expected):
    assert sorted(expected) == sorted(Solution().findDuplicates(nums))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
