
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
import sys
from typing import List
import pytest


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
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


@pytest.mark.parametrize('points, expected', [
    ([[10,16], [2,8], [1,6], [7,12]], 2),
])
def test(points, expected):
    assert expected == Solution().findMinArrowShots(points)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
