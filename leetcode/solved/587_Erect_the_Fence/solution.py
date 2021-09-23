#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:

Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:

Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

Constraints:

	1 <= points.length <= 3000
	points[i].length == 2
	0 <= xi, yi <= 100
	All the given points are unique.
"""
import math
import sys
from typing import List
import pytest


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """11/14/2020 12:24"""
        def dist(x, y):
            return ((x[1]-y[1])**2 + (x[0]-y[0])**2)**0.5

        def radian(a, b):
            x = (b[0]-a[0])
            y = (b[1]-a[1])
            [0, 1]
            rad = math.acos(y / ((x**2 + y**2)**0.5))
            if x == 0:
                return math.pi if y < 0 else 0
            if x < 0:
                return 2*math.pi - rad
            return round(rad, 10)

        left_bottom_most = min(points)
        boundary = [left_bottom_most]
        ret = set([tuple(left_bottom_most)])
        max_rad = -float('inf')
        while True:
            poles = []
            min_rad = float('inf')
            for p in points:
                if p == boundary[-1]:
                    continue
                g = radian(boundary[-1], p)
                if max_rad < g < min_rad:
                    min_rad = g
                    poles = [p]
                elif g == min_rad:
                    poles.append(p)
            if not poles:
                break
            max_dist = -float('inf')
            furthest_pole_index = -1
            for i, pole in enumerate(poles):
                d = dist(pole, boundary[-1])
                if d > max_dist:
                    max_dist = d
                    furthest_pole_index = i
            # print('---------------------')
            # print(boundary[-1], poles, furthest_pole_index)
            for i, pole in enumerate(poles):
                if i != furthest_pole_index:
                    ret.add(tuple(pole))
            # if poles[furthest_pole_index] in ret:
                # break
            boundary.append(poles[furthest_pole_index])
            ret.add(tuple(poles[furthest_pole_index]))
            max_rad = min_rad
        return [list(x) for x in ret]

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """11/19/2020 22:50"""
        def orientation(a, b, c):
            return ((c[1]-a[1]) * (b[0]-a[0])) - ((b[1]-a[1]) * (c[0]-a[0]))

        if len(points) <= 3:
            return points

        points.sort()
        # print('points: ', points)
        upper = []
        for p in points:
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) > 0:
                upper.pop()
            upper.append(p)

        lower = []
        for p in points:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        return list(map(list, {tuple(p) for p in upper}.union({tuple(p) for p in lower})))

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 3:
            return trees

        def ori(a, b, c):
            """Pos: inc, Neg: dec"""
            return ((b[1]-c[1]) * (a[0]-b[0])) - ((b[0]-c[0]) * (a[1]-b[1]))

        trees.sort()
        upper = []
        for i in range(len(trees)):
            while len(upper) >= 2 and ori(upper[-2], upper[-1], trees[i])>0:
                upper.pop()
            upper.append(trees[i])

        trees.reverse()
        lower = []
        for i in range(len(trees)):
            while len(lower) >= 2 and ori(lower[-2], lower[-1], trees[i])>0:
                lower.pop()
            lower.append(trees[i])

        return list(set([*[tuple(x) for x in upper], *[tuple(x) for x in lower[1:-1]]]))


@pytest.mark.parametrize('trees, expected', [
    ([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]], [[1,1],[2,0],[3,3],[2,4],[4,2]]),
    ([[1,2],[2,2],[4,2]], [[4,2],[2,2],[1,2]]),
    ([[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]], [[4,2],[5,2],[1,2],[2,2],[7,2],[6,2]])
])
def test(trees, expected):
    print()
    assert set(tuple(x) for x in expected) == set(tuple(x) for x in Solution().outerTrees(trees))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
