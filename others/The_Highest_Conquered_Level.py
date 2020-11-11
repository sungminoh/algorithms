#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
With a half of change, you can go one level up and with the other half of
chance you can go one level down.
If you are at zero's level, you can only go up.
What is the expectaion of highest level?

Input
0
Output
0

Input
1
Output
1  # 0 -> 1

Input
2
Output
1.5  # 0 -> 1 -> 2 (The highest level is 2), 0 -> 1 -> 0 (The highest level is 1)
"""

import pytest
from functools import lru_cache

def avg_conquer(n):
    @lru_cache(None)
    def _rec(cur, remain, highest):
        if remain == 0:
            return highest
        if cur == 0:
            return _rec(1, remain - 1, max(highest, cur + 1))
        else:
            return (_rec(cur + 1, remain - 1, max(highest, cur + 1)) / 2) + (_rec(cur - 1, remain - 1, highest) / 2)

    return _rec(0, n, 0)


@pytest.mark.parametrize('n, ans', [
    (0, 0),
    (1, 1),
    (2, 1.5),
    (3, 1.75),
    (4, 2.125),
    (5, 2.375),
])
def test(n, ans):
    assert avg_conquer(n) == ans
