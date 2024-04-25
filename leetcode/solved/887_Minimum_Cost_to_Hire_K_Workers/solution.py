#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

	Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
	Every worker in the paid group must be paid at least their minimum wage expectation.

Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

Constraints:

	n == quality.length == wage.length
	1 <= k <= n <= 104
	1 <= quality[i], wage[i] <= 104
"""
from functools import lru_cache
from typing import List
from heapq import heappop, heappush
import pytest
import sys


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """TLE
        q1, q2, q3, ... qn
        w1, w2, w3, ... wn

        for ij in [1, n] where j in [1, k]
        w_ij <= X * q_ij / sum(q_I)
        -> sum(q_I) * w_ij / q_ij <= X
        -> sum(q_I) * max(w_ij / q_ij) = X
        """
        N = len(quality)

        @lru_cache(None)
        def dp(i, k, s, e):
            if k == 0:
                return s*e
            if N-i < k:
                return float('inf')
            return min(
                dp(i+1, k, s, e),
                dp(i+1, k-1, s + quality[i], max(e, wage[i]/quality[i])))


        return dp(0, k, 0, 0)

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """Apr 18, 2024 21:32"""
        qw = sorted(zip(quality, wage))
        h = []
        s = 0
        ret = float('inf')
        for q, w in qw:
            if len(h) == k:
                e, p = heappop(h)
                e = -e
                s -= p
            s += q
            heappush(h, (-(w/q), q))
            if len(h) == k:
                cost = -h[0][0] * s
                ret = min(ret, cost)
        return ret


@pytest.mark.parametrize('args', [
    (([10,20,5], [70,50,30], 2, 105.00000)),
    (([3,1,10,10,1], [4,8,2,2,7], 3, 30.66667)),
    (([86,15,92,47,63,12,99,54,6,16,52,28,86,38,73,16,52,37,30,84,81,46,97,84,17,21,14,52,19,74,20,20,56,89,7,34,21,75,6,93,30,5,13,19,98,46,16,9,10,29],
      [281,29,346,275,475,466,233,15,148,206,143,370,47,52,72,403,259,116,286,380,293,92,330,128,432,233,161,479,9,335,258,263,427,58,177,8,204,173,261,319,448,268,420,492,335,42,401,500,256,328],
      10,
      990.0)),
    (([48,12,68,70,80,36,66,3,70,58,38,76,69,32,24,35,82,30,86,77,92,3,35,20,84,67,23,58,94,10,26,35,78,22,14,62,30,21,86,7,70,67,8,28,61,33,3,78,18,71],
      [84,484,366,274,338,317,228,237,42,8,346,195,258,152,427,10,151,37,139,389,23,397,309,223,477,500,82,358,334,319,100,330,201,336,166,335,173,118,379,7,76,213,433,148,16,487,57,147,232,223],
      30,
      10028.23334)),
])
def test(args):
    assert abs(args[-1] - Solution().mincostToHireWorkers(*args[:-1])) < 1e-5


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
