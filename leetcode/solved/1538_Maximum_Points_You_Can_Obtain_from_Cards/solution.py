#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Constraints:

	1 <= cardPoints.length <= 105
	1 <= cardPoints[i] <= 104
	1 <= k <= cardPoints.length
"""
import itertools
from pathlib import Path
import json
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """05/27/2021 15:20
        DP
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if k >= len(cardPoints):
            return sum(cardPoints)
        left = [0] + list(itertools.accumulate(cardPoints))
        right = [0] + list(itertools.accumulate(reversed(cardPoints)))
        return max(left[i] + right[k-i] for i in range(k+1))

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """TLE"""
        n = len(cardPoints)-1

        @lru_cache(None)
        def rec(i, j):
            if i + (n-j) == k:
                return 0
            return max(cardPoints[i] + rec(i+1, j), cardPoints[j] + rec(i, j-1))

        return rec(0, n)

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """07/22/2022 21:26"""
        n = len(cardPoints)-1
        acc = list(itertools.accumulate(cardPoints))
        ret = 0
        for i in range(k+1):
            j = n-(k-i)
            left = acc[i-1] if i>0 else 0
            right = acc[-1] - acc[j]
            ret = max(ret, left + right)
        return ret


@pytest.mark.parametrize('cardPoints, k, expected', [
    ([1,2,3,4,5,6,1], 3, 12),
    ([2,2,2], 2, 4),
    ([9,7,7,9,7,7,9], 7, 55),
    ([1,1000,1], 1, 1),
    ([1,79,80,1,1,1,200,1], 3, 202),
    (*json.load(open(Path(__file__).parent/'testcase.json')), 1461736)
])
def test(cardPoints, k, expected):
    assert expected == Solution().maxScore(cardPoints, k)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
