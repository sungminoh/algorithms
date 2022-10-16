#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

	If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
	If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.

Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

Example 1:

Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Example 2:

Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.

Example 3:

Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

Constraints:

	0 <= tokens.length <= 1000
	0 <= tokens[i], power < 104
"""
from typing import List
import pytest
import sys


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

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """09/23/2022 21:48"""
        tokens.sort()
        i, j = 0, len(tokens)-1
        ret = 0
        score = 0
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power -= tokens[i]
                i += 1
                ret = max(ret, score)
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return ret

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """10/03/2022 21:42"""
        ret = 0
        score = 0

        tokens.sort()
        i, j = 0, len(tokens)-1
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                ret = max(ret, score)
                i += 1
            elif score>0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                return ret
        return ret


@pytest.mark.parametrize('tokens, power, expected', [
    ([100], 50, 0),
    ([100,200], 150, 1),
    ([100,200,300,400], 200, 2),
    ([71,55,82], 54, 0),
])
def test(tokens, power, expected):
    assert expected == Solution().bagOfTokensScore(tokens, power)

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
