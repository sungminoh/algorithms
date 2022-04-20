#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Example 3:

Input: arr = [2,1,3], target = 6
Output: 1
Explanation: (1, 2, 3) occured one time in the array so we return 1.

Constraints:

	3 <= arr.length <= 3000
	0 <= arr[i] <= 100
	0 <= target <= 300
"""
from functools import lru_cache
import sys
from collections import Counter
from typing import List
import pytest


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        TLE. This can be a generic solution with some modification.
        """
        MOD = int(1e9+7)
        cnt = Counter(arr)
        keys = list(sorted(cnt.keys()))

        @lru_cache(None)
        def comb(n, r):
            r = min(r, n-r)
            if r == 0:
                return 1
            # n*n-1*...*n-(r-1)
            # ----------------
            # r*r-1*...*1
            return int(comb(n-1, r-1) * n / r) % MOD

        def backtrack(i, t, cur):
            if t == 0 and sum(cur.values()) == 3:
                ret = 1
                for k, c in cur.items():
                    ret *= comb(cnt[k], c)
                    ret %= MOD
                return ret
            if t < 0 or i < 0 or len(cur) >= 3:
                return 0
            ret = backtrack(i-1, t, cur)
            for c in range(1, cnt[keys[i]]+1):
                if keys[i]*c > t:
                    break
                cur[keys[i]] = c
                ret += backtrack(i-1, t-(c*keys[i]), cur)
                cur.pop(keys[i])
            return ret % MOD

        return backtrack(len(keys)-1, target, {})

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        MOD = int(1e9+7)
        cnt = Counter(arr)
        keys = list(sorted(cnt.keys()))

        ret = 0
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                remainder = target - keys[i] - keys[j]
                if remainder not in cnt or remainder < keys[j]:
                    continue
                cases = 1
                for k, c in Counter([remainder, keys[i], keys[j]]).items():
                    numerator = 1
                    denominator = 1
                    for _c in range(c):
                        numerator *= cnt[k] - _c
                        denominator *= _c+1
                    cases *= (numerator // denominator)
                    cases %= MOD

                ret += cases
                ret %= MOD
        return ret


@pytest.mark.parametrize('arr, target, expected', [
    ([1,1,2,2,3,3,4,4,5,5], 8, 20),
    ([1,1,2,2,2,2], 5, 12),
    ([2,1,3], 6, 1),
    ([0,0,0], 0, 1),
    ([33,2,78,17,71,16,97,73,55,68,64,45,47,8,1,69,39,52,30,86,1,30,7,28,78,4,80,62,44,96,100,16,72,67,64,20,66,40,67,33,67,34,23,76,1,15,42,87,29,3,98,11,29,46,44,31,3,63,13,24,84,86,51,10,21,3,74,10,22,32,85,59,28,14,12,60,100,37,40,26,93,93,26,79,17,31,42,74,28,64,98,96,18,19,32,18,6,8,98,63], 137, 1162),
])
def test(arr, target, expected):
    assert expected == Solution().threeSumMulti(arr, target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
