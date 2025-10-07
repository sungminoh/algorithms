#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.

Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278

Constraints:

	0 <= k <= n <= 104
	1 <= maxPts <= 104
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Wrong: different length of paths have different probability"""
        if k-1 + maxPts <= n:
            return 1

        @lru_cache(None)
        def num_cases(x):
            if x == 0:
                return 1
            return sum(num_cases(y) for y in range(max(0, x-maxPts), min(x, k)))

        numerator = sum(num_cases(i) for i in range(k,  n+1))
        denominator = sum(num_cases(i) for i in range(k, k+maxPts))
        return numerator/denominator

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Sep 05, 2025 10:44"""
        if k == 0 or k-1 + maxPts <= n:
            return 1
        dp = [0]*(n+1)
        dp[0] = s = 1
        for i in range(1, n+1):
            dp[i] = s/maxPts
            if i >= maxPts:
                s -= dp[i-maxPts]
            if i < k:
                s += dp[i]
        return sum(dp[k:])


@pytest.mark.parametrize('args', [
    ((10, 1, 10, 1.00000)),
    ((6, 1, 10, 0.60000)),
    ((21, 17, 10, 0.73278)),
])
def test(args):
    assert Solution().new21Game(*args[:-1]) == pytest.approx(args[-1], 3)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
