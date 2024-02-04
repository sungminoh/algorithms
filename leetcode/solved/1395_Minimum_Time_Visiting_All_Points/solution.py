from typing import List

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

	In 1 second, you can either:

		move vertically by one unit,
		move horizontally by one unit, or
		move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).

	You have to visit the points in the same order as they appear in the array.
	You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5

Constraints:

	points.length == n
	1 <= n <= 100
	points[i].length == 2
	-1000 <= points[i][0], points[i][1] <= 1000
"""
import pytest
import sys


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """Feb 04, 2024 09:59"""
        if not points:
            return 0

        def dist(a, b):
            dx = abs(a[0]-b[0])
            dy = abs(a[1]-b[1])
            return max(dx, dy)

        return sum(dist(points[i], points[i+1]) for i in range(len(points)-1))


@pytest.mark.parametrize('args', [
    (([[1,1],[3,4],[-1,0]], 7)),
    (([[3,2],[-2,2]], 5)),
])
def test(args):
    assert args[-1] == Solution().minTimeToVisitAllPoints(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
