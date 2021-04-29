#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

	perm[i] is divisible by i.
	i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:

Input: n = 1
Output: 1

Constraints:

	1 <= n <= 15
"""
from typing import List
from typing import Set
from functools import lru_cache
import sys
import pytest


class Solution:
    def countArrangement(self, n: int) -> int:
        """DFS using a list"""
        def dfs(i, remains: List[int]):
            if i == n+1:
                return 1
            cnt = 0
            for j in range(1, n+1):
                if remains[j] is None and (i%j == 0 or j%i == 0):
                    remains[j] = i
                    cnt += dfs(i+1, remains)
                    remains[j] = None
            return cnt

        return dfs(1, [None]*(n+1))


    def countArrangement(self, n: int) -> int:
        """DFS using a binary number to make argument hashable for caching"""
        def iter_digit(n):
            while n:
                yield n % 2
                n //= 2

        @lru_cache(None)
        def dfs(i, remains):
            if i == n+1:
                return 1
            cnt = 0
            for j, d in enumerate(iter_digit(remains)):
                if d == 0:
                    continue
                if j%i == 0 or i%j == 0:
                    remains ^= 2**j
                    cnt += dfs(i+1, remains)
                    remains ^= 2**j
            return cnt

        # starting from 11..10 (length is n+1)
        return dfs(1, 2**(n+1)-2)

    def countArrangement(self, n: int) -> int:
        """DFS using a set, especially frozenset for caching"""
        @lru_cache(None)
        def dfs(i, remains: Set[int]):
            if i == n+1:
                return 1
            cnt = 0
            for j in remains:
                if i%j == 0 or j%i == 0:
                    cnt += dfs(i+1, remains - {j})
            return cnt

        return dfs(1, frozenset(range(1, n+1)))


@pytest.mark.parametrize('n, expected', [
    (2,2),
    (1,1),
])
def test(n, expected):
    assert expected == Solution().countArrangement(n)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
