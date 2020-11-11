
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

	input and output values are in floating-point.
	radius and x-y position of the center of the circle is passed into the class constructor.
	a point on the circumference of the circle is considered to be in the circle.
	randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
import sys
import math
import random
from typing import List
import pytest


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def get_random(self):
        x = random.random()
        y = 2 * random.random()
        if y > 2 * x:
            x = 1 - x
        return x

    def randPoint(self) -> List[float]:
        r = self.r * self.get_random()
        theta = 2 * math.pi * random.random()
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]


@pytest.mark.parametrize('commands, args', [
    (["Solution","randPoint","randPoint","randPoint"], [[1,0,0],[],[],[]]),
    (["Solution","randPoint","randPoint","randPoint"], [[10,5,-7.5],[],[],[]])
])
def test(commands, args):
    s = Solution(*args[0])
    for c, a in zip(commands[1:], args[1:]):
        print(getattr(s, c)(*a))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
