#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:

Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:

Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them.

Note:

	All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
	All input integers will range from 0 to 100.
	The garden has at least one tree.
	All coordinates are distinct.
	Input points have NO order. No order required for output.
	input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
import math
import sys
from typing import List
import pytest


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


def dist(x, y):
    return ((x[1]-y[1])**2 + (x[0]-y[0])**2)**0.5


def orientation(a, b, c):
    return ((c[1]-a[1]) * (b[0]-a[0])) - ((b[1]-a[1]) * (c[0]-a[0]))


def grad(a, b):
    if a[0] == b[0]:
        return float('inf') if b[1] > a[1] else -float('inf')
    return (a[1]-b[1]) / (a[0]-b[0])


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
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

    def _outerTrees(self, points: List[List[int]]) -> List[List[int]]:
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
        print((99, 27) in ret)
        return [list(x) for x in ret]
        # return ret


@pytest.mark.parametrize('points, expected', [
    ([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]], [[1,1],[2,0],[4,2],[3,3],[2,4]]),
    ([[1,2],[2,2],[4,2]], [[1,2],[2,2],[4,2]]),
    ([[3,7],[6,8],[7,8],[11,10],[4,3],[8,5],[7,13],[4,13]], [[4,13],[4,3],[3,7],[8,5],[11,10],[7,13]]),
    ([[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]], [[7,4],[5,0],[7,3],[2,1],[5,5],[4,5],[3,5],[7,2],[1,2],[1,4],[4,0],[2,5],[6,1],[6,5],[0,3],[3,0]]),
    ([[10,11],[10,44],[10,46],[11,17],[11,21],[11,28],[11,36],[11,41],[12,17],[12,18],[12,19],[12,30],[12,41],[12,43],[12,48],[13,15],[13,39],[13,42],[13,43],[13,49],[14,21],[14,22],[14,27],[14,32],[14,34],[14,41],[14,47],[15,17],[15,19],[15,20],[15,24],[15,43],[15,44],[16,13],[16,15],[16,49],[17,27],[17,28],[17,30],[18,12],[18,23],[18,33],[18,39],[18,40],[18,42],[19,23],[19,32],[19,35],[19,47],[20,11],[20,34],[20,44],[21,19],[21,33],[21,46],[21,48],[22,36],[23,10],[23,16],[23,26],[24,17],[24,18],[24,23],[24,24],[24,33],[24,41],[25,33],[25,35],[25,36],[25,37],[25,48],[26,13],[26,29],[26,37],[27,31],[27,42],[27,43],[28,22],[28,40],[28,45],[28,47],[29,11],[29,18],[29,28],[29,29],[30,10],[30,16],[30,26],[30,28],[30,31],[30,35],[30,37],[30,39],[31,25],[31,35],[31,39],[31,40],[32,21],[32,24],[32,35],[32,36],[32,38],[32,41],[32,45],[33,24],[33,47],[34,19],[34,26],[34,29],[34,31],[35,11],[35,30],[35,39],[36,11],[36,19],[36,39],[36,45],[37,32],[38,23],[38,25],[38,37],[38,42],[38,48],[39,21],[39,29],[39,33],[39,39],[40,14],[40,23],[40,26],[40,40],[41,40],[42,16],[42,32],[43,13],[43,20],[43,32],[43,33],[43,37],[44,44],[44,49],[45,13],[45,16],[45,18],[45,33],[45,42],[45,48],[46,11],[46,26],[46,37],[46,43],[47,18],[47,26],[47,38],[48,11],[48,14],[48,16],[48,19],[48,25],[49,27],[49,30],[49,31],[49,45],[49,46],[50,12],[50,16],[50,18],[50,23],[51,13],[51,44],[52,27],[52,41],[52,43],[52,44],[52,48],[53,11],[53,14],[53,24],[53,27],[53,36],[53,44],[54,12],[54,15],[54,24],[54,30],[54,35],[54,38],[54,41],[54,43],[54,49],[55,17],[55,20],[55,30],[55,35],[55,40],[55,46],[55,49],[56,10],[56,11],[56,26],[56,44],[56,46],[56,48],[57,13],[57,37],[57,38],[58,22],[59,13],[59,14],[59,16],[59,28],[59,34],[59,41],[59,42],[59,47],[59,48],[60,19],[60,20],[60,29],[60,34],[61,30],[61,33],[61,44],[62,20],[62,37],[62,39],[62,48],[63,34],[63,39],[63,40],[64,12],[64,24],[64,33],[65,11],[65,14],[65,21],[65,31],[65,33],[65,39],[65,42],[65,47],[65,49],[66,14],[66,24],[66,29],[66,47],[67,14],[67,17],[67,22],[67,30],[67,38],[67,44],[67,45],[68,21],[68,25],[68,32],[68,36],[68,40],[68,48],[69,10],[69,45],[70,31],[70,32],[70,34],[70,41],[70,44],[70,46],[71,17],[71,20],[71,21],[71,32],[71,35],[72,12],[72,43],[72,44],[73,15],[73,43],[73,46],[73,47],[73,48],[73,49],[74,15],[74,25],[74,33],[75,19],[76,22],[76,34],[76,40],[76,42],[76,47],[77,19],[77,21],[77,38],[77,48],[78,32],[78,34],[78,35],[78,37],[78,40],[79,22],[79,28],[79,32],[79,33],[79,39],[79,46],[80,35],[80,44],[81,21],[81,23],[81,25],[82,13],[82,35],[82,41],[83,32],[84,10],[84,18],[84,26],[84,36],[84,40],[85,16],[85,18],[85,22],[85,33],[86,25],[86,31],[87,33],[87,39],[87,40],[87,41],[88,10],[88,42],[88,44],[89,22],[89,23],[89,36],[90,15],[90,20],[90,34],[91,49],[92,12],[92,14],[92,16],[92,17],[92,31],[92,48],[93,16],[93,27],[93,29],[93,40],[93,46],[94,27],[94,31],[94,34],[94,36],[94,39],[95,12],[95,19],[95,27],[95,34],[95,42],[96,14],[96,30],[96,38],[96,41],[96,47],[97,12],[97,17],[97,20],[97,21],[97,23],[97,31],[97,33],[97,34],[98,30],[98,34],[98,48],[99,11],[99,19],[99,27]], [[65,49],[23,10],[88,10],[10,11],[13,49],[16,49],[98,48],[12,48],[44,49],[73,49],[99,27],[56,10],[10,46],[10,44],[91,49],[84,10],[99,11],[30,10],[54,49],[69,10],[55,49],[99,19]]),
    ([[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]], [[7,2],[5,2],[6,2],[1,2],[2,2],[4,2]])
])
def test(points, expected):
    print()
    actual = Solution().outerTrees(points)
    print(actual)
    assert set(tuple(x) for x in expected) == set(tuple(x) for x in actual)
    assert len(expected) == len(actual)
    # assert sorted(expected) == sorted(actual)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
