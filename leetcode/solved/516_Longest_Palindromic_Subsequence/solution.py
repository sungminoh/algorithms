from functools import lru_cache
from collections import Counter
from collections import defaultdict
import itertools

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:

	1 <= s.length <= 1000
	s consists only of lowercase English letters.
"""
import pytest
import sys


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """May 31, 2020 13:18"""
        if len(Counter(s)) == 1:
            return len(s)
        @lru_cache(None)
        def rec(i, j):
            if j < i:
                return 0
            if i == j:
                return 1
            m = -float('inf')
            if s[i] == s[j]:
                m = max(m, rec(i + 1, j - 1) + 2)
            m = max(m, rec(i+1, j))
            m = max(m, rec(i, j-1))
            return m
        return rec(0, len(s)-1)

    def longestPalindromeSubseq(self, s: str) -> int:
        """May 31, 2020 13:20"""
        if len(Counter(s)) == 1:
            return len(s)

        @lru_cache(None)
        def rec(i, j):
            if j < i:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return rec(i + 1, j - 1) + 2
            else:
                return max(rec(i+1, j), rec(i, j-1))
        return rec(0, len(s)-1)

    def longestPalindromeSubseq(self, s: str) -> int:
        """TLE"""
        if len(Counter(s)) == 1:
            return len(s)

        adding_stacks = defaultdict(set)  # c -> stacks end with c
        popping_stacks = defaultdict(set)
        ret = 0
        for c in s:
            new_popping_stacks = defaultdict(set)
            for cnt, stack in popping_stacks.get(c, set()):
                popped = stack[:-1]
                if popped == '':
                    ret = max(ret, cnt+1)
                else:
                    new_popping_stacks[popped[-1]].add((cnt+1, popped))
            for stack in adding_stacks.get(c, set()):
                popped = stack[:-1]
                if popped == '':
                    ret = max(ret, 2)
                else:
                    new_popping_stacks[popped[-1]].add((len(stack)+1, popped))
            for k, v in new_popping_stacks.items():
                popping_stacks[k].update(v)

            new_stacks = set([c])
            for stack in itertools.chain(*adding_stacks.values()):
                new_stacks.add(stack + c)
            adding_stacks[c].update(new_stacks)

        if not s:
            return 0
        return max(1, ret)

    def longestPalindromeSubseq(self, s: str) -> int:
        """Sep 02, 2023 18:22"""
        if len(Counter(s)) == 1:
            return len(s)

        N = len(s)

        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1

        for k in range(1, N):
            for i in range(N-k):
                j = i+k
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][N-1]


@pytest.mark.parametrize('args', [
    (("bbbab", 4)),
    (("cbbd", 2)),
    (("a", 1)),
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 998)),
])
def test(args):
    assert args[-1] == Solution().longestPalindromeSubseq(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
