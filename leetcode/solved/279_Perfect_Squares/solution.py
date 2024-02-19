#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

	1 <= n <= 104
"""
from functools import lru_cache
from heapq import heappop
from math import ceil
import pytest
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        """09/10/2019 21:32"""
        def nsq(n, cnt, ret, memo):
            if n in memo:
                return memo[n]
            if cnt >= min(4, ret):
                return cnt
            if int(n ** (1/2)) ** 2 == n:
                return 1 if n != 0 else 0
            for i in range(int(n**(1/2)), 0, -1):
                ret = min(ret, 1 + nsq(n - (i**2), cnt + 1, ret, memo))
            memo[n] = ret
            return ret
        return nsq(n, 0, float('inf'), {})

    def numSquares(self, n: int) -> int:
        """09/10/2019 21:50"""
        squares = [i*i for i in range(int(n ** (1/2)), 0, -1)]
        ret = float('inf')
        memo = {}
        def nsq(n, i, cnt):
            nonlocal ret
            if n in memo:
                return memo[n]
            if cnt >= ret:
                return float('inf')
            if int(n ** (1/2)) ** 2 == n:
                return 1 if n != 0 else 0
            for j in range(i, len(squares)):
                m = n - squares[j]
                if m > 0:
                    ret = min(ret, 1 + nsq(m, j, cnt + 1))
            memo[n] = ret
            return ret
        return nsq(n, 0, 0)

    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        """TLE"""
        rt = int(n**0.5)
        if rt**2 == n:
            return 1
        return 1+min(self.numSquares(n-(i**2)) for i in range(rt, 0, -1))

    def numSquares(self, n: int) -> int:
        m = float('inf')

        visited = {}
        def dfs(n, cnt):
            nonlocal m
            if cnt > m or cnt >= visited.get(n, m) :
                return
            visited[n] = cnt
            if n == 0:
                m = min(m, cnt)
            rt = int(n**0.5)
            for i in range(rt, 0, -1):
                dfs(n-(i**2), cnt+1)

        dfs(n, 0)
        return m

    def numSquares(self, n: int) -> int:
        """11/29/2022 08:06, TLE"""
        squares = list(reversed([i*i for i in range(1, int(n**0.5)+1)]))

        def dfs(i, n):
            if n == 0:
                return 0
            if i == len(squares):
                return float('inf')
            ret = dfs(i+1, n)
            cnt = 0
            while squares[i] <= n:
                cnt += 1
                n -= squares[i]
                ret = min(ret, cnt+dfs(i+1, n))
            return ret

        return dfs(0, n)

    def numSquares(self, n: int) -> int:
        """12/03/2022 12:16"""
        ret = float('inf')

        visited = {}
        def rec(n, cnt):
            nonlocal ret
            if cnt >= ret or visited.get(n, float('inf'))<=cnt:
                return
            visited[n] = cnt
            if n == 0:
                ret = cnt
            for x in range(int(n**(0.5)), 0, -1):
                rec(n-(x*x), cnt+1)

        rec(n, 0)
        return ret

    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        """Feb 19, 2024 13:01"""
        if n == 0:
            return 0
        if int(n**.5)**2 == n:
            return 1
        return 1 + min(self.numSquares(n-i**2) for i in range(1, ceil(n**.5)))

    def numSquares(self, n: int) -> int:
        """Feb 19, 2024 13:25 BFS"""
        cnt = 0
        acc = set([0])
        while acc:
            _acc = set()
            if n in acc:
                return cnt
            for x in acc:
                for i in range(1, int(n**.5)+1):
                    y = x + i**2
                    if y <= n:
                        _acc.add(y)
            cnt += 1
            acc = _acc
        return cnt


@pytest.mark.parametrize('args', [
    ((12, 3)),
    ((13, 2)),
    ((4703, 4)),
    ((8935, 4)),
    ((25, 1)),
    ((144, 1)),
    ((31, 4)),
    ((0, 0)),
    ((1, 1)),
    ((16, 1)),
    ((88, 3)),  # 36 36 16
    ((7168, 4)),
    ((5156, 2)),
    ((192, 3)),
    ((240, 4)),  # 100 100 36 4
    ((6616, 3)),  # 60^2, 54^2, 10^2
    ((956, 4)),
    ((6024, 3)),
    ((2820, 3)),
])
def test(args):
    assert args[-1] == Solution().numSquares(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
