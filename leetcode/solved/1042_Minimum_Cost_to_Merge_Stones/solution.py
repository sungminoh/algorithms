#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:

Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:

Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.

Constraints:

	n == stones.length
	1 <= n <= 30
	1 <= stones[i] <= 100
	2 <= k <= 30
"""
import itertools
from functools import lru_cache
from typing import List
from heapq import heappop, heappush
import pytest
import sys


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """Apr 28, 2024 19:44 TLE"""
        def ksum(arr):
            acc = 0
            i = 0
            while i < k:
                acc += arr[i]
                i += 1
            ret = [acc]
            while i < len(arr):
                acc -= arr[i-k]
                acc += arr[i]
                ret.append(acc)
                i += 1
            return ret

        h = [(0, stones)]
        while h:
            cnt, stones = heappop(h)
            if len(stones) >= k:
                ss = ksum(stones)
                for i, s in enumerate(ss):
                    heappush(h, (cnt+s, stones[:i] + [s] + stones[i+k:]))
            elif len(stones) == 1:
                return cnt
        return -1

    def mergeStones(self, stones: List[int], k: int) -> int:
        """Apr 28, 2024 20:25"""
        N = len(stones)

        if (N - 1) % (k - 1):
            return -1

        prefix_sum = list(itertools.accumulate(stones)) + [0]

        @lru_cache(None)
        def dp(i, j):
            if j-i+1 < k:
                return 0
            ret = float('inf')
            for p in range(i, j, k-1):
                ret = min(ret, dp(i, p) + dp(p+1, j))
            if (j-i)%(k-1)==0:
                ret += prefix_sum[j] - prefix_sum[i-1]
            return ret

        ret = dp(0, N-1)
        return -1 if ret == float('inf') else ret


@pytest.mark.parametrize('args', [
    (([3,2,4,1], 2, 20)),
    (([3,2,4,1], 3, -1)),
    (([3,5,1,2,6], 3, 25)),
    (([6,4,4,6], 2, 40)),
    # (([69,39,79,78,16,6,36,97,79,27,14,31,4], 2, 0)),
])
def test(args):
    assert args[-1] == Solution().mergeStones(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
