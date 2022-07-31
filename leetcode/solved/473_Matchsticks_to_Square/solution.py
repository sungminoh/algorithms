#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:

	1 <= matchsticks.length <= 15
	1 <= matchsticks[i] <= 108
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        """05/10/2020 08:32"""
        if len(nums) < 4:
            return False
        s, r = divmod(sum(nums), 4)
        if r != 0:
            return False

        @lru_cache(None)
        def use_to_make(used, n):
            if n == 0:
                yield from [used]
            if used == (1 << (len(nums) + 1)) - 1:
                yield from []
            for i in range(len(nums)):
                if used & 1 << i:
                    continue
                b = 1 << i
                used |= b
                yield from use_to_make(used, n - nums[i])
                used -= b

        @lru_cache(None)
        def can_devide_into_n_group(used, k):
            if k == 0:
                return True

            for u in use_to_make(used, s):
                if can_devide_into_n_group(u, k - 1):
                    return True
            return False

        return can_devide_into_n_group(1 << len(nums), 4)

    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Bruteforce. Iterate all possible cases. Time limit exceeded.
        Time complexity: O(n*4^n)
        Space complexity: O(1)
        """
        n, r = divmod(sum(matchsticks), 4)
        if r or len(matchsticks) < 4:
            return False
        matchsticks.sort(reverse=True)
        for i in range(4**len(matchsticks)):
            s = [0]*4
            for m in matchsticks:
                s[i % 4] += m
                if s[i % 4] > n:
                    break
                i //= 4
            else:
                return True
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        DFS by matchsticks
        Time complexity: O(4*4^n)
        Space complexity: O(n)  (call stack)
        """
        n, r = divmod(sum(matchsticks), 4)
        if r or len(matchsticks) < 4:
            return False
        matchsticks.sort(reverse=True)

        s = [n]*4
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(len(s)):
                if matchsticks[i] > s[j]:
                    continue
                s[j] -= matchsticks[i]
                if dfs(i+1):
                    return True
                s[j] += matchsticks[i]
            return False

        return dfs(0)

    def makesquare(self, matchsticks: List[int]) -> bool:
        """07/17/2021 20:33
        DFS by sides
        """
        n, r = divmod(sum(matchsticks), 4)
        if r or len(matchsticks) < 4:
            return False
        matchsticks.sort(reverse=True)

        @lru_cache(None)
        def dfs(i, cur, used):
            if i == 4:
                return True
            if cur > n:
                return False
            if cur == n:
                return dfs(i+1, 0, used)
            for j in range(len(matchsticks)):
                if used & (1<<j):
                    continue
                if dfs(i, cur+matchsticks[j], used | (1<<j)):
                    return True
            return False

        return dfs(0, 0, 0)

    def makesquare(self, matchsticks: List[int]) -> bool:
        """07/30/2022 20:58"""
        total = sum(matchsticks)
        if total%4 != 0:
            return False
        side = total//4
        matchsticks.sort(reverse=True)

        @lru_cache(None)
        def dfs(i, remainders):
            if i == len(matchsticks):
                return True
            for j in range(len(remainders)):
                if remainders[j] >= matchsticks[i]:
                    _remainders = list(remainders)
                    _remainders[j] -= matchsticks[i]
                    # acceleration
                    if 0 < _remainders[j] < matchsticks[-1]:
                        continue
                    _remainders.sort(reverse=True)
                    if dfs(i+1, tuple(_remainders)):
                        return True
            return False

        return dfs(0, tuple([side]*4))


@pytest.mark.parametrize('matchsticks, expected', [
    ([1,1,2,2,2], True),
    ([3,3,3,3,4], False),
    ([5,5,5,5,4,4,4,4,3,3,3,3], True),
    ([1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755], False),
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], True),
    ([16,8,8,8,5,1,16,3,11,1,11,12,20,6,6], True),
    ([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4], False),
])
def test(matchsticks, expected):
    assert expected == Solution().makesquare(matchsticks)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
