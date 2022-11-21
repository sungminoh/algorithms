#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

	-1: Your guess is higher than the number I picked (i.e. num > pick).
	1: Your guess is lower than the number I picked (i.e. num < pick).
	0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

Constraints:

	1 <= n <= 231 - 1
	1 <= pick <= n
"""
import pytest
import sys


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
pick = -1
def guess(num: int) -> int:
    if num < pick:
        return 1
    if num > pick:
        return -1
    return 0


class Solution:
    def test(self, n: int, pick: int) -> int:
        globals()['pick'] = pick
        return self.guessNumber(n)

    def guessNumber(self, n: int) -> int:
        """10/20/2021 20:55"""
        s, e = 1, n

        while True:
            m = s + ((e-s)//2)
            g = guess(m)
            if g < 0:
                e = m-1
            elif g > 0:
                s = m+1
            else:
                return m

    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = l + (r-l)//2
            if guess(m) < 0:
                r = m-1
            elif guess(m) > 0:
                l = m+1
            else:
                return m


@pytest.mark.parametrize('n, pick, expected', [
    (10, 6, 6),
    (1, 1, 1),
    (2, 1, 1),
])
def test(n, pick, expected):
    assert expected == Solution().test(n, pick)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
