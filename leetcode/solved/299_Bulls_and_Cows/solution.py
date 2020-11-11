#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

	The number of "bulls", which are digits in the guess that are in the correct position.
	The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"

Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"

Constraints:

	1 <= secret.length, guess.length <= 1000
	secret.length == guess.length
	secret and guess consist of digits only.
"""
import sys
from collections import Counter
import pytest


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = Counter(secret)
        bulls = 0
        for i, (a, b) in enumerate(zip(secret, guess)):
            if a == b:
                bulls += 1
                cnt[a] -= 1
        cows = 0
        for i, c in enumerate(guess):
            if secret[i] == c:
                continue
            if cnt[c] > 0:
                cnt[c] -= 1
                cows += 1
        return f'{bulls}A{cows}B'


@pytest.mark.parametrize('secret, guess, expected', [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B"),
    ("1", "0", "0A0B"),
    ("1", "1", "1A0B"),
])
def test(secret, guess, expected):
    assert expected == Solution().getHint(secret, guess)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
