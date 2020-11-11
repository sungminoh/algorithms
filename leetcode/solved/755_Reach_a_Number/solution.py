#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are standing at position 0 on an infinite number line.  There is a goal at position target.

On each move, you can either go left or right.  During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""
import sys
from functools import lru_cache
import pytest


class Solution:
    def reachNumber(self, target: int) -> int:
        # (n-1)^2 <n*n-n < 2*target < n*n+n
        if target < 0:
            return self.reachNumber(-target)
        n = int(pow(2*target, 0.5))
        while n*(n+1)/2 < target:
            n += 1
        s = n*(n+1)//2
        d = s - target
        if  d % 2 == 0:
            return n
        else:
            return n+1 if n%2 == 0 else n+2

    def _reachNumber(self, target: int) -> int:
        n = 0
        visited = set()
        positions = {0}
        while True:
            if target in positions:
                return n
            n += 1
            _positions = set()
            for p in positions:
                _positions.add(p + n)
                _positions.add(p - n)
            positions = _positions


@pytest.mark.parametrize('target, expected', [
    (3, 2),
    (2, 3),
    (-1000000000, 44723),
    (5, 5),
])
def test(target, expected):
    assert expected == Solution().reachNumber(target)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
