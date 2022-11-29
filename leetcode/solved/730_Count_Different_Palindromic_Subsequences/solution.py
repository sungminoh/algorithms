#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.

Example 1:

Input: s = "bccb"
Output: 6
Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:

Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
Output: 104860361
Explanation: There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 109 + 7.

Constraints:

	1 <= s.length <= 1000
	s[i] is either 'a', 'b', 'c', or 'd'.
"""
from functools import lru_cache
import bisect
from collections import deque
from collections import defaultdict
from collections import Counter
import pytest
import sys


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """11/28/2022 19:22, TLE"""
        MOD = 10**9 + 7
        letter_positions = defaultdict(list)
        for i, c in enumerate(s):
            letter_positions[c].append(i)

        @lru_cache(None)
        def dp(i, j, l):
            if i > j or i >= len(s) or j<0:
                return 0
            if l == 1:
                return len(set(s[i:j+1])) % MOD
            if l == 2:
                cnt = Counter(s[i:j+1])
                return sum(1 if v>=2 else 0 for v in cnt.values()) % MOD
            ret = 0
            for c, pos in letter_positions.items():
                a = bisect.bisect_left(pos, i)
                b = bisect.bisect_right(pos, j)-1
                if 0<=a<len(pos) and 0<=b<len(pos):
                    ret += dp(pos[a]+1, pos[b]-1, l-2)
                    ret %= MOD
            return ret

        ret = 0
        for l in range(1, len(s)+1):
            ret += dp(0, len(s)-1, l)
            ret %= MOD
        return ret

    def countPalindromicSubsequences(self, s: str) -> int:
        """11/28/2022 19:38, TLE"""
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(s, l):
            if not s or len(s)<l:
                return 0
            if l == 1:
                return len(set(s)) % MOD
            if l == 2:
                cnt = Counter(s)
                return sum(1 if v>=2 else 0 for v in cnt.values()) % MOD
            ret = 0
            chars = set(s)
            i = 0
            while i < len(s):
                j = len(s)-1
                while j > i and s[j] != s[i]:
                    j -= 1
                ret += dp(s[i+1:j], l-2)
                ret %= MOD
                chars.remove(s[i])
                while i < len(s) and s[i] not in chars:
                    i += 1
            return ret

        ret = 0
        for l in range(1, len(s)+1):
            ret += dp(s, l)
            ret %= MOD
        return ret

    def countPalindromicSubsequences(self, s: str) -> int:
        """11/28/2022 20:12, TLE"""
        MOD = 10**9 + 7
        fwd = {}
        bwd = {}
        for i, c in enumerate(s):
            fwd.setdefault(c, [])
            while len(fwd[c]) <= i:
                fwd[c].append(i)
            bwd.setdefault(c, [])
            while len(bwd[c]) < i:
                bwd[c].append(-1 if len(bwd[c])==0 else bwd[c][-1])
            bwd[c].append(i)
        for v in fwd.values():
            v.extend([-1]*(len(s)-len(v)))
        for v in bwd.values():
            v.extend([v[-1]]*(len(s)-len(v)))
        chars = set(s)

        @lru_cache(None)
        def dp(i, j, l):
            if i > j or i >= len(s) or j<0:
                return 0
            if l == 1:
                return len(set(s[i:j+1])) % MOD
            if l == 2:
                cnt = Counter(s[i:j+1])
                return sum(1 if v>=2 else 0 for v in cnt.values()) % MOD
            ret = 0
            for c in chars:
                a, b = fwd[c][i], bwd[c][j]
                if 0<=a<len(s) and 0<=b<len(s):
                    ret += dp(a+1, b-1, l-2)
                    ret %= MOD
            return ret

        ret = 0
        for l in range(1, len(s)+1):
            ret += dp(0, len(s)-1, l)
            ret %= MOD
        return ret

    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        fwd = {}
        bwd = {}
        for i, c in enumerate(s):
            fwd.setdefault(c, [])
            while len(fwd[c]) <= i:
                fwd[c].append(i)
            bwd.setdefault(c, [])
            while len(bwd[c]) < i:
                bwd[c].append(-1 if len(bwd[c])==0 else bwd[c][-1])
            bwd[c].append(i)
        for v in fwd.values():
            v.extend([-1]*(len(s)-len(v)))
        for v in bwd.values():
            v.extend([v[-1]]*(len(s)-len(v)))
        chars = set(s)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 1
            ret = 1  # empty string
            for c in chars:
                a, b = fwd[c][i], bwd[c][j]
                if a == -1 or b < i or a > j:
                    continue
                ret += 1  # single char
                if a < b:
                    ret += dp(a+1, b-1)
                    ret %= MOD
            return ret

        return dp(0, len(s)-1)-1


@pytest.mark.parametrize('s, expected', [
    ("bccb", 6),
    ("abcddbca", 26),
    ("aaaaa", 5),
    ("aabbaa", 10),
    ("acaccbbdcddaacddaccd", 201),
    ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", 104860361),
    ("bacdcbbcbadcddcbabddbabcaabaacaabbbdcbdacbbadcdbcbdadaaaddddbccbcbcbccaabcdcaddadbdddcacaacbcdbbdabacdddcaaddaabbddabccabbbadbabbdcbaccbcabbdbcbbadbdbcabbbaccadbdadbabddbdcbbddaabdcddbbcadaacaadaccdca", 829276122),
    ("abbadbcacbbdadadadcbdccdbdbcdacbcbabacbbccdadbbcacaacdbcdcdadacacaabcaddcdbbbbccdcdddbdddaabdccbaccccabbdacacadcddcadaacaabccbabbbdaabcaabadbbdcacbbdbccbadadbcdcdbadcbcbaabbbbcadaaaccaccdabbbadbcababa", 703613271),
    ("cdabbbbccdcddacbccccbbddbdbdbaabaaaabbbabbaccacabadccddbcbbcbbaccddacbdcaabaacabbbbaadbbcbdcddacabccbcbdbcbcbbccdadcccbcddcbabdbabaabccdaabacddaacbaccdccabbccbbcdbdadbbdcdcccbcaacaccaaccdcbcdbbddddcda", 571801983),
])
def test(s, expected):
    assert expected == Solution().countPalindromicSubsequences(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
