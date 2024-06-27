#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Constraints:

	bloomDay.length == n
	1 <= n <= 105
	1 <= bloomDay[i] <= 109
	1 <= m <= 106
	1 <= k <= n
"""
from pathlib import Path
import json
import heapq
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """TLE"""
        N = len(bloomDay)

        mx = []
        h = []
        j = 0
        for i in range(N):
            while h and h[0][1] < i:
                heapq.heappop(h)
            while j-i < k and j < N:
                heapq.heappush(h, (-bloomDay[j], j))
                j += 1
            mx.append(-h[0][0])

        @lru_cache(None)
        def dfs(i, n):
            if n == 0:
                return 0
            if N-i < n*k:
                return float('inf')
            return min(dfs(i+1, n), max(dfs(i+k, n-1), mx[i]))

        ret = dfs(0, m)
        return ret if ret != float('inf') else -1

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """TLE"""
        N = len(bloomDay)

        mx = []
        h = []
        j = 0
        for i in range(N):
            while h and h[0][1] < i:
                heapq.heappop(h)
            while j-i < k and j < N:
                heapq.heappush(h, (-bloomDay[j], j))
                j += 1
            mx.append(-h[0][0])

        # Initialize the dp array with infinite values, except for the base cases
        dp = [[float('inf')] * (m + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 0  # 0 days needed if no bouquets are required

        # Fill the dp array from right to left (backwards)
        for i in range(N - 1, -1, -1):
            for n in range(1, m + 1):
                if i + k <= N:
                    dp[i][n] = min(dp[i + 1][n], max(dp[i + k][n - 1], mx[i] if i < len(mx) else float('inf')))

        # The answer is stored in dp[0][m]
        return dp[0][m] if dp[0][m] != float('inf') else -1

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """Jun 26, 2024 22:38"""
        N = len(bloomDay)

        if N < m*k:
            return -1

        mx = []
        h = []
        j = 0
        for i in range(N):
            while h and h[0][1] < i:
                heapq.heappop(h)
            while j-i < k and j < N:
                heapq.heappush(h, (-bloomDay[j], j))
                j += 1
            mx.append(-h[0][0])

        def doable(d):
            cnt = 0
            i = 0
            while i < N-(k-1):
                if mx[i] <= d:
                    cnt += 1
                    i += k
                else:
                    i += 1
            return cnt >= m

        def bisearch(s, e):
            while s <= e:
                d = s + (e-s)//2
                if doable(d):
                    e = d-1
                else:
                    s = d+1
            return e+1

        s, e = min(bloomDay), max(bloomDay)
        return bisearch(s, e)


@pytest.mark.parametrize('args', [
    (([1,10,3,10,2], 3, 1, 3)),
    (([1,10,3,10,2], 3, 2, -1)),
    (([7,7,7,7,12,7,7], 2, 3, 12)),
    (([1,10,2,9,3,8,4,7,5,6], 4, 2, 9)),
    ((json.load(open(Path(__file__).parent/'testcase.json')), 7349, 7, 365531)),
])
def test(args):
    assert args[-1] == Solution().minDays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
