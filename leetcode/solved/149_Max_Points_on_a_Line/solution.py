#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
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

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
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

"""
from collections import defaultdict
from fractions import Fraction, gcd


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return 'Point(%r, %r)' % (self.x, self.y)


class Solution:
    def grad(self, p1, p2):
        if p1.x == p2.x:
            if p1.y == p2.y:
                return None
            else:
                return float('inf')
        else:
            dy = p1.y - p2.y
            dx = p1.x - p2.x
            g = gcd(dy, dx)
            return dy/g, dx/g
            # return Fraction(dy, dx)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
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
                g = self.grad(p1, p2)
                if g is not None:
                    gradients[g] += 1
                else:
                    itself += 1
                major_grad = max(major_grad, gradients[g])
            m = max(m, major_grad + itself)
            # print(p1, gradients, itself)
        return m


def main():
    examples = []
    examples.append(([[1,1],[2,2],[3,3]], 3))
    examples.append(([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4))
    examples.append(([], 0))
    examples.append(([[0,0],[1,1],[0,0]], 3))
    examples.append(([[0,0],[1,65536],[65536,0]], 2))
    examples.append(([[0,0],[94911151,94911150],[94911152,94911151]], 2))
    examples.append(([[-240,-657],[-27,-188],[-616,-247],[-264,-311],[-352,-393],[-270,-748],[3,4],[-308,-87],[150,526],[0,-13],[-7,-40],[-3,-10],[-531,-892],[-88,-147],[4,-3],[-873,-555],[-582,-360],[-539,-207],[-118,-206],[970,680],[-231,-47],[352,263],[510,143],[295,480],[-590,-990],[-236,-402],[308,233],[-60,-111],[462,313],[-270,-748],[-352,-393],[-35,-148],[-7,-40],[440,345],[388,290],[270,890],[10,-7],[60,253],[-531,-892],[388,290],[-388,-230],[340,85],[0,-13],[770,473],[0,73],[873,615],[-42,-175],[-6,-8],[49,176],[308,222],[170,27],[-485,-295],[170,27],[510,143],[-18,-156],[-63,-316],[-28,-121],[396,304],[472,774],[-14,-67],[-5,7],[-485,-295],[118,186],[-154,-7],[-7,-40],[-97,-35],[4,-9],[-18,-156],[0,-31],[-9,-124],[-300,-839],[-308,-352],[-425,-176],[-194,-100],[873,615],[413,676],[-90,-202],[220,140],[77,113],[-236,-402],[-9,-124],[63,230],[-255,-118],[472,774],[-56,-229],[90,228],[3,-8],[81,196],[970,680],[485,355],[-354,-598],[-385,-127],[-2,7],[531,872],[-680,-263],[-21,-94],[-118,-206],[616,393],[291,225],[-240,-657],[-5,-4],[1,-2],[485,355],[231,193],[-88,-147],[-291,-165],[-176,-229],[154,153],[-970,-620],[-77,33],[-60,-111],[30,162],[-18,-156],[425,114],[-177,-304],[-21,-94],[-10,9],[-352,-393],[154,153],[-220,-270],[44,-24],[-291,-165],[0,-31],[240,799],[-5,-9],[-70,-283],[-176,-229],[3,8],[-679,-425],[-385,-127],[396,304],[-308,-352],[-595,-234],[42,149],[-220,-270],[385,273],[-308,-87],[-54,-284],[680,201],[-154,-7],[-440,-475],[-531,-892],[-42,-175],[770,473],[118,186],[-385,-127],[154,153],[56,203],[-616,-247]], 24))
    for points, sol in examples:
        ans = Solution().maxPoints([Point(*args) for args in points])
        print(ans == sol, 'Actual: %s\tExpected: %s' % (ans, sol), sep='\t')


if __name__ == '__main__':
    main()
