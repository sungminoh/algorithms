
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k  from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]

Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]

Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
from functools import lru_cache
import sys
from typing import List
import pytest


# sys.setrecursionlimit(10**6)


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_of_length(nums, i):
            ret = []
            discards = len(nums) - i
            for n in nums:
                while discards and ret and ret[-1] < n:
                    ret.pop()
                    discards -= 1
                ret.append(n)
            return ret[:i]

        def merge(l1, l2):
            ret = []
            i = j = 0
            while l1 or l2:
                ret.append(max(l1, l2).pop(0))
            return ret

        ret = []
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                arr1 = max_of_length(nums1, i)
                arr2 = max_of_length(nums2, k-i)
                ret = max(ret, merge(arr1, arr2))
        return ret


    def _maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)

        @lru_cache(None)
        def _rec(i, j, k):
            if k == 0:
                return 0
            if m - i + 1 + n - j + 1 < k:
                return 0
            n1 = -float('inf')
            i1 = i
            for _i in range(i, m-max(0, k-(n-j+1))):
                if nums1[_i] > n1:
                    n1 = nums1[_i]
                    i1 = _i
            n2 = -float('inf')
            i2 = j
            for _i in range(j, n-max(0, k-(m-i+1))):
                if nums2[_i] > n2:
                    n2 = nums2[_i]
                    i2 = _i
            if n1 > n2:
                ret = n1 * pow(10, k-1) + _rec(i1+1, j, k-1)
            elif n1 < n2:
                ret = n2 * pow(10, k-1) + _rec(i, i2+1, k-1)
            else:
                sub1 = n1 * pow(10, k-1) + _rec(i1+1, j, k-1)
                sub2 = n2 * pow(10, k-1) + _rec(i, i2+1, k-1)
                if sub1 > sub2:
                    ret = sub1
                else:
                    ret = sub2
            return ret
        return list(map(int, str(_rec(0, 0, k))))


    ([8,9,7,3,5,9,1,0,8,5,3,0,9,2,7,4,8,9,8,1,0,2,0,2,7,2,3,5,4,7,4,1,4,0,1,4,2,1,3,1,5,3,9,3,9,0,1,7,0,6,1,8,5,6,6,5,0,4,7,2,9,2,2,7,6,2,9,2,3,5,7,4,7,0,1,8,3,6,6,3,0,8,5,3,0,3,7,3,0,9,8,5,1,9,5,0,7,9,6,8,5,1,9,6,5,8,2,3,7,1,0,1,4,3,4,4,2,4,0,8,4,6,5,5,7,6,9,0,8,4,6,1,6,7,2,0,1,1,8,2,6,4,0,5,5,2,6,1,6,4,7,1,7,2,2,9,8,9,1,0,5,5,9,7,7,8,8,3,3,8,9,3,7,5,3,6,1,0,1,0,9,3,7,8,4,0,3,5,8,1,0,5,7,2,8,4,9,5,6,8,1,1,8,7,3,2,3,4,8,7,9,9,7,8,5,2,2,7,1,9,1,5,5,1,3,5,9,0,5,2,9,4,2,8,7,3,9,4,7,4,8,7,5,0,9,9,7,9,3,8,0,9,5,3,0,0,3,0,4,9,0,9,1,6,0,2,0,5,2,2,6,0,0,9,6,3,4,1,2,0,8,3,6,6,9,0,2,1,6,9,2,4,9,0,8,3,9,0,5,4,5,4,6,1,2,5,2,2,1,7,3,8,1,1,6,8,8,1,8,5,6,1,3,0,1,3,5,6,5,0,6,4,2,8,6,0,3,7,9,5,5,9,8,0,4,8,6,0,8,6,6,1,6,2,7,1,0,2,2,4,0,0,0,4,6,5,5,4,0,1,5,8,3,2,0,9,7,6,2,6,9,9,9,7,1,4,6,2,8,2,5,3,4,5,2,4,4,4,7,2,2,5,3,2,8,2,2,4,9,8,0,9,8,7,6,2,6,7,5,4,7,5,1,0,5,7,8,7,7,8,9,7,0,3,7,7,4,7,2,0,4,1,1,9,1,7,5,0,5,6,6,1,0,6,9,4,2,8,0,5,1,9,8,4,0,3,1,2,4,2,1,8,9,5,9,6,5,3,1,8,9,0,9,8,3,0,9,4,1,1,6,0,5,9,0,8,3,7,8,5], [7,8,4,1,9,4,2,6,5,2,1,2,8,9,3,9,9,5,4,4,2,9,2,0,5,9,4,2,1,7,2,5,1,2,0,0,5,3,1,1,7,2,3,3,2,8,2,0,1,4,5,1,0,0,7,7,9,6,3,8,0,1,5,8,3,2,3,6,4,2,6,3,6,7,6,6,9,5,4,3,2,7,6,3,1,8,7,5,7,8,1,6,0,7,3,0,4,4,4,9,6,3,1,0,3,7,3,6,1,0,0,2,5,7,2,9,6,6,2,6,8,1,9,7,8,8,9,5,1,1,4,2,0,1,3,6,7,8,7,0,5,6,0,1,7,9,6,4,8,6,7,0,2,3,2,7,6,0,5,0,9,0,3,3,8,5,0,9,3,8,0,1,3,1,8,1,8,1,1,7,5,7,4,1,0,0,0,8,9,5,7,8,9,2,8,3,0,3,4,9,8,1,7,2,3,8,3,5,3,1,4,7,7,5,4,9,2,6,2,6,4,0,0,2,8,3,3,0,9,1,6,8,3,1,7,0,7,1,5,8,3,2,5,1,1,0,3,1,4,6,3,6,2,8,6,7,2,9,5,9,1,6,0,5,4,8,6,6,9,4,0,5,8,7,0,8,9,7,3,9,0,1,0,6,2,7,3,3,2,3,3,6,3,0,8,0,0,5,2,1,0,7,5,0,3,2,6,0,5,4,9,6,7,1,0,4,0,9,6,8,3,1,2,5,0,1,0,6,8,6,6,8,8,2,4,5,0,0,8,0,5,6,2,2,5,6,3,7,7,8,4,8,4,8,9,1,6,8,9,9,0,4,0,5,5,4,9,6,7,7,9,0,5,0,9,2,5,2,9,8,9,7,6,8,6,9,2,9,1,6,0,2,7,4,4,5,3,4,5,5,5,0,8,1,3,8,3,0,8,5,7,6,8,7,8,9,7,0,8,4,0,7,0,9,5,8,2,0,8,7,0,3,1,8,1,7,1,6,9,7,9,7,2,6,3,0,5,3,6,0,5,9,3,9,1,1,0,0,8,1,4,3,0,4,3,7,7,7,4,6,4,0,0,5,7,3,2,8,5,1,4,5,8,5,6,7,5,7,3,3,9,6,8,1,5,1,1,1,0,3], 500, []),
@pytest.mark.parametrize('nums1, nums2, k, expected', [
    ([3, 4, 6, 5],[9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
    ([6, 7],[6, 0, 4], 5, [6, 7, 6, 0, 4]),
    ([3, 9],[8, 9], 3, [9, 8, 9]),
    ([2,2,0,6,8,9,6], [5,2,4,5,3,6,2], 7, [9, 6, 5, 5, 3, 6, 2]),
    ([7,6,1,9,3,2,3,1,1], [4,0,9,9,0,5,5,4,7], 9, [9, 9, 9, 7, 3, 2, 3, 1, 1]),
])
def test(nums1, nums2, k, expected):
    assert expected == Solution().maxNumber(nums1, nums2, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
