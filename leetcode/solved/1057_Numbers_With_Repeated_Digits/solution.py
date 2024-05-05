#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.

Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:

Input: n = 1000
Output: 262

Constraints:

	1 <= n <= 109
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """May 04, 2024 12:00"""
        s = str(n)

        @lru_cache(None)
        def dfs(i, smaller, possible):
            if i == len(s):
                return 1
            ret = 0
            if not smaller:
                d = int(s[i])
                if s[i] not in s[:i]:
                    ret += dfs(i+1, False, None)  # d
                if d > 0 and '0' not in s[:i]:
                    ret += dfs(i+1, True, 10 if i == 0 else (10-(i+1)))  # 0
                if d > 1:
                    _possible = set(range(1, d)) - set(map(int, s[:i]))
                    ret += len(_possible) * dfs(i+1, True, 10-(i+1))  # 1 ~ d-1
            else:
                if possible == 10:
                    ret += dfs(i+1, True, possible)  # all zero so far
                    ret += 9 * dfs(i+1, True, 9)  # use non zero
                elif possible > 0:
                    ret += possible * dfs(i+1, True, possible-1)
            return ret

        return n+1 - dfs(0, False, None)


@pytest.mark.parametrize('args', [
    ((20, 1)),
    ((100, 10)),
    ((1000, 262)),
    ((11, 1)),
    ((12, 1)),
    ((101, 11)),
    ((110, 12)),
])
def test(args):
    assert args[-1] == Solution().numDupDigitsAtMostN(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
