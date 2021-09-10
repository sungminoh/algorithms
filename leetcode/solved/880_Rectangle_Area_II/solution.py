#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.

Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.

Constraints:

	1 <= rectangles.length <= 200
	rectanges[i].length = 4
	0 <= rectangles[i][j] <= 109
	The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
"""
import sys
import bisect
from typing import List
import pytest


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)
        xs = list(xs)
        ys = list(ys)
        xs.sort()
        ys.sort()
        xm = {x: i for i, x in enumerate(xs)}
        ym = {y: i for i, y in enumerate(ys)}
        mat = [[False]*len(ys) for _ in range(len(xs))]
        for x1, y1, x2, y2 in rectangles:
            for i in range(xm[x1], xm[x2]):
                for j in range(ym[y1], ym[y2]):
                    mat[i][j] = True
        area = 0
        for i in range(len(xs)-1):
            for j in range(len(ys)-1):
                if mat[i][j]:
                    area += (((xs[i+1] - xs[i]) % MOD) * ((ys[j+1] - ys[j]) % MOD)) % MOD
                    area %= MOD
        return area

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))
            events.append((x2, 1, y1, y2))
        events.sort()

        def sum_interval(intervals):
            end = 0
            ret = 0
            for y1, y2 in intervals:
                start = max(end, y1)
                end = max(end, y2)
                ret += end-start
            return ret

        intervals = []
        area = 0
        prev_x = 0
        for x, typ, y1, y2 in events:
            if x != prev_x:
                area += (x-prev_x) * sum_interval(intervals) # O(n)
                area %= MOD
                prev_x = x
            if typ == 0:
                intervals.insert(bisect.bisect_right(intervals, (y1, y2)), (y1, y2))  # O(n)
            else:
                intervals.pop(bisect.bisect_left(intervals, (y1, y2)))  # O(n)
        return area


@pytest.mark.parametrize('rectangles, expected', [
    ([[0,0,2,2],[1,0,2,3],[1,0,3,1]], 6),
    ([[0,0,200,200],[100,0,200,300],[100,0,300,100]], 60000),
    ([[0,0,1000000000,1000000000]], 49),
    ([[471,0,947,999],[780,0,823,320],[868,0,948,538],[907,0,911,673],[929,0,952,596],[458,0,889,669],[156,0,364,754],[900,0,973,236],[406,0,620,454],[773,0,946,538],[407,0,834,23],[759,0,858,526],[431,0,776,599],[969,0,979,30],[642,0,737,339],[239,0,448,183],[260,0,517,903],[14,0,674,976],[251,0,850,112],[57,0,794,395],[595,0,728,149],[970,0,989,36],[496,0,954,791],[447,0,832,805],[829,0,939,100],[169,0,568,501],[704,0,969,411],[607,0,609,221],[935,0,953,437],[47,0,670,130],[794,0,799,230],[943,0,959,90],[332,0,337,732],[123,0,228,344],[281,0,487,598],[381,0,732,443],[235,0,391,548],[646,0,930,20],[219,0,675,95],[8,0,212,227],[138,0,704,658],[368,0,782,707],[810,0,826,957],[543,0,697,654],[887,0,986,180],[837,0,900,228],[280,0,391,331],[180,0,229,42],[201,0,489,687],[648,0,680,732],[228,0,630,922],[886,0,960,56],[946,0,955,522],[903,0,992,464],[557,0,860,38],[89,0,268,642],[669,0,774,185],[1,0,724,374],[395,0,923,782],[82,0,230,550],[166,0,166,808],[441,0,644,435],[497,0,823,224],[372,0,973,556],[188,0,846,127],[226,0,396,535],[869,0,945,575],[406,0,526,795],[781,0,795,569],[563,0,831,991],[466,0,486,641],[274,0,855,529],[61,0,819,364],[285,0,421,101],[193,0,950,748],[320,0,655,836],[207,0,627,945],[782,0,899,56],[578,0,970,913],[499,0,684,205],[490,0,877,16],[483,0,668,915],[364,0,741,16]], 957901),
])
def test(rectangles, expected):
    print()
    assert expected == Solution().rectangleArea(rectangles)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
