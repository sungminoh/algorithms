#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: 10, 1, 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.

Example 2:

Input: 6, 1, 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:

Input: 21, 17, 10
Output: 0.73278

Note:

	0 <= K <= N <= 10000
	1 <= W <= 10000
	Answers will be accepted as correct if they are within 10^-5 of the correct answer.
	The judging time limit has been reduced for this question.
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        memo = [0]*K
        # K-1, K,    N       K-1+W
        # 0,   1,    N-K+1   W
        memo[K-1] = (N-K+1) / W
        for i in range(K-2, -1, -1):
            memo[i] = (memo[i+1] / W) + (memo[i+1] - (memo[i+1+W] if i+1+W < len(memo) else 1 if i+1+W <= N else 0)/W)
        return memo[0]


    def _new21Game(self, N: int, K: int, W: int) -> float:
        @lru_cache(None)
        def prob(cur):
            if K <= cur <= N:
                return 1
            if cur > N:
                return 0
            return sum(prob(cur+i) * (1 / W) for i in range(1, W+1))

        return prob(0)


@pytest.mark.parametrize('N, K, W, expected', [
    (10, 1, 10, 1.00000),
    (6, 1, 10, 0.60000),
    (21, 17, 10, 0.73278),
    (9811, 8776, 1096, 0),
    (0, 0, 1, 1),
])
def test(N, K, W, expected):
    assert expected - Solution().new21Game(N, K, W) < 0.0001


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
