#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0

Constraints:

	1 <= nums.length, k <= 105
	-104 <= nums[i] <= 104
"""
from collections import deque
from heapq import heappop, heappush
from pathlib import Path
import json
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """Top Down"""
        @lru_cache(None)
        def score(i):
            if i == 0:
                return nums[i]
            return nums[i] + max(score(j) for j in range(max(0, i-k), i))

        return score(len(nums)-1)

    def maxResult(self, nums: List[int], k: int) -> int:
        """Bottom Up"""
        if not nums:
            return 0

        memo = [0] * k
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            memo[i%k] = (nums[i] + max(memo[j%k] for j in range(max(0, i-k), i)))
        return memo[(len(nums)-1)%k]

    def maxResult(self, nums: List[int], k: int) -> int:
        """Bottom Up"""
        if not nums:
            return 0

        memo = [0] * k
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            mx = -float('inf')
            for j in range(i-1, max(0, i-k)-1, -1):
                if nums[j] > 0:
                    memo[i%k] = nums[i] + memo[j%k]
                    break
                else:
                    if memo[j%k] > mx:
                        mx = memo[j%k]
            else:
                memo[i%k] = nums[i] + mx
        return memo[(len(nums)-1)%k]

    def maxResult(self, nums: List[int], k: int) -> int:
        """07/26/2022 12:55
        Heap
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        heap = []
        for i in range(len(nums)):
            while heap and heap[0][1] < i-k:
                heappop(heap)
            score = nums[i] + (-heap[0][0] if heap else 0)
            if i == len(nums)-1:
                return score
            heappush(heap, (-score, i))

    def maxResult(self, nums: List[int], k: int) -> int:
        """07/26/2022 12:59
        Decreasing Queue
        Time complexity: O(n)
        Space complexity: O(k)
        """
        queue = deque()  # (index, score)
        for i in range(len(nums)):
            score = nums[i] + (queue[0][1] if queue else 0)
            while queue and queue[-1][1] <= score:
                queue.pop()
            queue.append((i, score))
            while queue and queue[0][0] <= i-k:
                queue.popleft()
        return queue[-1][1]


@pytest.mark.parametrize('nums, k, expected', [
    ([1,-1,-2,4,-7,3], 2, 7),
    ([10,-5,-2,4,0,3], 3, 17),
    ([1,-5,-20,4,-1,3,-6,-3], 2, 0),
    ([-123], 10, -123),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 223537346),
    (*json.load(open(Path(__file__).parent/'testcase2.json')), 1),
])
def test(nums, k, expected):
    assert expected == Solution().maxResult(nums, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
