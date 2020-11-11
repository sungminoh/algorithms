#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
"""
import sys
from typing import List
import pytest


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points = set()
        s = 0
        nx, ny, mx, my = float('inf'), float('inf'), -float('inf'), -float('inf')
        for x1, y1, x2, y2 in rectangles:
            nx = min(nx, x1)
            ny = min(ny, y1)
            mx = max(mx, x2)
            my = max(my, y2)
            s += (x2-x1)*(y2-y1)
            if (x1, y1) in points:
                points.remove((x1, y1))
            else:
                points.add((x1, y1))
            if (x2, y2) in points:
                points.remove((x2, y2))
            else:
                points.add((x2, y2))
            if (x1, y2) in points:
                points.remove((x1, y2))
            else:
                points.add((x1, y2))
            if (x2, y1) in points:
                points.remove((x2, y1))
            else:
                points.add((x2, y1))
        return s == (mx-nx)*(my-ny) \
            and len(points) == 4 \
            and {(nx, ny), (nx, my), (mx, ny), (mx, my)} == points


@pytest.mark.parametrize('rectangles, expected', [
    ([
        [1,1,3,3],
        [3,1,4,2],
        [3,2,4,4],
        [1,3,2,4],
        [2,3,3,4]
    ], True),

    ([
        [1,1,2,3],
        [1,3,2,4],
        [3,1,4,2],
        [3,2,4,4]
    ], False),
    ([
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [3,2,4,4]
    ], False),
    ([
        [1,1,3,3],
        [3,1,4,2],
        [1,3,2,4],
        [2,2,4,4]
    ], False),
    ([[0,0,1,1],[0,1,3,2],[1,0,2,2]], False)
])
def test(rectangles, expected):
    assert expected == Solution().isRectangleCover(rectangles)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
