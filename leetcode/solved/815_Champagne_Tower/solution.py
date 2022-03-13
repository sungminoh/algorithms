#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000

Constraints:

	0 <= poured <= 109
	0 <= query_glass <= query_row < 100
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """09/17/2020 23:41"""
        @lru_cache(None)
        def line(n, r):
            if n < r:
                return [0]*r
            if r == 1:
                return [n]
            pline = line(n, r-1)
            ret = [0]*r
            for i in range(r-1):
                if i == 0:
                    ret[i] = 0.5*max(0, pline[i]-1)
                else:
                    ret[i] = (0.5*max(0, pline[i-1]-1)) + (0.5*max(0, pline[i]-1))
            ret[-1] = 0.5*max(0, pline[-1]-1)
            return ret

        return min(1, line(poured, query_row+1)[query_glass])

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """09/17/2020 23:46"""
        line = [poured]
        for l in range(1, query_row+1):
            _line = [0]*(l+1)
            for i in range(l):
                if i == 0:
                    _line[i] = 0.5*max(0, line[i]-1)
                else:
                    _line[i] = 0.5*max(0, line[i-1]-1) + 0.5*max(0, line[i]-1)
                _line[-1] = 0.5*max(0, line[-1]-1)
            line = _line
        return min(1, line[query_glass])

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """03/12/2022 13:12"""
        @lru_cache(None)
        def flow(p, i, j):
            if p == 0:
                return 0
            if i == 0:
                return p
            ret = 0
            if j > 0:
                ret += max(0, flow(p, i-1, j-1)-1)/2
            if i-1 >= j:
                ret += max(0, flow(p, i-1, j)-1)/2
            return ret

        return min(1, flow(poured, query_row, query_glass))


@pytest.mark.parametrize('poured, query_row, query_glass, expected', [
    (1, 1, 1, 0.00000),
    (2, 1, 1, 0.50000),
    (100000009, 33, 17, 1.00000),
    (25, 6, 1, 0.18750),
])
def test(poured, query_row, query_glass, expected):
    assert expected == Solution().champagneTower(poured, query_row, query_glass)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
