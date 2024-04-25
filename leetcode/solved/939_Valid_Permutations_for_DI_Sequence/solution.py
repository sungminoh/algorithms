#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a string s of length n where s[i] is either:

	'D' means decreasing, or
	'I' means increasing.

A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

	If s[i] == 'D', then perm[i] > perm[i + 1], and
	If s[i] == 'I', then perm[i] < perm[i + 1].

Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: s = "DID"
Output: 5
Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

Example 2:

Input: s = "D"
Output: 1

Constraints:

	n == s.length
	1 <= n <= 200
	s[i] is either 'I' or 'D'.
"""
from functools import lru_cache
import pytest
import sys


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        """Apr 24, 2024 20:56"""
        MOD = int(1e9 + 7)

        @lru_cache(None)
        def dp(n, p):
            if p > n:
                return 0
            if n == 0:
                return 1
            decrease = s[n-1] == 'D'
            ret = 0
            if decrease:
                for q in range(p, n):
                    ret += dp(n-1, q)
            else:
                for q in range(p):
                    ret += dp(n-1, q)
            return ret % MOD

        N = len(s)
        return sum(dp(N, i) for i in range(N+1)) % MOD



@pytest.mark.parametrize('args', [
    (("DID", 5)),
    (("D", 1)),
])
def test(args):
    assert args[-1] == Solution().numPermsDISequence(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
