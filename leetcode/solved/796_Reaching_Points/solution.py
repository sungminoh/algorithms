#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.

The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

Example 1:

Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: true
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Example 2:

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: false

Example 3:

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: true

Constraints:

	1 <= sx, sy, tx, ty <= 109
"""
import pytest
import sys
from functools import lru_cache

import numpy as np


class Solution:
    @lru_cache(None)
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """TLE"""
        if sx == tx and sy == ty:
            return True
        ret = False
        if sx + sy <= tx:
            ret |= self.reachingPoints(sx+sy, sy, tx, ty)
        if sx + sy <= ty:
            ret |= self.reachingPoints(sx, sx+sy, tx, ty)
        return ret

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """TLE"""
        q = [(sx, sy)]

        seen = set()
        while q:
            _q = []
            for x, y in q:
                if (x, y) == (tx, ty):
                    return True
                nxts = []
                if x+y <= tx:
                    nxts.append((x+y, y))
                if x+y <= ty:
                    nxts.append((x, x+y))
                for xy in nxts:
                    if xy not in seen:
                        seen.add(xy)
                        _q.append(xy)
            q = _q
        return False

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """Apr 14, 2024 11:32"""
        if sx > tx or sy > ty:
            return False
        if (sx, sy) == (tx, ty):
            return True
        if tx > ty:
            ntx = (tx-ty)%ty + ty*(sx//ty)
            if ntx == tx:
                return False
            return self.reachingPoints(sx, sy, ntx, ty)
        else:
            nty = (ty-tx)%tx + tx*(sy//tx)
            if nty == ty:
                return False
            return self.reachingPoints(sx, sy, tx, nty)


@pytest.mark.parametrize('args', [
    ((1, 1, 3, 5, True)),
    ((1, 1, 2, 2, False)),
    ((1, 1, 1, 1, True)),
    ((35, 13, 455955547, 420098884, False)),
    ((1, 1, 1000000000, 1, True)),
    ((1, 7, 4, 15, False)),
    ((1, 2, 1000000000, 2, False)),
])
def test(args):
    assert args[-1] == Solution().reachingPoints(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
