#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

	0 <= i, j, k, l < n
	nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:

	n == nums1.length
	n == nums2.length
	n == nums3.length
	n == nums4.length
	1 <= n <= 200
	-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
from collections import defaultdict
import sys
from typing import List
import pytest


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """05/03/2020 18:59"""
        ab_counter = defaultdict(int)
        for a in A:
            for b in B:
                ab_counter[a + b] += 1

        cd_counter = defaultdict(int)
        for c in C:
            for d in D:
                cd_counter[c + d] += 1

        ret = 0
        for k, v in ab_counter.items():
            ret += v * cd_counter.get(-k, 0)
        return ret

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Time complexity: O(n^4)
        Space complexity: O(n)
        """
        numsList = [nums1, nums2, nums3, nums4]
        indexes = [0] * len(numsList)
        def dfs(i, remain):
            if i == len(numsList):
                return 1 if remain == 0 else 0
            else:
                ret = 0
                for j in range(len(numsList[i])):
                    indexes[i] = j
                    ret += dfs(i+1, remain - numsList[i][indexes[i]])
                return ret
        return dfs(0, 0)

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        numsList = [nums1, nums2, nums3, nums4]
        numsList.sort(key=len)
        s = defaultdict(int)
        for i in range(len(numsList[0])):
            for j in range(len(numsList[3])):
                s[numsList[0][i] + numsList[3][j]] += 1
        ret = 0
        for i in range(len(numsList[1])):
            for j in range(len(numsList[2])):
                ret += s[-(numsList[1][i] + numsList[2][j])]
        return ret


@pytest.mark.parametrize('nums1, nums2, nums3, nums4, expected', [
    ([1,2], [-2,-1], [-1,2], [0,2], 2),
    ([0], [0], [0], [0], 1),
])
def test(nums1, nums2, nums3, nums4, expected):
    assert expected == Solution().fourSumCount(nums1, nums2, nums3, nums4)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
