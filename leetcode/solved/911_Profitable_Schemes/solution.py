from collections import defaultdict
from functools import lru_cache
from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.

Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

Constraints:

	1 <= n <= 100
	0 <= minProfit <= 100
	1 <= group.length <= 100
	1 <= group[i] <= 100
	profit.length == group.length
	0 <= profit[i] <= 100
"""
import pytest
import sys


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """MLE"""
        MOD = int(1e9+7)

        N = len(group)

        @lru_cache(None)
        def dp(remaining_members, i, profit_over):
            if i == -1 or remaining_members == 0:
                if profit_over <= 0:
                    return 1
                return 0
            # no job
            ret = dp(remaining_members, i-1, profit_over)
            # job
            g = group[i]
            p = profit[i]
            if remaining_members >= g:
                ret += dp(remaining_members-g, i-1, profit_over-p)
            return ret % MOD

        return dp(n, N-1, minProfit)

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """Sep 03, 2023 22:08"""
        MOD = int(1e9+7)

        N = len(group)

        dp = defaultdict(int)
        dp[(n, 0)] = 1
        for i in range(N):
            for (r, p), c in list(dp.items()):
                if r >= group[i]:
                    # hack not to keep unnecessary detail
                    dp[(r-group[i], min(minProfit, p+profit[i]))] += c
                    dp[(r-group[i], min(minProfit, p+profit[i]))] %= MOD

        ret = 0
        for (r, p), c in dp.items():
            if p >= minProfit:
                ret += c
        return ret % MOD


@pytest.mark.parametrize('args', [
    ((5, 3, [2,2], [2,3], 2)),
    ((10, 5, [2,3,5], [6,7,8], 7)),
    ((95, 53, [82,7,18,34,1,3,83,56,50,34,39,38,76,92,71,2,6,74,1,82,22,73,88,98,6,71,6,26,100,75,57,88,43,16,22,89,7,9,78,97,22,87,34,81,74,56,49,94,87,71,59,6,20,66,64,37,2,42,30,87,73,16,39,87,28,9,95,78,43,59,87,78,2,93,7,22,21,59,68,67,65,63,78,20,82,35,86], [45,57,38,64,52,92,31,57,31,52,3,12,93,8,11,60,55,92,42,27,40,10,77,53,8,34,87,39,8,35,28,70,32,97,88,54,82,54,54,10,78,23,82,52,10,49,8,36,9,52,81,26,5,2,30,39,89,62,39,100,67,33,86,22,49,15,94,59,47,41,45,17,99,87,77,48,22,77,82,85,97,66,3,38,49,60,66], 9883351)),
    ((100, 100, [24,23,7,4,26,3,7,11,1,7,1,3,5,26,26,1,13,12,2,1,7,4,1,27,13,16,26,18,6,1,1,7,16,1,6,2,5,9,19,28,1,23,2,1,3,4,4,3,22,1,1,3,5,34,2,1,22,16,8,5,3,21,1,8,14,2,1,3,8,12,40,6,4,2,2,14,1,11,9,1,7,1,1,1,6,6,4,1,1,7,8,10,20,2,14,31,1,13,1,9], [5,2,38,25,4,17,5,1,4,0,0,8,13,0,20,0,28,1,22,7,10,32,6,37,0,11,6,11,23,20,13,13,6,2,36,1,0,9,4,5,6,14,20,1,13,6,33,0,22,1,17,12,10,1,19,13,8,1,0,17,20,9,8,6,2,2,1,4,22,11,3,2,6,0,40,0,0,7,1,0,25,5,12,7,19,4,12,7,4,4,1,15,33,14,2,1,1,61,4,5], 653387801)),
])
def test(args):
    assert args[-1] == Solution().profitableSchemes(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
