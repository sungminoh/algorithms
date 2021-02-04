#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:

Input: points = [[1,1]]
Output: 0

Constraints:

	n == points.length
	1 <= n <= 500
	points[i].length == 2
	-104 <= xi, yi <= 104
	All the points are unique.
"""
import sys
from collections import defaultdict
from typing import List
import pytest


def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        m = [defaultdict(list) for _ in points]
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                p2 = points[j]
                d = dist(p1, p2)
                m[i][d].append(j)
                m[j][d].append(i)
        ret = 0
        for dist_points in m:
            for d, ps in dist_points.items():
                if len(ps) >= 2:
                    ret += len(ps) * (len(ps)-1)
        return ret


@pytest.mark.parametrize('points, expected', [
    ([[0,0],[1,0],[2,0]], 2),
    ([[1,1],[2,2],[3,3]], 2),
    ([[1,1]], 0),
])
def test(points, expected):
    assert expected == Solution().numberOfBoomerangs(points)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
