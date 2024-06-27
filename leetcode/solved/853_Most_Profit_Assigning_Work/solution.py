#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

	difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
	worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

Every worker can be assigned at most one job, but one job can be completed multiple times.

	For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

Constraints:

	n == difficulty.length
	n == profit.length
	m == worker.length
	1 <= n, m <= 104
	1 <= difficulty[i], profit[i], worker[i] <= 105
"""
import bisect
from typing import List
import pytest
import sys


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """May 25, 2020 19:37"""
        dp = sorted(zip(difficulty, profit))
        worker = sorted(worker)
        m = 0
        i = 0
        ret = 0
        for w in worker:
            while i < len(dp) and dp[i][0] <= w:
                m = max(dp[i][1], m)
                i += 1
            ret += m
        return ret

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """Jun 26, 2024 21:09"""
        dp = sorted(zip(difficulty, profit))
        if not dp:
            return 0
        d_maxp = [dp[0]]
        maxp = d_maxp[0][1]
        for d, p in dp[1:]:
            maxp = max(maxp, p)
            d_maxp.append((d, maxp))
        ret = 0
        for w in worker:
            i = bisect.bisect_right(d_maxp, w, key=lambda x: x[0])
            if i > 0:
                ret += d_maxp[i - 1][1]
        return ret


@pytest.mark.parametrize('args', [
    (([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7], 100)),
    (([85,47,57], [24,66,99], [40,25,25], 0)),
    (([13,37,58], [4,90,96], [34,73,45], 190)),
])
def test(args):
    assert args[-1] == Solution().maxProfitAssignment(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
