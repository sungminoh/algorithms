#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.

Constraints:

	1 <= jobDifficulty.length <= 300
	0 <= jobDifficulty[i] <= 1000
	1 <= d <= 10
"""
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """11/06/2022 00:36"""
        @lru_cache(None)
        def rec(i, d):
            if len(jobDifficulty)-i < d:
                return float('inf')
            if len(jobDifficulty)-i == d:
                return sum(jobDifficulty[i:])
            if d == 1:
                return max(jobDifficulty[i:])

            ret = float('inf')
            max_difficulty = -float('inf')
            while i < len(jobDifficulty):
                if max_difficulty < jobDifficulty[i]:
                    max_difficulty = jobDifficulty[i]
                ret = min(ret, max_difficulty + rec(i+1, d-1))
                i += 1
            return ret

        ret = rec(0, d)
        return ret if ret != float('inf') else -1


@pytest.mark.parametrize('jobDifficulty, d, expected', [
    ([6,5,4,3,2,1], 2, 7),
    ([9,9,9], 4, -1),
    ([1,1,1], 3, 3),
    ([11,111,22,222,33,333,44,444], 6, 843),
])
def test(jobDifficulty, d, expected):
    assert expected == Solution().minDifficulty(jobDifficulty, d)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
