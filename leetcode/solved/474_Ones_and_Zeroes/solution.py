
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

Constraints:
* 1 <= strs.length <= 600
* 1 <= strs[i].length <= 100
* strs[i] consists only of digits '0' and '1'.
* 1 <= m, n <= 100
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Time complexity: O(k*m'*n')
        Space complexity: O(k*m'*n')
        """
        def count(s):
            ret = [0, 0]
            for c in s:
                ret[int(c)] += 1
            return ret

        cnt = [count(s) for s in strs]

        @lru_cache(None)
        def _rec(i, m, n):
            if i >= len(strs):
                return 0
            ret = _rec(i + 1, m, n)
            a, b = cnt[i]
            if m >= a and n >= b:
                ret = max(ret, 1 + _rec(i + 1, m - a, n - b))
            return ret

        return _rec(0, m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Time complexity: O(k*m'*n' + klogk)
        Space complexity: O(k*m'*n')
        """
        def count(s):
            cnts = [0, 0]
            for c in s:
                cnts[0 if c == '0' else 1] += 1
            return tuple(cnts)

        pairs = [count(s) for s in strs]
        pairs.sort()

        @lru_cache(None)
        def dfs(i, m, n):
            if i >= len(pairs):
                return 0
            c0, c1 = pairs[i]
            if c0 > m:
                return 0
            ret = dfs(i+1, m, n)
            if m >= c0 and n >= c1:
                ret = max(ret, 1+dfs(i+1, m-c0, n-c1))
            return ret

        return dfs(0, m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Time complexity: O(k*m*n)
        Space complexity: O(m*n)
        """
        def count(s):
            cnts = [0, 0]
            for c in s:
                cnts[0 if c == '0' else 1] += 1
            return tuple(cnts)

        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            c0, c1 = count(s)
            for i in range(m, c0-1, -1):
                for j in range(n, c1-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-c0][j-c1])

        return dp[-1][-1]


@pytest.mark.parametrize('strs, m, n, expected', [
    (["10","0001","111001","1","0"], 5, 3, 4),
    (["10","0","1"], 1, 1, 2),
    (["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80, 17)
])
def test(strs, m, n, expected):
    assert expected == Solution().findMaxForm(strs, m, n)
