#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b . Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:

The number of given pairs will be in the range [1, 1000].
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
        pairs.sort()
        cnt = 1
        l = pairs[0]
        for p in pairs[1:]:
            if l[1] < p[0]:
                cnt += 1
                l = p
            else:
                if p[1] < l[1]:
                    l = p
        return cnt

    def _findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        @lru_cache(None)
        def rec(i):
            m = 1
            for j in range(i):
                l = rec(j)
                if pairs[j][1] < pairs[i][0]:
                    m = max(m, l+1)
            return m
        return rec(len(pairs)-1)


@pytest.mark.parametrize('pairs, expected', [
    ([[1,2], [2,3], [3,4]], 2),
    ([[3,4],[2,3],[1,2]], 2)
])
def test(pairs, expected):
    assert expected == Solution().findLongestChain(pairs)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
