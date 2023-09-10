#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

	answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
	answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

Constraints:

	1 <= nums1.length, nums2.length <= 1000
	-1000 <= nums1[i], nums2[i] <= 1000
"""
from typing import List
import pytest
import sys


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """Sep 09, 2023 21:29"""
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1.difference(s2)), list(s2.difference(s1))]


@pytest.mark.parametrize('args', [
    (([1,2,3], [2,4,6], [[1,3],[4,6]])),
    (([1,2,3,3], [1,1,2,2], [[3],[]])),
])
def test(args):
    assert args[-1] == Solution().findDifference(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
