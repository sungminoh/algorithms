#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Example 3:

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:

	1 <= startTime.length == endTime.length == profit.length <= 5 * 104
	1 <= startTime[i] < endTime[i] <= 109
	1 <= profit[i] <= 104
"""
from pathlib import Path
import json
import bisect
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        sep = list(sorted(zip(startTime, endTime, profit)))
        @lru_cache(None)
        def dp(i):
            if i == len(sep):
                return 0
            j = i+1
            while j < len(sep):
                if sep[j][0] >= sep[i][1]:
                    break
                j += 1
            return max(dp(i+1), sep[i][2] + dp(j))
        return dp(0)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Time complexity: O(n*logn)
        Space complexity: O(n)
        """
        sep = list(sorted(zip(startTime, endTime, profit)))
        @lru_cache(None)
        def dp(i):
            if i == len(sep):
                return 0
            j = bisect.bisect_left(sep, (sep[i][1], ), lo=i+1)
            return max(dp(i+1), sep[i][2] + dp(j))
        return dp(0)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """12/03/2022 14:15, Memory Limit Exceeded"""
        sep = list(sorted(zip(startTime, endTime, profit)))

        @lru_cache(None)
        def dfs(i, cur):
            if i == len(sep):
                return 0
            if sep[i][0] < cur:
                return dfs(i+1, cur)
            return max(sep[i][2] + dfs(i+1, sep[i][1]), dfs(i+1, cur))

        return dfs(0, 0)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """12/03/2022 14:21
        Top down recursion
        """
        sep = list(sorted(zip(startTime, endTime, profit)))

        @lru_cache(None)
        def dfs(i):
            if i == len(sep):
                return 0
            j = bisect.bisect_left(sep, sep[i][1], key=lambda x: x[0])
            return max(sep[i][2] + dfs(j), dfs(i+1))

        return dfs(0)

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """12/03/2022 14:45
        Bottom up dp
        """
        sep = list(sorted(zip(startTime, endTime, profit), key=lambda x: x[1]))
        dp = [0]
        for i, (s, e, p) in enumerate(sep):
            j = bisect.bisect_right(sep, s, key=lambda x: x[1], hi=i)
            dp.append(max(dp[j] + p, dp[-1]))
        return dp[-1]


@pytest.mark.parametrize('startTime, endTime, profit, expected', [
    ([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
    ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150),
    ([1,1,1], [2,3,4], [5,6,4], 6),
    ([6,15,7,11,1,3,16,2],
     [19,18,19,16,10,8,19,8],
     [2,9,1,19,5,7,3,19], 41),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 1539718),
])
def test(startTime, endTime, profit, expected):
    assert expected == Solution().jobScheduling(startTime, endTime, profit)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
