#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

Constraints:

	1 <= points.length <= 300
	points[i].length == 2
	-104 <= xi, yi <= 104
	All the points are unique.
"""
from collections import defaultdict
from functools import lru_cache
from typing import List
import pytest
import sys
from fractions import Fraction, gcd


class Solution:
    def maxPoints(self, points):
        """Nov 04, 2018 07:16"""
        def grad(p1, p2):
            if p1[0] == p2[0]:
                if p1[1] == p2[1]:
                    return None
                else:
                    return float('inf')
            else:
                dy = p1[1] - p2[1]
                dx = p1[0] - p2[0]
                g = gcd(dy, dx)
                return dy/g, dx/g
                # return Fraction(dy, dx)

        if not points:
            return 0
        m = 0
        for i in range(len(points)):
            p1 = points[i]
            itself = 1
            gradients = defaultdict(int)
            major_grad = 0
            for j in range(i+1, len(points)):
                p2 = points[j]
                g = grad(p1, p2)
                if g is not None:
                    gradients[g] += 1
                else:
                    itself += 1
                major_grad = max(major_grad, gradients[g])
            m = max(m, major_grad + itself)
            # print(p1, gradients, itself)
        return m


    def maxPoints(self, points: List[List[int]]) -> int:
        """Mar 05, 2023 14:01"""
        if len(points) <= 2:
            return len(points)

        @lru_cache(None)
        def gcd(x, y):
            if x < 0 or y < 0:
                return gcd(abs(x), abs(y))
            if x < y:
                return gcd(y, x)
            if x % y == 0:
                return y
            return gcd(y, x%y)

        def find_line(x1, y1, x2, y2):
            if x1 == x2:
                return (float('inf'), x1)
            if y1 == y2:
                return (0, y1)
            # y = (dy/dx)x + b
            dy = (y1-y2)
            dx = (x1-x2)
            dg = gcd(dx, dy)
            dydx = (dy//dg, dx//dg)
            b = y1*dydx[1] - x1*dydx[0]
            return (dydx, b)

        def on_line(line, x, y):
            if line[0] == float('inf'):
                return x == line[1]
            elif line[0] == 0:
                return y == line[1]
            dy, dx = line[0]
            return y*dx - x*dy == line[1]

        lines = {}
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                lines[find_line(*points[i], *points[j])] = 0
        for x, y in points:
            for line in lines:
                if on_line(line, x, y):
                    lines[line] += 1

        return max(lines.values())


@pytest.mark.parametrize('args', [
    (([[1,1],[2,2],[3,3]], 3)),
    (([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)),
    (([[1,1],[2,2],[3,3]], 3)),
    (([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4)),
    (([], 0)),
    (([[0,0],[1,1],[0,0]], 3)),
    (([[0,0],[1,65536],[65536,0]], 2)),
    (([[0,0],[94911151,94911150],[94911152,94911151]], 2)),
    (([[-240,-657],[-27,-188],[-616,-247],[-264,-311],[-352,-393],[-270,-748],[3,4],[-308,-87],[150,526],[0,-13],[-7,-40],[-3,-10],[-531,-892],[-88,-147],[4,-3],[-873,-555],[-582,-360],[-539,-207],[-118,-206],[970,680],[-231,-47],[352,263],[510,143],[295,480],[-590,-990],[-236,-402],[308,233],[-60,-111],[462,313],[-270,-748],[-352,-393],[-35,-148],[-7,-40],[440,345],[388,290],[270,890],[10,-7],[60,253],[-531,-892],[388,290],[-388,-230],[340,85],[0,-13],[770,473],[0,73],[873,615],[-42,-175],[-6,-8],[49,176],[308,222],[170,27],[-485,-295],[170,27],[510,143],[-18,-156],[-63,-316],[-28,-121],[396,304],[472,774],[-14,-67],[-5,7],[-485,-295],[118,186],[-154,-7],[-7,-40],[-97,-35],[4,-9],[-18,-156],[0,-31],[-9,-124],[-300,-839],[-308,-352],[-425,-176],[-194,-100],[873,615],[413,676],[-90,-202],[220,140],[77,113],[-236,-402],[-9,-124],[63,230],[-255,-118],[472,774],[-56,-229],[90,228],[3,-8],[81,196],[970,680],[485,355],[-354,-598],[-385,-127],[-2,7],[531,872],[-680,-263],[-21,-94],[-118,-206],[616,393],[291,225],[-240,-657],[-5,-4],[1,-2],[485,355],[231,193],[-88,-147],[-291,-165],[-176,-229],[154,153],[-970,-620],[-77,33],[-60,-111],[30,162],[-18,-156],[425,114],[-177,-304],[-21,-94],[-10,9],[-352,-393],[154,153],[-220,-270],[44,-24],[-291,-165],[0,-31],[240,799],[-5,-9],[-70,-283],[-176,-229],[3,8],[-679,-425],[-385,-127],[396,304],[-308,-352],[-595,-234],[42,149],[-220,-270],[385,273],[-308,-87],[-54,-284],[680,201],[-154,-7],[-440,-475],[-531,-892],[-42,-175],[770,473],[118,186],[-385,-127],[154,153],[56,203],[-616,-247]], 24)),
])
def test(args):
    assert args[-1] == Solution().maxPoints(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
