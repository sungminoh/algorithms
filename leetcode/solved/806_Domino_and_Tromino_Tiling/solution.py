#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X

Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY

Note:

	N  will be in range [1, 1000].
"""
import sys
import pytest


class Solution:
    def numTilings(self, N: int) -> int:
        if N == 0:
            return 1
        if N == 1:
            return 1
        if N == 2:
            return 2
        s = 1
        ret = [1, 1, 2]
        for i in range(3, N+1):
            ret[i%3] = (ret[i%3-1] + ret[i%3-2] + 2*s) % (1e9+7)
            s += ret[i%3-2]
            s %= 1e9+7
        return int(ret[N%3] % (1e9+7))


@pytest.mark.parametrize('N, expected', [
    (0, 1),
    (1, 1),
    (3, 5),
    (4, 11),
    (30, 312342182),
    (60, 882347204)
])
def test(N, expected):
    assert expected == Solution().numTilings(N)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
