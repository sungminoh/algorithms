#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

Constraints:

	1 <= strs.length <= 600
	1 <= strs[i].length <= 100
	strs[i] consists only of digits '0' and '1'.
	1 <= m, n <= 100
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """05/09/2020 17:55
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
        """04/21/2021 01:20
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
        """04/21/2021 01:32
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

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """06/08/2022 11:07"""
        cnt = []
        for s in strs:
            zero_one_cnt = [0, 0]
            for c in s:
                zero_one_cnt[int(c)] += 1
            cnt.append(zero_one_cnt)

        @lru_cache(None)
        def dfs(i, m, n):
            if i == len(cnt):
                return 0
            ret = dfs(i+1, m, n)
            if cnt[i][0] <= m and cnt[i][1] <= n:
                ret = max(ret, dfs(i+1, m-cnt[i][0], n-cnt[i][1])+1)
            return ret

        return dfs(0, m, n)


@pytest.mark.parametrize('strs, m, n, expected', [
    (["10","0001","111001","1","0"], 5, 3, 4),
    (["10","0","1"], 1, 1, 2),
    (["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80, 17),
])
def test(strs, m, n, expected):
    assert expected == Solution().findMaxForm(strs, m, n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
