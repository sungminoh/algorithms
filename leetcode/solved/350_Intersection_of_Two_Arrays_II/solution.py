#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

	1 <= nums1.length, nums2.length <= 1000
	0 <= nums1[i], nums2[i] <= 1000

Follow up:

	What if the given array is already sorted? How would you optimize your algorithm?
	What if nums1's size is small compared to nums2's size? Which algorithm is better?
	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
import sys
from typing import List
import pytest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """04/05/2020 15:26"""
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

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ret = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ret.append(nums1[i])
                i += 1
                j += 1
        return ret


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1,2,2,1], [2,2], [2,2]),
    ([4,9,5], [9,4,9,8,4], [4,9]),
])
def test(nums1, nums2, expected):
    assert expected == Solution().intersect(nums1, nums2)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
