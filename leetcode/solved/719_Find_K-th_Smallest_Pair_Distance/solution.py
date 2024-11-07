#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.
"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2
Output: 0

Example 3:

Input: nums = [1,6,1], k = 3
Output: 5

Constraints:

	n == nums.length
	2 <= n <= 104
	0 <= nums[i] <= 106
	1 <= k <= n * (n - 1) / 2
"""
from pathlib import Path
import json
from collections import defaultdict
from collections import Counter
from typing import List
import pytest
import sys


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """11/28/2022 18:19, TLE
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        dist = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dist.append(abs(nums[i]-nums[j]))

        def quick_select(arr, s, e, k):
            pivot = arr[e]
            i, j = s, e-1
            while i <= j:
                if arr[i] <= pivot:
                    i += 1
                elif arr[j] > pivot:
                    j -= 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[e] = arr[e], arr[i]
            if k<i:
                return quick_select(arr, s, i-1, k)
            elif k>i:
                return quick_select(arr, i+1, e, k)
            return arr[i]

        return quick_select(dist, 0, len(dist)-1, k-1)

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """11/28/2022 18:31
        Time Complexity: O(n*logn) + O(n*logm) where m = max(nums)
        """
        def count_le(m):
            cnt = 0
            i = j = 0
            while i < len(nums) or j < len(nums):
                while j < len(nums) and abs(nums[i]-nums[j]) <= m:
                    j += 1
                cnt += (j-i)-1
                i += 1
            return cnt

        def bisearch(l, r, k, func):
            while l <= r:
                m = l + (r-l)//2
                if func(m, k):
                    r = m-1
                else:
                    l = m+1
            return r+1

        nums.sort()
        l, r = 0, nums[-1]-nums[0]
        return bisearch(l, r, k, func=lambda m, k: count_le(m)>=k)

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """TLE"""
        cnts = Counter(nums)
        keys = sorted(cnts.keys())
        N = len(keys)
        dists = defaultdict(int)
        for i in range(N):
            dists[0] += (cnts[keys[i]] * (cnts[keys[i]]-1)) // 2
            for j in range(i):
                dists[abs(keys[i] - keys[j])] += cnts[keys[i]]*cnts[keys[j]]


        for d in sorted(dists.keys()):
            k -= dists[d]
            if k <= 0:
                return d

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """Nov 06, 2024 18:01"""
        N = len(nums)

        def count_le(m):
            ret = 0
            i = j = 0
            while i < N or j < N:
                while j < N and abs(nums[i] - nums[j]) <= m:
                    j += 1
                ret += (j-i)-1
                i += 1
            return ret

        def bisearch(l, r, k):
            while l <= r:
                m = l + (r-l)//2
                if count_le(m) >= k:
                    r = m-1
                else:
                    l = m+1
            return r+1

        nums.sort()
        l, r = 0, nums[-1]-nums[0]
        return bisearch(l, r, k)


@pytest.mark.parametrize('args', [
    (([1,3,1], 1, 0)),
    (([1,1,1], 2, 0)),
    (([1,6,1], 3, 5)),
    (([9,10,7,10,6,1,5,4,9,8], 18, 2)),
    (([2,2,0,1,0,1,2,0,2,1,1,1,1,0,1,2,1,1,1,2,1,2,1,0,1,0,1,1,0,2,1,0,0,2,2,1,1,1,2,2,1,0,0,0,2,0,0,0,0,0,1,0,1,2,2,2,2,2,2,1,1,0,1,0,1,1,1,1,2,1,1,2,2,2,0,1,2,2,2,0,0,2,0,1,2,2,1,2,0,2,1,0,0,2,1,1,0,1,0,1,0,0,0,1,1,2,0,0,1,2,2,2,2,2,2,0,2,1,1,1,1,1,2,0,2,2,2,0,2,0,1,0,1,2,1,0,1,2,1,2,1,2,0,2,0,1,0,1,2,2,1,2,2,1,0,0,1,2,1,1,0,0,2,1,0,2,1,2,0,0,1,0,2,0,1,2,2,2,1,2,0,2,2,2,2,2,0,0,0,1,0,2,0,0,1,1,0,0,2,2,1,0,0,0,2,0,1,1,1,2,1,1,2,1,1,0,1,0,1,1,1,2,0,0,2,2,2,1,1,1,2,2,2,0,1,0,0,0,0,1,0,2,2,0,2,2,1,1,1,2,1,1,1,0,2,0,2,1,1,2,2,1,1,2,0,0,2,1,2,0,1,1,1,2,2,0,1,2,2,2,1,1,0,1,0,0,1,2,1,1,0,1,0,2,2,2,0,1,1,0,1,0,1,2,2,2,1,1,0,1,0,0,2,1,1,1,0,0,0,0,2,2,2,0,1,0,2,0,0,0,0,0,0,2,0,1,0,0,0,1,1,2,2,1,2,2,0,2,1,0,2,1,2,0,1,2,1,2,2,2,2,2,0,0,1,0,0,2,2,0,1,0,0,0,2,1,0,1,2,1,1,0,0,1,1,0,0,2,2,2,1,0,0,0,0,0,0,1,0,1,2,0,1,1,2,1,0,0,0,2,2,1,2,2,0,0,1,0,1,0,0,1,2,0,0,0,1,1,0,0,1,0,0,0,0,0,2,0,2,0,0,0,0,0,1,2,1,1,1,2,2,0,2,1,0,2,1,0,2,1,1,0,2,0,2,1,0,0,0,1,1,0,1,0,2,2,2,1,2,0,1,2,0,0,0,2,2,2,1,1,1,2,2,2,2,0,1,0,0,1], 62500, 1)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 25000000, 292051)),
])
def test(args):
    assert args[-1] == Solution().smallestDistancePair(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
