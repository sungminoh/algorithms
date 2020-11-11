
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

	All the input integers are in the range [-10000, 10000].
	A valid square has four equal sides with positive length and four equal angles (90-degree angles).
	Input points have no order.
"""
import sys
from typing import List
import pytest


def sqdist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # p1 --diag-- p2, p3, p4
        d12 = sqdist(p1, p2)
        d13 = sqdist(p1, p3)
        d14 = sqdist(p1, p4)
        d23 = sqdist(p2, p3)
        d24 = sqdist(p2, p4)
        d34 = sqdist(p3, p4)

        return (d13 == d14 == d23 == d24 > 0 and d12 == d34) \
            or (d12 == d14 == d23 == d34 > 0 and d13 == d24) \
            or (d12 == d13 == d24 == d34 > 0 and d14 == d23)


@pytest.mark.parametrize('p1, p2, p3, p4, expected', [
    ([0,0], [1,1], [1,0], [0,1], True),
    ([0,0], [-1,0], [1,0], [0,1], False),
    ([0,0], [0,0], [0,0], [0,0], False),
])
def test(p1, p2, p3, p4, expected):
    assert expected == Solution().validSquare(p1, p2, p3, p4)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
