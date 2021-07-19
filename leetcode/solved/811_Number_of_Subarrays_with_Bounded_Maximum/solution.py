#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7

Constraints:

	1 <= nums.length <= 105
	0 <= nums[i] <= 109
	0 <= left <= right <= 109
"""
import sys
import itertools
from typing import List
import pytest



class SegmentTree:
    def __init__(self, nums, merge=max):
        def build(l, r):
            if l == r:
                return [nums[l], None, None]
            m = l + (r-l)//2
            left = build(l, m)
            right = build(m+1, r)
            return [merge(left[0], right[0]), left, right]

        self.merge = merge
        self.size = len(nums)
        self.tree = build(0, self.size-1)

    def query(self, i, j):
        def q(l, r, i, j, node):
            v, ln, rn = node
            if l == i and r == j:
                return v
            m = l + (r-l)//2
            if j <= m:
                return q(l, m, i, j, ln)
            if i > m:
                return q(m+1, r, i, j, rn)
            return self.merge(q(l, m, i, m, ln), q(m+1, r, m+1, j, rn))
        return q(0, self.size-1, i, j, self.tree)


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """09/17/2020 16:36"""
        cnt = 0
        p = -1
        s = -1
        for i, n in enumerate(A):
            if n > R:
                if p >= 0:
                    cnt += (i-p-1)*(p-s)
                s = i
                p = -1
            elif L <= n <= R:
                if p >= 0:
                    cnt += (i-p-1)*(p-s)
                cnt += i-s
                p = i
        if p >= 0:
            cnt += (len(A)-p-1)*(p-s)
        return cnt

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        Segment tree. TLE
        Time complexity: O(n^2 * log(n))
        """
        if not nums:
            return 0
        tree = SegmentTree(nums, merge=max)
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if left <= tree.query(i, j) <= right:
                    cnt += 1
        return cnt

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        Count the number of valid intervals that end at i
        If ith number is smaller than `left`, possible starting indexes are
        between the last index whose value is larger than the `right` and the
        last index whose value is between `left` and `right`.
        If ith number is between `left` and `right`, any indexes before i can
        be starting index.
        If ith number is larget than `right`, non is possible.
        Need to keep the last index whose value is between `left` and `right`
        and the last index whoe value is larger than `right`

        Time complexity: O(n)
        """
        cnt = 0
        p = -1
        s = -1
        for i, n in enumerate(nums):
            if n < left:
                if p >= 0:
                    cnt += (p-s)
            elif left <= n <= right:
                cnt += i-s
                p = i
            else:
                p = -1
                s = i
        return cnt


@pytest.mark.parametrize('nums, left, right, expected', [
    ([2,1,4,3], 2, 3, 3),
    ([2,9,2,5,6], 2, 8, 7),
    ([73,55,36,5,55,14,9,7,72,52], 32, 69, 22),
])
def test(nums, left, right, expected):
    assert expected == Solution().numSubarrayBoundedMax(nums, left, right)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
