#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List
import pytest
import random


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        cnt = {}
        for n in nums1:
            cnt.setdefault(n, 0)
            cnt[n] += 1
        ret = []
        for n in nums2:
            if cnt.get(n, 0) > 0:
                ret.append(n)
                cnt[n] -= 1
        return ret


def gen_case():
    nums1 = random.choices(range(random.randint(1, 50)), k=random.randint(0, 10))
    nums2 = random.choices(range(random.randint(1, 50)), k=random.randint(0, 10))
    ans = [n for n in nums1 if n in nums2]
    return nums1, nums2, ans


@pytest.mark.parametrize(
    'nums1, nums2, expected', [
        ([1,2,2,1], [2,2], [2,2]),
        ([4,9,5], [9,4,9,8,4], [4,9]),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case(),
        gen_case()
    ])
def test(nums1, nums2, expected):
    s = Solution()
    assert sorted(s.intersect(nums1, nums2)) == sorted(expected)
