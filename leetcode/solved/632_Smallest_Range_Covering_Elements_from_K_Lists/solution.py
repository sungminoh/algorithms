#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Constraints:

	nums.length == k
	1 <= k <= 3500
	1 <= nums[i].length <= 50
	-105 <= nums[i][j] <= 105
	nums[i] is sorted in non-decreasing order.
"""
from collections import Counter
from collections import deque
from heapq import heapify, heappop, heappush
from typing import List
import pytest
import sys


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def min_range(r1, r2):
            if not r1 or not r2:
                return r1 or r2
            if (r1[1] - r1[0] < r2[1] - r2[0]) or (r1[0] < r2[0] and r1[1] - r1[0] == r2[1] - r2[0]):
                return r1
            return r2

        ret = None
        counter = Counter()
        queue = deque()
        indexes = [0]*len(nums)
        heap = [(lst[0], 0, i) for i, lst in enumerate(nums)]
        heapify(heap)
        while heap:
            v, j, i = heappop(heap)
            queue.append((v, i))
            counter[i] += 1
            while counter[queue[0][1]] > 1:
                _, k = queue.popleft()
                counter[k] -= 1
                if counter[k] == 0:
                    counter.pop(k)
            if j+1 < len(nums[i]):
                heappush(heap, (nums[i][j+1], j+1, i))
            if len(counter) == len(nums):
                ret = min_range(ret, [queue[0][0], queue[-1][0]])
        return ret


@pytest.mark.parametrize('nums, expected', [
    ([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]], [20,24]),
    ([[1,2,3],[1,2,3],[1,2,3]], [1,1]),
])
def test(nums, expected):
    assert expected == Solution().smallestRange(nums)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
