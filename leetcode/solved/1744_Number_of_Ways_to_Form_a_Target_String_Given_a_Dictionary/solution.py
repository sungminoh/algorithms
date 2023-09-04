from pathlib import Path
import json

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

	target should be formed from left to right.
	To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
	Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
	Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

Constraints:

	1 <= words.length <= 1000
	1 <= words[i].length <= 1000
	All strings in words have the same length.
	1 <= target.length <= 1000
	words[i] and target contain only lowercase English letters.
"""
import bisect
from collections import Counter
from collections import defaultdict
from functools import lru_cache
from typing import List
import pytest
import sys


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """TLE"""
        # char -> [(index, count), ...]
        char_indexes = defaultdict(list)
        l = len(words[0])
        for j in range(l):
            for c, cnt in Counter(w[j] for w in words).items():
                char_indexes[c].append((j, cnt))


        def find(j, indexes):
            return indexes[bisect.bisect(indexes, (j, 0)):]


        MOD = int(1e9+7)
        @lru_cache(None)
        def rec(i, j):
            if i == len(target):
                return 1

            ret = 0
            for _j, cnt in find(j, char_indexes[target[i]]):
                ret += (cnt*rec(i+1, _j+1))%MOD
                ret %= MOD
            return ret

        return rec(0, 0)

    def numWays(self, words: List[str], target: str) -> int:
        MOD = int(1e9+7)
        N = len(target)
        M = len(words[0])

        dp = [[0]*M for _ in range(N)]  # N*M
        for i in range(N):
            c = target[i]
            for j in range(M):
                cnt = 0
                for word in words:
                    if word[j] == c:
                        cnt += 1
                mul = 1
                if i > 0:
                    mul = sum(dp[i-1][:j])
                    print(mul, i-1, j-1)
                dp[i][j] = (mul * cnt) % MOD


        return sum(dp[N-1])%MOD

    def numWays(self, words: List[str], target: str) -> int:
        """Sep 03, 2023 20:48"""
        MOD = int(1e9+7)
        N = len(target)
        M = len(words[0])

        dp = [[0]*(M+1) for _ in range(N+1)]  # N*M
        acc = [[0]*(M+1) for _ in range(N+1)]  # N*M

        char_cnt = defaultdict(int)
        for word in words:
            for j in range(M):
                c = word[j]
                char_cnt[(c, j)] += 1

        for i in range(N):
            c = target[i]
            for j in range(M):
                cnt = char_cnt[(c, j)]
                mul = 1
                if i > 0:
                    mul = acc[i-1][j-1]
                dp[i][j] = (mul * cnt) % MOD
                acc[i][j] = acc[i][j-1] + dp[i][j]

        return acc[N-1][M-1]%MOD


@pytest.mark.parametrize('args', [
    ((["acca","bbbb","caca"], "aba", 6)),
    ((["abba","baab"], "bab", 4)),
    ((*json.load(open(Path(__file__).parent/'testcase.json')), 613997185)),
])
def test(args):
    assert args[-1] == Solution().numWays(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
