
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

Every time you guess wrong, I&#39;ll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

Given a particular n &ge; 1, find out how much money you need to have to guarantee a win.
"""
from functools import lru_cache
import pytest


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def _rec(i, j):
            if i == j:
                return 0
            if i == j-1:
                return i
            if i == j-2:
                return i+1
            bigger_side = float('inf')
            for k in range(i + 1, j):
                left = _rec(i, k - 1)
                right = _rec(k + 1, j)
                current_bigger_side = max(left + k, right + k)
                if current_bigger_side < bigger_side:
                    bigger_side = current_bigger_side
            return bigger_side
        return _rec(1, n)


@pytest.mark.parametrize('n, expected', [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 4),
    (7, 10),
    (20, 49),
    (100, 0),
])
def test(n, expected):
    assert expected == Solution().getMoneyAmount(n)
