from functools import lru_cache
from collections import deque
from collections import defaultdict

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
from dataclasses import dataclass
import pytest
import sys


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """TLE"""
        @lru_cache(None)
        def prob(cur):
            if K <= cur <= N:
                return 1
            if cur > N:
                return 0
            return sum(prob(cur+i) * (1 / W) for i in range(1, W+1))

        return prob(0)

    def new21Game(self, N: int, K: int, W: int) -> float:
        """Sep 20, 2020 12:19"""
        if K == 0:
            return 1
        memo = [0.]*K  # answer when you start at each index
        # K-1, K,    N       K-1+W
        # 0,   1,    N-K+1   W
        memo[K-1] = (N-K+1) / W
        for i in range(K-2, -1, -1):
            # take 1 step from i
            memo[i] = (memo[i+1] / W)
            # take (1, W] step from i
            # i.e. sum(prob from i+1+j)/W where 1<=j<W
            # note that prop from i
            #         = sum(prob from i+1+j)/W where 1<=j<=W
            memo[i] += memo[i+1] - (
                memo[i+1+W] if i+1+W < len(memo)
                else 1 if i+1+W <= N
                else 0
            )/W
        return memo[0]

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """TLE"""
        ret = 0
        prob = 1/maxPts
        d = {0: 1}
        while d:
            _d = defaultdict(float)
            for v, p in d.items():
                if v >= k:
                    if v <= n:
                        ret += p
                else:
                    for i in range(1, maxPts+1):
                        _d[i+v] += p*prob
            d = _d
        return ret

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Recursion overflow"""
        PROP = 1/maxPts

        @lru_cache(None)
        def dp(value):
            if value == 0:
                return 1
            ret = 0
            for i in range(1, min(maxPts, value)+1):
                if value-i < k:
                    ret += dp(value-i) * PROP
            return ret

        ret = 0
        for i in range(k, n+1):
            ret += dp(i)
        return ret

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """TLE"""
        PROP = 1/maxPts

        props = [0.]*(n+1)
        props[0] = 1.
        for v in range(1, n+1):
            for _v in range(max(0, v-maxPts), min(k, v)):
                props[v] += props[_v]*PROP

        return sum(props[k:])

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """Sep 23, 2023 12:53"""
        PROP = 1/maxPts

        props = [0.]*(n+1)
        props[0] = 1.
        acc = 1 if k > 0 else 0
        for v in range(1, n+1):
            props[v] = acc*PROP
            if v < k:
                acc += props[v]
            if 0 <= v-maxPts < k:
                acc -= props[v-maxPts]

        return sum(props[k:])


@pytest.mark.parametrize('args', [
    ((10, 1, 10, 1.00000)),
    ((6, 1, 10, 0.60000)),
    ((21, 17, 10, 0.73278)),
    ((0, 0, 1, 1.00000)),
    ((449, 355, 96, 0.9997852760210774)),
    ((9811, 8776, 1096, 0.9969558652063627)),
    ((5710, 5070, 8516, 0.13649394685476995)),
])
def test(args):
    assert abs(args[-1] - Solution().new21Game(*args[:-1])) < 1e-5


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
