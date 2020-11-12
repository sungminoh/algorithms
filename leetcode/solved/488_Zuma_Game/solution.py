#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Constraints:

	You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
	1 <= board.length <= 16
	1 <= hand.length <= 5
	Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""
from functools import lru_cache
import sys
from collections import Counter
import pytest


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def compress(b):
            i = 0
            while i < len(b):
                j = i
                while j < len(b) and b[i] == b[j]:
                    j += 1
                if i + 3 <= j:
                    return compress(b[:i]+b[j:])
                i = j
            return b

        def dfs(b, h):
            if not b:
                return 0
            ret = float('inf')
            i = 0
            while i < len(b):
                j = i
                while j < len(b) and b[i] == b[j]:
                    j += 1
                n = 3-(j-i)
                if h[b[i]] >= n:
                    h[b[i]] -= n
                    ret = min(ret, dfs(compress(b[:i] + b[j:]), h) + n)
                    h[b[i]] += n
                i = j
            return ret

        @lru_cache(None)
        def dfs(b, h):
            if not b:
                return 0
            h = ''.join(x for x in h if x in set(b))
            ret = float('inf')
            for i, c in enumerate(b):
                for j, d in enumerate(h):
                    ret = min(ret, 1 + dfs(compress(b[:i] + d + b[i:]), h[:j] + h[j+1:]))
            return ret

        # h = Counter(hand)
        m = dfs(board, hand)
        return m if m < float('inf') else -1

    def _findMinStep(self, board, hand):
        def dfs(s, c):
            if not s: return 0
            res, i = float("inf"), 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[i] == s[j]: j += 1
                incr = 3 - (j - i)
                if c[s[i]] >= incr:
                    incr = 0 if incr < 0 else incr
                    c[s[i]] -= incr
                    tep = dfs(s[:i] + s[j:], c)
                    if tep >= 0: res = min(res, tep + incr)
                    c[s[i]] += incr
                i = j
            return res if res != float("inf") else -1
        return dfs(board, Counter(hand))


@pytest.mark.parametrize('board, hand, expected', [
    ("WRRBBW", "RB", -1),
    ("WWRRBBWW", "WRBRW", 2),
    ("G", "GGGGG", 2),
    ("RBYYBBRRB", "YRBGB", 3),
    ("RRWWRRBBRR", "WB", 2),
    ("WWBBWBBWW", "BB", -1),
])
def test(board, hand, expected):
    print()
    assert expected == Solution().findMinStep(board, hand)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
