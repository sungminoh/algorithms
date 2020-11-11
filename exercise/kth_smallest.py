#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import sys
from typing import List
import pytest


def find_kth_smallest(nums: List[int], k: int):
    def _rec(nums, s, e):
        print(nums)
        l, r, = s, e
        while l < r:
            while nums[l] < nums[k]:
                l += 1
            while nums[r] > nums[k]:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if k < l:
            return _rec(nums, s, l - 1)
        if k > r:
            return _rec(nums, r + 1, e)
        return nums[k]
    _nums = nums[:]
    ans = _rec(_nums, 0, len(_nums) - 1)
    return ans


@pytest.mark.parametrize(
    'nums, k', [
        ([1,5,1,1,6,4], 2),
        ([1,3,2,2,3,1], 2),
        ([1,1,1,2,2,2], 2),
        ([1,2,3,9,8,7], 2),
        ([1,1,1,1,1,2,2,2,2,2], 2),
        ([4,5,5,6], 3),
        ([1,1,1,1,1,1], 1),
        ([1,1,2,2,2,1], 2)
    ])
def test(nums, k):
    n = find_kth_smallest(nums, k)
    assert sorted(nums)[k] == n


if __name__ == "__main__":
    pytest.main(["-s", "-v"] + sys.argv)
