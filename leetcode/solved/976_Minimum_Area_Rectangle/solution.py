
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:

	1
	0
	0
	All points are distinct.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


def min_gap(s):
    s = sorted(list(s))
    g = float('inf')
    for i in range(1, len(s)):
        g = min(g, s[i] - s[i - 1])
    return g

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xy = defaultdict(set)
        for p in points:
            x, y = p
            xy[x].add(y)

        area = float('inf')
        xs = list(xy.keys())
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                x1, x2 = xs[i], xs[j]
                ys1 = xy[x1]
                ys2 = xy[x2]
                inter = ys1.intersection(ys2)
                if len(inter) >= 2:
                    area = min(area, abs(x1 - x2) * min_gap(inter))
        return area if area < float('inf') else 0


@pytest.mark.parametrize('points, expected', [
    ([[1,1],[1,3],[3,1],[3,3],[2,2]], 4),
    ([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]], 2),
    ([[0,1],[3,2],[5,5],[4,5],[4,4],[2,0],[2,3],[2,2],[1,0],[5,1],[2,5],[5,2],[2,4],[4,0]], 2)
])
def test(points, expected):
    assert expected == Solution().minAreaRect(points)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
