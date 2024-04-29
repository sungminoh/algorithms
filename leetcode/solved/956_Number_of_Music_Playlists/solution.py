#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

	Every song is played at least once.
	A song can only be played again only if k other songs have been played.

Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].

Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].

Constraints:

	0 <= k < n <= goal <= 100
"""
from pprint import pprint
from functools import reduce
import itertools
from collections import defaultdict
import pytest
import sys


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """Memory Limit Exceeded"""
        MOD = int(1e9+7)
        numbers = set(range(n))

        queue = {(tuple(), tuple()): 1}  # seq, used, cnt
        for i in range(goal):
            _queue = defaultdict(int)
            for (seq, used), cnt in queue.items():
                unused = numbers - set(used)
                for c in unused:
                    _seq = seq + (c, )
                    _seq = tuple(_seq[-k:]) if k != 0 else tuple()
                    _queue[_seq, used + (c, )] += cnt
                to_reuse = set(used) - set(seq)
                for c in to_reuse:
                    _seq = seq + (c, )
                    _seq = tuple(_seq[-k:]) if k != 0 else tuple()
                    _queue[_seq, used] += cnt
            queue = {k: v%MOD for k, v in _queue.items()}
        ret = 0
        for (seq, used), cnt in queue.items():
            if len(used) == n:
                ret += cnt
        return ret % MOD

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """Apr 26, 2024 19:58"""
        MOD = int(1e9+7)

        dp = {1: n}
        for i in range(1, goal):
            _dp = defaultdict(int)
            for used, cnt in dp.items():
                _dp[used] += cnt * (used-min(i, k))
                _dp[used+1] += cnt * (n-used)
            dp = {k: v % MOD for k, v in _dp.items()}

        return dp[n]


@pytest.mark.parametrize('args', [
    ((3, 3, 1, 6)),
    ((2, 3, 0, 6)),
    ((2, 3, 1, 2)),
    ((16, 16, 4, 789741546)),
])
def test(args):
    assert args[-1] == Solution().numMusicPlaylists(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
