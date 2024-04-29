#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Constraints:

	1 <= s.length <= 2000
	s consists of lowercase English letters.
"""
import pytest
import sys


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """TLE"""
        MOD = int(1e9+7)
        seq = set()
        def dfs(i, acc):
            if i == len(s):
                seq.add(''.join(acc))
                return
            dfs(i+1, acc)
            acc.append(s[i])
            dfs(i+1, acc)
            acc.pop()
        dfs(0, [])
        return (len(seq)-1) % MOD

    def distinctSubseqII(self, s: str) -> int:
        """Memory Limit Exceeded"""
        MOD = int(1e9+7)
        seq = set()
        seen = set()
        def dfs(i, acc):
            if (i, acc) in seen:
                return
            seen.add((i, acc))
            if i == len(s):
                seq.add(acc)
                return
            dfs(i+1, acc)
            dfs(i+1, acc + s[i])
        dfs(0, '')
        return (len(seq)-1) % MOD

    def distinctSubseqII(self, s: str) -> int:
        """TLE"""
        MOD = int(1e9+7)
        queue = set([''])
        for i, c in enumerate(s):
            queue.update([acc + c for acc in queue])
        return (len(queue)-1) % MOD

    def distinctSubseqII(self, s: str) -> int:
        """Apr 28, 2024 15:18"""
        MOD = int(1e9+7)
        dp = {}  # the number of subseq ends with a key
        for c in s:
            dp[c] = (sum(dp.values()) + 1) % MOD
        return sum(dp.values()) % MOD


@pytest.mark.parametrize('args', [
    (("abc", 7)),
    (("aba", 6)),
    (("aaa", 3)),
    (("pcrdhwdxmqdznbenhwjsenjhvulyve", 836817663)),
])
def test(args):
    assert args[-1] == Solution().distinctSubseqII(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
