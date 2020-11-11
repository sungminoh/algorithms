
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

	An integer point is a point that has integer coordinates. 
	A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
	ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
	length and width of each rectangle does not exceed 2000.
	1
	pick return a point as an array of integer coordinates [p_x, p_y]
	pick is called at most 10000 times.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]

Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
from collections import defaultdict
import sys
import random
from itertools import accumulate
from typing import List
import pytest


def binsearch(lst, v):
    i, j = 0, len(lst) - 1
    while i <= j:
        m = i + ((j - i) // 2)
        if lst[m] > v:
            j = m - 1
        elif lst[m] < v:
            i = m + 1
        else:
            return m
    return i


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.cum_sum = list(accumulate([(r[2] - r[0] + 1) * (r[3] - r[1] + 1) for r in rects]))

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = self.rects[binsearch(self.cum_sum, random.randint(1, self.cum_sum[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]


@pytest.mark.parametrize('commands, args', [
    (["Solution","pick","pick","pick"], [[[[1,1,5,5]]],[],[],[]]),
    (["Solution","pick","pick","pick","pick","pick"], [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]])
])
def test(commands, args):
    s = Solution(*args[0])
    for c, a in zip(commands[1:], args[1:]):
        print(getattr(s, c)(*a))


@pytest.mark.parametrize('rects', [
    ([[1,1,5,5]]),
    ([[-2,-2,-1,-1],[1,0,3,0]]),
])
def test_random(rects):
    def idx(x, y):
        for i, r in enumerate(rects):
            if r[0] <= x <= r[2] and r[1] <= y <= r[3]:
                return i
        assert False, (x, y)

    count = defaultdict(int)
    for _ in range(10000):
        x, y = Solution(rects).pick()
        count[idx(x, y)] += 1

    area = [(r[2] - r[0] + 1) * (r[3] - r[1] + 1) for r in rects]
    rate = area[0] / count[0]
    print()
    print(area)
    print(count)
    print(rate)
    for k, v in count.items():
        assert rate * 0.95 <= area[k] / v <= rate * 1.05




@pytest.mark.parametrize('lst, v, expected', [
    ([10, 20, 30], 0, 0),
    ([10, 20, 30], 5, 0),
    ([10, 20, 30], 10, 0),
    ([10, 20, 30], 15, 1),
    ([10, 20, 30], 20, 1),
    ([10, 20, 30], 25, 2),
    ([10, 20, 30], 30, 2),
])
def test_binsearch(lst, v, expected):
    assert expected == binsearch(lst, v)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))

