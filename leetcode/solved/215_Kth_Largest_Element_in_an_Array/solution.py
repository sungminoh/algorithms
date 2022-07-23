#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

	1 <= k <= nums.length <= 104
	-104 <= nums[i] <= 104
"""
import sys
from heapq import heappop
from heapq import heappush
from typing import List
import pytest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """04/29/2019 00:26"""
        if k == 1:
            return max(nums)
        n = nums[-1]
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] < n < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] >= n:
                i += 1
            if nums[j] <= n:
                j -= 1
        nums[j + 1], nums[-1] = n, nums[j + 1]
        if k - 1 < j + 1:
            return self.findKthLargest(nums[:j + 1], k)
        elif k - 1 > j + 1:
            return self.findKthLargest(nums[j + 2:], k - j - 2)
        else:
            return nums[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Heap
        Time complexity: O(nlogk)
        Sapce complexity: O(k)
        """
        class HeapWithCapacity:
            def __init__(self, capacity):
                self.capacity = capacity
                self.h = []

            def add(self, v):
                heappush(self.h, v)
                while len(self.h) > self.capacity:
                    heappop(self.h)

            def peak(self):
                return self.h[0]

        h = HeapWithCapacity(k)
        for n in nums:
            h.add(n)

        return h.peak()

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quick select
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def quick_select(i, j, k):
            pivot = nums[j]
            s, e = i, j-1
            while s <= e:
                if nums[s] > pivot:
                    swap(s, e)
                    e -= 1
                elif nums[e] < pivot:
                    swap(s, e)
                    s += 1
                else:
                    e -= 1
                    s += 1
            swap(s, j)
            if s < k:
                return quick_select(s+1, j, k)
            elif s > k:
                return quick_select(i, s-1, k)
            return nums[s]

        return quick_select(0, len(nums)-1, len(nums)-k)


@pytest.mark.parametrize('nums, k, expected', [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4),
    ([1,2,3,4,5,6,7], 4),
])
def test(nums, k, expected):
    assert expected == Solution().findKthLargest(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

