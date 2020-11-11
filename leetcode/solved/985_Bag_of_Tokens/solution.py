
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

	If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
	If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.

Return the largest number of points we can have after playing any number of tokens.

Example 1:

Input: tokens = [100], P = 50
Output: 0

Example 2:

Input: tokens = [100,200], P = 150
Output: 1

Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2

Note:

	tokens.length
	0
	0
"""
import sys
from functools import lru_cache
from typing import List
import pytest


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        m = 0
        i, j = 0, len(tokens) - 1
        s = 0
        while i <= j:
            moved = False
            while i < len(tokens) and tokens[i] <= P:
                P -= tokens[i]
                s += 1
                m = max(m, s)
                i += 1
                moved = True
            while i < j and s > 0 and P < tokens[i]:
                P += tokens[j]
                s -= 1
                j -= 1
                moved = True
            if not moved:
                break
        return m


@pytest.mark.parametrize('tokens, P, expected', [
    ([100], 50, 0),
    ([100,200], 150, 1),
    ([100,200,300,400], 200, 2),
    ([58,91], 50, 0)
])
def test(tokens, P, expected):
    assert expected == Solution().bagOfTokensScore(tokens, P)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
