#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Note:

	1 <= A.length <= 100.
	1 <= A[i] <= 10000.
	1 <= K <= A.length.
	Answers within 10^-6 of the correct answer will be accepted as correct.
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        cumsum = [A[0]]
        for i in range(1, len(A)):
            cumsum.append(cumsum[-1] + A[i])
        cumsum.append(0)

        @lru_cache(None)
        def rec(i, K):
            if K == 1:
                return (cumsum[len(A)-1] - cumsum[i-1]) / (len(A)-i)
            return max((cumsum[j] - cumsum[i-1]) / (j-i+1) + rec(j+1, K-1) for j in range(i, len(A)-K+1))

        return rec(0, K)



@pytest.mark.parametrize('A, K, expected', [
    ([9,1,2,3,9], 3, 20),
])
def test(A, K, expected):
    assert expected == Solution().largestSumOfAverages(A, K)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
