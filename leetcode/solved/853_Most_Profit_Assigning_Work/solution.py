
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

Notes:
    1. 1 <= difficulty.length = profit.length <= 10000
    2. 1 <= worker.length <= 10000
	3. difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
"""
import sys
from typing import List
import pytest


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
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


@pytest.mark.parametrize('difficulty, profit, worker, expected', [
    ([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7], 100),
    ([85,47,57], [24,66,99], [40,25,25], 0),
    ([13,37,58], [4,90,96], [34,73,45], 190)
])
def test(difficulty, profit, worker, expected):
    assert expected == Solution().maxProfitAssignment(difficulty, profit, worker)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
