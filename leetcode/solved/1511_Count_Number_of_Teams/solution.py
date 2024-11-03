#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

	Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
	A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4

Constraints:

	n == rating.length
	3 <= n <= 1000
	1 <= rating[i] <= 105
	All the integers in rating are unique.
"""
from typing import List
import pytest
import sys


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """Nov 02, 2024 19:22"""

        def count(rating, compare, points):
            N = len(rating)
            dp = [1] * N
            for n in range(points-1):
                _dp = [0] * N
                for j in range(n+1, N):
                    for i in range(j):
                        if compare(rating[i], rating[j]):
                            _dp[j] += dp[i]
                dp = _dp
            return sum(dp)

        return count(rating, lambda a, b: a < b, 3) + count(rating, lambda a, b: a > b, 3)


@pytest.mark.parametrize('args', [
    (([2,5,3,4,1], 3)),
    (([2,1,3], 0)),
    (([1,2,3,4], 4)),
])
def test(args):
    assert args[-1] == Solution().numTeams(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
