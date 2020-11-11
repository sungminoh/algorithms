
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 , and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

	The number of buildings in any input list is guaranteed to be in the range [0, 10000].
	The input list is already sorted in ascending order by the left x position Li.
	The output list must be sorted by the x position.
	There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
import sys
from heapq import heappush
from heapq import heappop
from typing import List
import pytest


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort(key=lambda x: (x[0], -x[2], x[1]))  # sort l, h, r
        heap = [(0, float('inf'))]  # -h, r
        ret = []
        for l, r, h in buildings:
            while heap[0][1] <= l:
                ph, pr = heappop(heap)
                while heap[0][0] == ph:
                    _, _pr =heappop(heap)
                    pr = max(pr, _pr)
                while heap[0][1] <= pr:
                    heappop(heap)
                if pr < l or -heap[0][0] >= h:
                    ret.append([pr, -heap[0][0]])
            if h > -heap[0][0] and (not ret or h != ret[-1][1]):
                ret.append([l, h])
            heappush(heap, (-h, r))

        while len(heap) > 1:
            ph, pr = heappop(heap)
            while heap[0][0] == ph:
                _, _pr =heappop(heap)
                pr = max(pr, _pr)
            while heap[0][1] <= pr:
                heappop(heap)
            ret.append([pr, -heap[0][0]])
        return ret


@pytest.mark.parametrize('buildings, expected', [
    ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
    ([[0,2,3],[2,5,3]], [[0,3],[5,0]]),
    ([[1,2,1],[1,2,2],[1,2,3]], [[1,3],[2,0]]),
    ([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]], [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]),
])
def test(buildings, expected):
    assert expected == Solution().getSkyline(buildings)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
