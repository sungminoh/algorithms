#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:

	1 <= points.length <= 105
	points[i].length == 2
	-231 <= xstart < xend <= 231 - 1
"""
from typing import List
import pytest
import sys


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """May 03, 2020 18:48"""
        points = sorted(points, key=lambda x: x[0])

        def count_shoot(idx=0):
            min_e = float('inf')
            for i in range(idx, len(points)):
                s, e = points[i]
                if s > min_e:
                    return 1 + count_shoot(i)
                else:
                    min_e = min(min_e, e)
            return 1

        if not points:
            return 0
        return count_shoot(0)

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Jan 29, 2022 19:10"""
        points.sort()

        ret = 0
        me = -float('inf')
        for s, e in points:
            if me < s:
                ret += 1
                me = e
            else:
                me = min(me, e)

        return ret

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Mar 04, 2023 21:13"""
        ret = 0
        min_e = -float('inf')
        for s, e in sorted(points):
            if s > min_e:
                min_e = float('inf')
                ret += 1
            min_e = min(min_e, e)
        return ret


@pytest.mark.parametrize('args', [
    (([[10,16],[2,8],[1,6],[7,12]], 2)),
    (([[1,2],[3,4],[5,6],[7,8]], 4)),
    (([[1,2],[2,3],[3,4],[4,5]], 2)),
    (([[10,16],[2,8],[1,6],[7,12]], 2)),
    (([[-2147483648,2147483647]], 1)),
])
def test(args):
    assert args[-1] == Solution().findMinArrowShots(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
