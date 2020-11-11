#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from math import sqrt, cos, sin, asin, pi, atan


def rd(x):
    ret = round(x, 15)
    if ret == 0: return 0
    else: return ret


def solve(a):
    # area = cos y (sin x + cos x) + sin y
    # p1 = [0.5, 0, 0] -> 0.5 * [cos y, sin y, 0]
    # p2 = [0, 0.5, 0] -> 0.5 * [0, cos x, sin x] -> 0.5 * [- cos x sin y, cos x cos y, sin x]
    # p3 = [0, 0, 0.5] -> 0.5 * [0, - sin x, cos x] -> 0.5 * [sin x sin y, - sin x cos y, cos x]
    if a < sqrt(2):
        # when area <= 1.414..  y = 0
        # area = sin x + cos x = sqrt(2) * sin(x+pi/4)
        # p1 = [0.5, 0, 0]
        # p2 = 0.5[0, cos x, sin x]
        # p3 = 0.5[0, -sin x, cos x]
        x = asin(a/sqrt(2)) - pi/4
        return [[0.5, 0, 0],
                [0, rd(0.5*cos(x)), rd(0.5*sin(x))],
                [0, rd(-0.5*sin(x)), rd(0.5*cos(x))]]
    else:
        # let x = pi/4
        # area = sqrt(2) * cos y + sin y = 1/sqrt(3) * sin(y + atan(sqrt(2)))
        y = asin(a * sqrt(3)) - atan(sqrt(2))
        return [map(lambda x: rd(0.5*x), [cos(y), sin(y), 0]),
                map(lambda x: rd(0.5*x), [-cos(x)*sin(y), cos(x)*sin(y), sin(x)]),
                map(lambda x: rd(0.5*x), [sin(x)*sin(y), sin(x)*cos(y), cos(x)])]



def main():
    t = int(input())
    for i in range(1, t+1):
        a = float(input())
        print('Case #%s:' % i)
        for v in solve(a):
            print(' '.join(map(str, v)))


if __name__ == '__main__':
    main()
